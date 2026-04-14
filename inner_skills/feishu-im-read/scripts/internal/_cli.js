/**
 * _cli.js — feishu-im-read skill CLI 框架
 *
 * 所有飞书 API 调用通过 Go 服务代理完成，JS 侧不持有任何凭证（app_secret / access_token）。
 * 认证参数从环境变量 IRIS_USER_CLOUD_JWT 或 BUILD_TOKEN 读取，通过 Authorization: Bearer 传给 Go 服务。
 * 代理端点从环境变量 IRIS_RUNTIME_AIME_API_HOST 读取（格式如 http://host:port）。
 *
 * 本地调试时可通过命令行参数传入：
 *   --proxy-endpoint http://localhost:8080/api/agents/v2/internal/proxy
 *   --jwt-token <token>
 */

import { readFile } from "node:fs/promises";
import { buildAuthCard, buildAuthSuccessCard, buildAuthFailedCard } from "./_utils.js";

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const cur = argv[i];
    if (!cur.startsWith("--")) {
      args._.push(cur);
      continue;
    }
    const eq = cur.indexOf("=");
    if (eq !== -1) {
      const k = cur.slice(2, eq);
      const v = cur.slice(eq + 1);
      args[k] = v;
      continue;
    }
    const k = cur.slice(2);
    const next = argv[i + 1];
    if (next && !next.startsWith("--")) {
      args[k] = next;
      i++;
    } else {
      args[k] = true;
    }
  }
  return args;
}

async function readStdinText() {
  const chunks = [];
  for await (const chunk of process.stdin) {
    chunks.push(Buffer.isBuffer(chunk) ? chunk : Buffer.from(String(chunk)));
  }
  return Buffer.concat(chunks).toString("utf8").trim();
}

async function readJsonInput(args) {
  if (typeof args["input-file"] === "string" && args["input-file"].length > 0) {
    const raw = await readFile(args["input-file"], "utf8");
    return JSON.parse(raw);
  }
  if (typeof args.input === "string" && args.input.length > 0) {
    return JSON.parse(args.input);
  }
  const raw = await readStdinText();
  if (!raw) {
    throw new Error("missing input JSON (use --input, --input-file, or stdin)");
  }
  return JSON.parse(raw);
}

export const DEFAULT_P2P_LANE_ID = "default_p2p_lane_id";

export function assertOk(res) {
  if (!res || typeof res !== "object") {
    throw new Error("empty response");
  }
  const code = res.code ?? res?.data?.code;
  if (code !== 0) {
    const msg = res.msg ?? res?.data?.msg ?? "Lark API error";
    const err = new Error(`${msg} (code=${code})`);
    err.code = code;
    err.response = res;
    throw err;
  }
}

/**
 * 尝试从 /tmp/.cloud_token 文件读取最新的 Cloud JWT token。
 * jwt_manager.go 会定时刷新并写入该文件。
 * 本地调试时文件不存在则返回 null。
 */
async function tryReadCloudTokenFile() {
  try {
    const token = await readFile("/tmp/.cloud_token", "utf8");
    return token.trim() || null;
  } catch {
    return null;
  }
}

/**
 * proxyOAuth — 代替 fetch 直接调飞书 OAuth 端点。
 */
export async function proxyOAuth(proxyEndpoint, jwtToken, targetUrl, options = {}) {
  const res = await fetch(`${proxyEndpoint}/lark_oauth`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "authorization": `Byte-Cloud-JWT ${jwtToken}`,
    },
    body: JSON.stringify({
      target_url: targetUrl,
      method: options.method || "POST",
      form_fields: options.formFields || undefined,
      json_body: options.jsonBody || undefined,
      headers: options.headers || undefined,
    }),
  });

  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(`OAuth proxy failed: HTTP ${res.status} – ${text.slice(0, 200)}`);
  }

  const data = await res.json();
  return {
    ok: res.ok,
    status: res.status,
    json: async () => data,
    text: async () => JSON.stringify(data),
  };
}

/**
 * notifyAuthCallback — 授权成功后将 token 上报给 Go 服务
 */
async function notifyAuthCallback(proxyEndpoint, jwtToken, sessionID, token) {
  try {
    const res = await fetch(`${proxyEndpoint}/lark_auth_callback`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "authorization": `Byte-Cloud-JWT ${jwtToken}`,
      },
      body: JSON.stringify({
        session_id: sessionID,
        access_token: token.accessToken,
        refresh_token: token.refreshToken,
        expires_in: token.expiresIn,
        refresh_expires_in: token.refreshExpiresIn,
        scope: token.scope,
      }),
    });
    if (!res.ok) {
      const text = await res.text().catch(() => "");
      console.error(`[authCallback] failed: HTTP ${res.status} – ${text.slice(0, 200)}`);
    }
  } catch (e) {
    console.error(`[authCallback] request error: ${e.message}`);
  }
}

/**
 * buildProxyClient 构建飞书 SDK 代理对象。
 */
function buildProxyClient(proxyEndpoint, jwtToken) {
  const headers = {
    "Content-Type": "application/json",
    "authorization": `Byte-Cloud-JWT ${jwtToken}`,
  };

  /**
   * 自动授权流程
   */
  async function runAuthFlow(missingScopes, reason = "Continue operation") {
    const senderOpenId = process.env.IRIS_SENDER_OPEN_ID;
    if (!senderOpenId) {
      console.error("[AutoAuth] Missing IRIS_SENDER_OPEN_ID, cannot send auth card.");
      return false;
    }

    // 0. Check application scopes
    let validScopes = missingScopes;
    try {
      const appScopesRes = await callProxy("application.v6.scope.list", {}, {}, {}, false);
      if (appScopesRes.code === 0 && appScopesRes.data?.scopes) {
        // Build set of all available scope names from response
        const appScopeSet = new Set((appScopesRes.data.scopes || []).map(s => s.scope_name));
        
        // Filter missingScopes against available scopes
        validScopes = missingScopes.filter(s => appScopeSet.has(s));
        
        const dropped = missingScopes.filter(s => !appScopeSet.has(s));
        if (dropped.length > 0) {
          console.warn(`[AutoAuth] Dropped scopes not configured in app: ${dropped.join(", ")}`);
        }
      }
    } catch (e) {
      // If scope check fails (e.g. permission error), warn but proceed with original scopes
      console.warn(`[AutoAuth] Failed to check app scopes, proceeding with all requested scopes. Error: ${e.message}`);
    }

    if (validScopes.length === 0) {
      console.error("[AutoAuth] Error: The application has NOT been configured with the requested permissions. Please ask the Feishu App Administrator to add these scopes in the Feishu Open Platform console. Agent cannot resolve this issue automatically.");
      return false;
    }

    const scopeStr = validScopes.join(" ");
    // offline_access 由 Go 侧在发起 device_authorization 时自动保留
    const finalScope = scopeStr.includes("offline_access") ? scopeStr : `${scopeStr} offline_access`;

    console.log(`[AutoAuth] Requesting scopes: ${finalScope}`);

    // 1. 发起 Device Authorization
    const deviceAuthProxy = await proxyOAuth(
      proxyEndpoint,
      jwtToken,
      "https://accounts.feishu.cn/oauth/v1/device_authorization",
      {
        method: "POST",
        formFields: { scope: finalScope },
      }
    );
    const deviceAuthData = await deviceAuthProxy.json();
    if (!deviceAuthProxy.ok || deviceAuthData.error) {
        console.error("[AutoAuth] Device authorization failed:", deviceAuthData.error_description || deviceAuthData.error);
        return false;
    }

    const { device_code, verification_uri_complete, expires_in, interval } = deviceAuthData;

    // 2. Build Card & Send (using tenant token)
    const card = buildAuthCard({
        verificationUriComplete: verification_uri_complete,
        expiresMin: Math.ceil(expires_in / 60),
        scope: scopeStr,
        reason,
    });

    const receiveIdType = senderOpenId.startsWith("ou_") ? "open_id" : "chat_id";
    const sendRes = await callProxy("im.v1.message.create", {}, { receive_id_type: receiveIdType }, {
        receive_id: senderOpenId,
        msg_type: "interactive",
        content: JSON.stringify(card),
    }, false); // useUserToken=false

    if (sendRes.code !== 0) {
        console.error("[AutoAuth] Failed to send auth card:", sendRes.msg);
        return false;
    }
    const messageId = sendRes.data.message_id;
    console.log(`[AutoAuth] Auth card sent (msgId: ${messageId}). Waiting for authorization...`);

    // 3. Poll for Token
    const tokenUrl = "https://open.feishu.cn/open-apis/authen/v2/oauth/token";
    const deadline = Date.now() + expires_in * 1000;
    let currentInterval = interval;
    let authResult = { ok: false, message: "Timeout" };

    while (Date.now() < deadline) {
        await new Promise(r => setTimeout(r, currentInterval * 1000));
        try {
            const pollProxy = await proxyOAuth(proxyEndpoint, jwtToken, tokenUrl, {
                method: "POST",
                formFields: {
                    grant_type: "urn:ietf:params:oauth:grant-type:device_code",
                    device_code: device_code,
                },
            });
            const data = await pollProxy.json();
            if (data.access_token) {
                authResult = {
                    ok: true,
                    token: {
                        accessToken: data.access_token,
                        refreshToken: data.refresh_token,
                        expiresIn: data.expires_in,
                        refreshExpiresIn: data.refresh_token_expires_in,
                        scope: data.scope,
                    },
                };
                break;
            }
            const error = data.error;
            if (error === "authorization_pending") continue;
            if (error === "slow_down") { currentInterval += 5; continue; }
            if (error === "access_denied") { authResult = { ok: false, message: "用户拒绝了授权请求" }; break; }
            if (error === "expired_token" || error === "invalid_grant") { 
                authResult = { 
                    ok: false, 
                    message: "授权超时，请重新发起",
                    isTimeout: true
                }; 
                break; 
            }
            authResult = { ok: false, message: data.error_description || data.error || "Unknown error" };
            break;
        } catch (e) {
            continue;
        }
    }

    // 4. Update Card & Callback
    if (authResult.ok) {
        console.log("[AutoAuth] Authorization successful!");
        await notifyAuthCallback(proxyEndpoint, jwtToken, process.env.IRIS_SESSION_ID || "", authResult.token);
        await callProxy("im.v1.message.patch", { message_id: messageId }, {}, {
            content: JSON.stringify(buildAuthSuccessCard()),
        }, false);
        return true;
    } else {
        console.error(`[AutoAuth] Authorization failed: ${authResult.message}`);
        const failScope = authResult.isTimeout ? scopeStr : undefined;
        const failAppReason = authResult.isTimeout ? reason : undefined;
        await callProxy("im.v1.message.patch", { message_id: messageId }, {}, {
            content: JSON.stringify(buildAuthFailedCard(authResult.message, failScope, failAppReason)),
        }, false);
        return false;
    }
  }

  /**
   * 发起代理请求
   */
  async function callProxy(methodName, path, query, body, useUserToken, httpMethod, urlPath, retryCount = 0) {
    const queryObj = {};
    if (query && typeof query === "object") {
      for (const [k, v] of Object.entries(query)) {
        if (v !== undefined && v !== null) queryObj[k] = String(v);
      }
    }
    const reqBody = JSON.stringify({
      method_name: methodName,
      path: path && Object.keys(path).length > 0 ? path : undefined,
      query: Object.keys(queryObj).length > 0 ? queryObj : undefined,
      body: body !== undefined && body !== null ? body : undefined,
      use_user_token: useUserToken,
      http_method: httpMethod || undefined,
      url_path: urlPath || undefined,
    });
    
    let res = await fetch(`${proxyEndpoint}/lark_api`, {
      method: "POST",
      headers,
      body: reqBody,
    });
    if (res.status === 401) {
      const newToken = await tryReadCloudTokenFile();
      const currentToken = headers["authorization"].startsWith("Byte-Cloud-JWT ") ? headers["authorization"].slice("Byte-Cloud-JWT ".length) : headers["authorization"];
      if (newToken && newToken !== currentToken) {
        headers["authorization"] = `Byte-Cloud-JWT ${newToken}`;
        res = await fetch(`${proxyEndpoint}/lark_api`, {
          method: "POST",
          headers,
          body: reqBody,
        });
      }
    }

    let json;
    try {
      json = await res.json();
    } catch (e) {
      if (!res.ok) {
        const text = await res.text().catch(() => "");
        throw new Error(`Proxy request failed: HTTP ${res.status} – ${text.slice(0, 200)}`);
      }
      throw e;
    }

    if (!res.ok && json?.code !== 99991679) {
       throw new Error(`Proxy request failed: HTTP ${res.status} – ${JSON.stringify(json).slice(0, 200)}`);
    }
    
    // Intercept 99991679 (Unauthorized)
    if (json.code === 99991679 && useUserToken && retryCount < 1) {
       let missingScopes = [];
       const violations = json.error?.permission_violations || json.error?.error?.permission_violations || [];
       missingScopes = violations.map(v => v.subject).filter(Boolean);
       
       // Fallback: Parse from msg if permissions_violations is empty
       if (missingScopes.length === 0 && json.msg) {
          const match = json.msg.match(/identity:\s*\[([^\]]+)\]/);
          if (match && match[1]) {
             missingScopes = match[1].split(",").map(s => s.trim()).filter(Boolean);
          }
       }

       if (missingScopes.length > 0) {
           console.log(`[AutoAuth] Encountered 99991679. Missing scopes: ${missingScopes.join(", ")}`);
           const authSuccess = await runAuthFlow(missingScopes, sdk.authReason);
           if (authSuccess) {
               console.log("[AutoAuth] Auth successful. Please retry the operation.");
               throw new Error("Authorization successful. Please retry the operation to continue.");
           } else {
               throw new Error(`Auto-authorization failed: User did not approve the request for scopes [${missingScopes.join(", ")}] within the time limit or denied it. You may retry the tool call to trigger the authorization flow again.`);
           }
       }
    }

    return json;
  }

  function isUserToken(opts) {
    return opts && opts.__use_user_token === true;
  }

  function makeChainProxy(pathParts) {
    const handler = {
      apply(_, __, args) {
        const [callParams, opts] = args;
        const methodName = pathParts.join(".");
        if (methodName === "request") {
          const httpMethod = callParams?.method || "GET";
          const urlPath = callParams?.url || "";
          const query = callParams?.params || {};
          const body = callParams?.data;
          return callProxy("request", {}, query, body, isUserToken(opts), httpMethod, urlPath);
        }
        const path = callParams?.path || {};
        const query = callParams?.params || {};
        const body = callParams?.data;
        return callProxy(methodName, path, query, body, isUserToken(opts));
      },
      get(target, prop) {
        if (prop in target) return target[prop];
        if (typeof prop !== "string") return undefined;
        return makeChainProxy([...pathParts, prop]);
      },
      set(target, prop, value) {
        target[prop] = value;
        return true;
      }
    };
    return new Proxy(function () {}, handler);
  }

  const sdk = makeChainProxy([]);
  sdk.withUserAccessToken = (token) => ({ __use_user_token: true, _token: token });
  sdk.authReason = "Continue operation";
  return sdk;
}

export function withUserAccessToken(_token) {
  return { __use_user_token: true };
}

export async function runCli(run) {
  const args = parseArgs(process.argv.slice(2));
  if (args.help || args.h) {
    process.stdout.write(
        [
          "Usage:",
          "  node scripts/<tool>.js --input '<json>'",
          "  node scripts/<tool>.js --input-file ./params.json",
          "  cat params.json | node scripts/<tool>.js",
          "",
          "Proxy mode (server-side, via env vars):",
          "  IRIS_USER_CLOUD_JWT=<token> 或 BUILD_TOKEN=<token> IRIS_RUNTIME_AIME_API_HOST=http://host:port node scripts/<tool>.js",
          "",
          "Or via flags (for local testing, requires running Go server):",
          "  --proxy-endpoint http://localhost:8080/api/agents/v2/internal/proxy",
          "  --jwt-token <token>",
          "",
        ].join("\n"),
    );
    return;
  }

  const input = await readJsonInput(args);

  const proxyConfig = input.__proxy__ || {};
  const aimeAPIHost = process.env.IRIS_RUNTIME_AIME_API_HOST || "";
  const proxyEndpoint = aimeAPIHost
      ? `https://${aimeAPIHost}/api/agents/v2/internal/proxy`
      : (proxyConfig.proxy_endpoint || args["proxy-endpoint"]);

  const jwtToken = process.env.IRIS_USER_CLOUD_JWT || process.env.BUILD_TOKEN || args["jwt-token"];

  if (!jwtToken) {
    throw new Error(
        "missing JWT token (env IRIS_USER_CLOUD_JWT or BUILD_TOKEN or --jwt-token). " +
        "This script must be invoked with include_secrets=true in the agent environment."
    );
  }
  if (!proxyEndpoint) {
    throw new Error(
        "missing proxy endpoint (env IRIS_RUNTIME_AIME_API_HOST or --proxy-endpoint)."
    );
  }

  const sdk = buildProxyClient(proxyEndpoint, jwtToken);
  const opts = withUserAccessToken(null);

  const { __proxy__: _proxy, ...businessInput } = input;

  try {
    const out = await run({ sdk, opts, input: businessInput, args });
    if (out !== undefined) {
      process.stdout.write(`${JSON.stringify(out, null, 2)}\n`);
    }
  } catch (error) {
    if (error.message && error.message.startsWith("Authorization successful")) {
      console.log(JSON.stringify({
        authorization_status: "success",
        message: error.message
      }, null, 2));
      return; // Exit gracefully
    }
    console.error(error);
    process.exit(1);
  }
}
