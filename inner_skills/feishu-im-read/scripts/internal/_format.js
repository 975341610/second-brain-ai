/**
 * _format.js — 飞书消息格式化模块
 *
 * 将飞书 IM API 返回的原始消息转换为 AI 可读格式。
 * 纯 JS 实现，无三方依赖。
 *
 * 逻辑对齐官方 feishu-openclaw-plugin 的 format-messages + content converters。
 */

import { convertInteractive } from "./card/index.js";

const BJ_OFFSET_MS = 8 * 60 * 60 * 1000;

// ===========================================================================
// Utility Functions
// ===========================================================================

function safeParse(raw) {
  try {
    return JSON.parse(raw);
  } catch {
    return undefined;
  }
}

function escapeRegExp(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function formatDuration(ms) {
  const seconds = ms / 1000;
  if (seconds < 1) return `${ms}ms`;
  if (Number.isInteger(seconds)) return `${seconds}s`;
  return `${seconds.toFixed(1)}s`;
}

/** 毫秒时间戳 → "YYYY-MM-DD HH:mm"（北京时间） */
function millisToDatetime(ms) {
  const num = Number(ms);
  if (!Number.isFinite(num)) return String(ms);
  const d = new Date(num + BJ_OFFSET_MS);
  const y = d.getUTCFullYear();
  const mo = String(d.getUTCMonth() + 1).padStart(2, "0");
  const da = String(d.getUTCDate()).padStart(2, "0");
  const h = String(d.getUTCHours()).padStart(2, "0");
  const mi = String(d.getUTCMinutes()).padStart(2, "0");
  return `${y}-${mo}-${da} ${h}:${mi}`;
}

/** 毫秒时间戳字符串 → ISO 8601 北京时间 */
function millisStringToDateTime(millis) {
  const ms = parseInt(millis, 10);
  const d = new Date(ms + BJ_OFFSET_MS);
  const y = d.getUTCFullYear();
  const mo = String(d.getUTCMonth() + 1).padStart(2, "0");
  const da = String(d.getUTCDate()).padStart(2, "0");
  const h = String(d.getUTCHours()).padStart(2, "0");
  const mi = String(d.getUTCMinutes()).padStart(2, "0");
  const s = String(d.getUTCSeconds()).padStart(2, "0");
  return `${y}-${mo}-${da}T${h}:${mi}:${s}+08:00`;
}

/** 毫秒时间戳 → RFC 3339 北京时间（用于 merge_forward 子消息） */
function formatTimestamp(ms) {
  const d = new Date(ms);
  const utcMs = d.getTime() + d.getTimezoneOffset() * 60_000;
  const bjDate = new Date(utcMs + 8 * 3_600_000);
  const y = bjDate.getFullYear();
  const mo = String(bjDate.getMonth() + 1).padStart(2, "0");
  const da = String(bjDate.getDate()).padStart(2, "0");
  const h = String(bjDate.getHours()).padStart(2, "0");
  const mi = String(bjDate.getMinutes()).padStart(2, "0");
  const s = String(bjDate.getSeconds()).padStart(2, "0");
  return `${y}-${mo}-${da}T${h}:${mi}:${s}+08:00`;
}

function indentLines(text, indent) {
  return text
    .split("\n")
    .map((line) => `${indent}${line}`)
    .join("\n");
}

// ===========================================================================
// Mention Helpers
// ===========================================================================

/** 从 mention 的 id 字段提取 open_id（兼容事件推送的对象格式和 API 响应的字符串格式） */
function extractMentionOpenId(id) {
  if (typeof id === "string") return id;
  if (id != null && typeof id === "object" && "open_id" in id) {
    const openId = id.open_id;
    return typeof openId === "string" ? openId : "";
  }
  return "";
}

/** 将消息文本中的 mention 占位符替换为 @name */
function resolveMentions(text, ctx) {
  if (!ctx.mentions || ctx.mentions.size === 0) return text;
  let result = text;
  for (const [key, info] of ctx.mentions) {
    result = result.replace(
      new RegExp(escapeRegExp(key), "g"),
      `@${info.name}`,
    );
  }
  return result;
}

/** 从 API message item 构建 ConvertContext */
function buildConvertContextFromItem(item, fallbackMessageId) {
  const mentions = new Map();
  const mentionsByOpenId = new Map();
  for (const m of item.mentions ?? []) {
    const openId = extractMentionOpenId(m.id);
    if (!openId) continue;
    const info = { key: m.key, openId, name: m.name ?? "", isBot: false };
    mentions.set(m.key, info);
    mentionsByOpenId.set(openId, info);
  }
  return {
    mentions,
    mentionsByOpenId,
    messageId: item.message_id ?? fallbackMessageId,
  };
}

// ===========================================================================
// Content Converters
// ===========================================================================

// ---- text ----

function convertText(raw, ctx) {
  const parsed = safeParse(raw);
  const text = parsed?.text ?? raw;
  return { content: resolveMentions(text, ctx), resources: [] };
}

// ---- post (rich text) ----

const LOCALE_PRIORITY = ["zh_cn", "en_us", "ja_jp"];

function unwrapLocale(parsed) {
  if ("title" in parsed || "content" in parsed) return parsed;
  for (const locale of LOCALE_PRIORITY) {
    const localeData = parsed[locale];
    if (localeData != null && typeof localeData === "object") return localeData;
  }
  const firstKey = Object.keys(parsed)[0];
  if (firstKey) {
    const firstValue = parsed[firstKey];
    if (firstValue != null && typeof firstValue === "object") return firstValue;
  }
  return undefined;
}

function applyStyle(text, style) {
  if (!style || style.length === 0) return text;
  let result = text;
  if (style.includes("bold")) result = `**${result}**`;
  if (style.includes("italic")) result = `*${result}*`;
  if (style.includes("underline")) result = `<u>${result}</u>`;
  if (style.includes("lineThrough")) result = `~~${result}~~`;
  if (style.includes("codeInline")) result = `\`${result}\``;
  return result;
}

function renderPostElement(el, ctx, resources) {
  switch (el.tag) {
    case "text": {
      let text = el.text ?? "";
      return applyStyle(text, el.style);
    }
    case "a": {
      const text = el.text ?? el.href ?? "";
      return el.href ? `[${text}](${el.href})` : text;
    }
    case "at": {
      const userId = el.user_id ?? "";
      if (userId === "all") return "@all";
      const name = el.user_name ?? userId;
      const info = ctx.mentionsByOpenId?.get(userId);
      if (info) return info.key;
      return `@${name}`;
    }
    case "img":
      if (el.image_key) {
        resources.push({ type: "image", fileKey: el.image_key });
        return `![image](${el.image_key})`;
      }
      return "";
    case "media":
      if (el.file_key) {
        resources.push({ type: "file", fileKey: el.file_key });
        return `<file key="${el.file_key}"/>`;
      }
      return "";
    case "code_block": {
      const lang = el.language ?? "";
      const code = el.text ?? "";
      return `\n\`\`\`${lang}\n${code}\n\`\`\`\n`;
    }
    case "hr":
      return "\n---\n";
    default:
      return el.text ?? "";
  }
}

function convertPost(raw, ctx) {
  const rawParsed = safeParse(raw);
  if (rawParsed == null || typeof rawParsed !== "object") {
    return { content: "[rich text message]", resources: [] };
  }
  const parsed = unwrapLocale(rawParsed);
  if (!parsed) return { content: "[rich text message]", resources: [] };

  const resources = [];
  const lines = [];
  if (parsed.title) lines.push(`**${parsed.title}**`, "");

  for (const paragraph of parsed.content ?? []) {
    if (!Array.isArray(paragraph)) continue;
    let line = "";
    for (const el of paragraph) {
      line += renderPostElement(el, ctx, resources);
    }
    lines.push(line);
  }

  let content = lines.join("\n").trim() || "[rich text message]";
  content = resolveMentions(content, ctx);
  return { content, resources };
}

// ---- image ----

function convertImage(raw) {
  const parsed = safeParse(raw);
  const imageKey = parsed?.image_key;
  if (!imageKey) return { content: "[image]", resources: [] };
  return {
    content: `![image](${imageKey})`,
    resources: [{ type: "image", fileKey: imageKey }],
  };
}

// ---- file ----

function convertFile(raw) {
  const parsed = safeParse(raw);
  const fileKey = parsed?.file_key;
  if (!fileKey) return { content: "[file]", resources: [] };
  const fileName = parsed?.file_name ?? "";
  const nameAttr = fileName ? ` name="${fileName}"` : "";
  return {
    content: `<file key="${fileKey}"${nameAttr}/>`,
    resources: [{ type: "file", fileKey, fileName: fileName || undefined }],
  };
}

// ---- audio ----

function convertAudio(raw) {
  const parsed = safeParse(raw);
  const fileKey = parsed?.file_key;
  if (!fileKey) return { content: "[audio]", resources: [] };
  const duration = parsed?.duration;
  const durationAttr =
    duration != null ? ` duration="${formatDuration(duration)}"` : "";
  return {
    content: `<audio key="${fileKey}"${durationAttr}/>`,
    resources: [{ type: "audio", fileKey, duration: duration ?? undefined }],
  };
}

// ---- video / media ----

function convertVideo(raw) {
  const parsed = safeParse(raw);
  const fileKey = parsed?.file_key;
  if (!fileKey) return { content: "[video]", resources: [] };
  const fileName = parsed?.file_name ?? "";
  const duration = parsed?.duration;
  const coverKey = parsed?.image_key;
  const nameAttr = fileName ? ` name="${fileName}"` : "";
  const durationAttr =
    duration != null ? ` duration="${formatDuration(duration)}"` : "";
  return {
    content: `<video key="${fileKey}"${nameAttr}${durationAttr}/>`,
    resources: [
      {
        type: "video",
        fileKey,
        fileName: fileName || undefined,
        duration: duration ?? undefined,
        coverImageKey: coverKey ?? undefined,
      },
    ],
  };
}

// ---- sticker ----

function convertSticker(raw) {
  const parsed = safeParse(raw);
  const fileKey = parsed?.file_key;
  if (!fileKey) return { content: "[sticker]", resources: [] };
  return {
    content: `<sticker key="${fileKey}"/>`,
    resources: [{ type: "sticker", fileKey }],
  };
}

// ---- share_chat / share_user ----

function convertShareChat(raw) {
  const parsed = safeParse(raw);
  return {
    content: `<group_card id="${parsed?.chat_id ?? ""}"/>`,
    resources: [],
  };
}

function convertShareUser(raw) {
  const parsed = safeParse(raw);
  return {
    content: `<contact_card id="${parsed?.user_id ?? ""}"/>`,
    resources: [],
  };
}

// ---- location ----

function convertLocation(raw) {
  const parsed = safeParse(raw);
  const name = parsed?.name ?? "";
  const lat = parsed?.latitude ?? "";
  const lng = parsed?.longitude ?? "";
  const nameAttr = name ? ` name="${name}"` : "";
  const coordsAttr = lat && lng ? ` coords="lat:${lat},lng:${lng}"` : "";
  return { content: `<location${nameAttr}${coordsAttr}/>`, resources: [] };
}

// ---- system ----

function convertSystem(raw) {
  const parsed = safeParse(raw);
  if (!parsed?.template)
    return { content: "[system message]", resources: [] };

  let content = parsed.template;
  const replacements = {
    "{from_user}": parsed.from_user?.length
      ? parsed.from_user.filter(Boolean).join(", ")
      : undefined,
    "{to_chatters}": parsed.to_chatters?.length
      ? parsed.to_chatters.filter(Boolean).join(", ")
      : undefined,
    "{divider_text}": parsed.divider_text?.text,
  };
  for (const [placeholder, value] of Object.entries(replacements)) {
    content = content.replaceAll(placeholder, value ?? "");
  }
  return { content: content.trim(), resources: [] };
}

// ---- calendar (share_calendar_event / calendar / general_calendar) ----

function formatCalendarContent(parsed) {
  const summary = parsed?.summary ?? "";
  const parts = [];
  if (summary) parts.push(summary);
  const start = parsed?.start_time
    ? millisToDatetime(parsed.start_time)
    : "";
  const end = parsed?.end_time ? millisToDatetime(parsed.end_time) : "";
  if (start && end) parts.push(`${start} ~ ${end}`);
  else if (start) parts.push(start);
  return parts.join("\n") || "[calendar event]";
}

function convertShareCalendarEvent(raw) {
  const parsed = safeParse(raw);
  return {
    content: `<calendar_share>${formatCalendarContent(parsed)}</calendar_share>`,
    resources: [],
  };
}

function convertCalendar(raw) {
  const parsed = safeParse(raw);
  return {
    content: `<calendar_invite>${formatCalendarContent(parsed)}</calendar_invite>`,
    resources: [],
  };
}

function convertGeneralCalendar(raw) {
  const parsed = safeParse(raw);
  return {
    content: `<calendar>${formatCalendarContent(parsed)}</calendar>`,
    resources: [],
  };
}

// ---- video_chat ----

function convertVideoChat(raw) {
  const parsed = safeParse(raw);
  const topic = parsed?.topic ?? "";
  const parts = [];
  if (topic) parts.push(topic);
  if (parsed?.start_time) parts.push(millisToDatetime(parsed.start_time));
  const inner = parts.join("\n") || "[video chat]";
  return { content: `<meeting>${inner}</meeting>`, resources: [] };
}

// ---- todo ----

function extractPlainText(content) {
  const lines = [];
  for (const paragraph of content) {
    if (!Array.isArray(paragraph)) continue;
    let line = "";
    for (const el of paragraph) {
      if (el.text) line += el.text;
    }
    lines.push(line);
  }
  return lines.join("\n").trim();
}

function convertTodo(raw) {
  const parsed = safeParse(raw);
  const parts = [];
  const title = parsed?.summary?.title ?? "";
  const body = parsed?.summary?.content
    ? extractPlainText(parsed.summary.content)
    : "";
  const fullTitle = [title, body].filter(Boolean).join("\n");
  if (fullTitle) parts.push(fullTitle);
  if (parsed?.due_time)
    parts.push(`Due: ${millisToDatetime(parsed.due_time)}`);
  const inner = parts.join("\n") || "[todo]";
  return { content: `<todo>\n${inner}\n</todo>`, resources: [] };
}

// ---- vote ----

function convertVote(raw) {
  const parsed = safeParse(raw);
  const topic = parsed?.topic ?? "";
  const options = parsed?.options ?? [];
  const parts = [];
  if (topic) parts.push(topic);
  for (const opt of options) parts.push(`• ${opt}`);
  const inner = parts.join("\n") || "[vote]";
  return { content: `<vote>\n${inner}\n</vote>`, resources: [] };
}

// ---- hongbao ----

function convertHongbao(raw) {
  const parsed = safeParse(raw);
  const text = parsed?.text;
  const textAttr = text ? ` text="${text}"` : "";
  return { content: `<hongbao${textAttr}/>`, resources: [] };
}

// ---- folder ----

function convertFolder(raw) {
  const parsed = safeParse(raw);
  const fileKey = parsed?.file_key;
  if (!fileKey) return { content: "[folder]", resources: [] };
  const fileName = parsed?.file_name ?? "";
  const nameAttr = fileName ? ` name="${fileName}"` : "";
  return {
    content: `<folder key="${fileKey}"${nameAttr}/>`,
    resources: [{ type: "file", fileKey, fileName: fileName || undefined }],
  };
}

// ---- unknown (fallback) ----

function convertUnknown(raw) {
  const parsed = safeParse(raw);
  if (parsed != null && typeof parsed === "object" && "text" in parsed) {
    const text = parsed.text;
    if (typeof text === "string") return { content: text, resources: [] };
  }
  return { content: "[unsupported message]", resources: [] };
}

// ---- merge_forward ----

async function convertMergeForward(_raw, ctx) {
  if (!ctx.fetchSubMessages) {
    return { content: "<forwarded_messages/>", resources: [] };
  }
  const messageId = ctx.messageId;

  let items;
  try {
    items = await ctx.fetchSubMessages(messageId);
  } catch {
    return { content: "<forwarded_messages/>", resources: [] };
  }
  if (!items || items.length === 0) {
    return { content: "<forwarded_messages/>", resources: [] };
  }

  // 构建 parent → children 映射
  const childrenMap = new Map();
  for (const item of items) {
    if (item.message_id === messageId && !item.upper_message_id) continue;
    const parentId = item.upper_message_id ?? messageId;
    let children = childrenMap.get(parentId);
    if (!children) {
      children = [];
      childrenMap.set(parentId, children);
    }
    children.push(item);
  }
  for (const children of childrenMap.values()) {
    children.sort((a, b) => {
      const ta = parseInt(String(a.create_time ?? "0"), 10);
      const tb = parseInt(String(b.create_time ?? "0"), 10);
      return ta - tb;
    });
  }

  // 批量解析 sender 名字
  const senderIds = [
    ...new Set(
      items
        .filter(
          (item) =>
            !(item.message_id === messageId && !item.upper_message_id),
        )
        .map((item) =>
          item.sender?.sender_type === "user" ? item.sender.id : undefined,
        )
        .filter(Boolean),
    ),
  ];
  if (senderIds.length > 0 && ctx.batchResolveNames) {
    try {
      await ctx.batchResolveNames(senderIds);
    } catch {
      /* best-effort */
    }
  }

  const content = await formatSubTree(
    messageId,
    childrenMap,
    ctx.resolveUserName,
  );
  return { content, resources: [] };
}

async function formatSubTree(parentId, childrenMap, resolveUserName) {
  const children = childrenMap.get(parentId);
  if (!children || children.length === 0) return "<forwarded_messages/>";

  const parts = [];
  for (const item of children) {
    try {
      const msgType = item.msg_type ?? "text";
      const senderId = item.sender?.id ?? "unknown";
      const createTime = item.create_time
        ? parseInt(String(item.create_time), 10)
        : undefined;
      const timestamp = createTime ? formatTimestamp(createTime) : "unknown";
      const rawContent = item.body?.content ?? "{}";

      let content;
      if (msgType === "merge_forward") {
        const nestedId = item.message_id;
        content = nestedId
          ? await formatSubTree(nestedId, childrenMap, resolveUserName)
          : "<forwarded_messages/>";
      } else {
        const subCtx = {
          ...buildConvertContextFromItem(item, parentId),
          resolveUserName,
        };
        content = (await convertMessageContent(rawContent, msgType, subCtx))
          .content;
      }

      const displayName = resolveUserName?.(senderId) ?? senderId;
      const indented = indentLines(content, "    ");
      parts.push(`[${timestamp}] ${displayName}:\n${indented}`);
    } catch {
      /* skip failed sub-messages */
    }
  }

  if (parts.length === 0) return "<forwarded_messages/>";
  return `<forwarded_messages>\n${parts.join("\n")}\n</forwarded_messages>`;
}

// ===========================================================================
// Dispatcher
// ===========================================================================

const converterMap = new Map([
  ["text", convertText],
  ["post", convertPost],
  ["image", convertImage],
  ["file", convertFile],
  ["audio", convertAudio],
  ["video", convertVideo],
  ["media", convertVideo],
  ["sticker", convertSticker],
  ["interactive", convertInteractive],
  ["share_chat", convertShareChat],
  ["share_user", convertShareUser],
  ["location", convertLocation],
  ["merge_forward", convertMergeForward],
  ["folder", convertFolder],
  ["system", convertSystem],
  ["hongbao", convertHongbao],
  ["share_calendar_event", convertShareCalendarEvent],
  ["calendar", convertCalendar],
  ["general_calendar", convertGeneralCalendar],
  ["video_chat", convertVideoChat],
  ["todo", convertTodo],
  ["vote", convertVote],
  ["unknown", convertUnknown],
]);

async function convertMessageContent(raw, messageType, ctx) {
  const fn = converterMap.get(messageType) ?? converterMap.get("unknown");
  const defaultCtx = { mentions: new Map(), mentionsByOpenId: new Map() };
  return fn(raw, ctx ?? defaultCtx);
}

// ===========================================================================
// User Name Resolution
// ===========================================================================

// 简单内存缓存：openId → name
const nameCache = new Map();

async function batchResolveUserNames(sdk, opts, openIds) {
  const missing = openIds.filter((id) => !nameCache.has(id));
  if (missing.length === 0) return;

  // Lark API 每次最多查 50 个
  for (let i = 0; i < missing.length; i += 50) {
    const batch = missing.slice(i, i + 50);
    try {
      const queryStr = batch
        .map((id) => `user_ids=${encodeURIComponent(id)}`)
        .join("&");
      const res = await sdk.request(
        {
          method: "GET",
          url: `/open-apis/contact/v3/users/batch?${queryStr}`,
          params: { user_id_type: "open_id" },
        },
        opts,
      );

      if (res.code === 0 && res.data?.items) {
        for (const user of res.data.items) {
          const openId = user.open_id;
          const name =
            user.name ||
            user.display_name ||
            user.nickname ||
            user.en_name ||
            "";
          if (openId) nameCache.set(openId, name);
        }
      }
    } catch {
      /* best-effort */
    }
    // 未解析成功的 ID 缓存空字符串，避免重复请求
    for (const id of batch) {
      if (!nameCache.has(id)) nameCache.set(id, "");
    }
  }
}

// ===========================================================================
// Message Formatting (Public API)
// ===========================================================================

/**
 * 格式化单条消息。
 *
 * 使用 convertMessageContent 将 body.content 转为 AI 可读文本，
 * 并过滤掉 AI 不需要的字段。
 */
async function formatMessageItem(item, nameResolver, ctxOverrides) {
  const messageId = item.message_id ?? "";
  const msgType = item.msg_type ?? "unknown";

  // 转换消息内容
  let content = "";
  try {
    const rawContent = item.body?.content ?? "";
    if (rawContent) {
      const ctx = {
        ...buildConvertContextFromItem(item, messageId),
        ...ctxOverrides,
      };
      const result = await convertMessageContent(rawContent, msgType, ctx);
      content = result.content;
    }
  } catch {
    content = item.body?.content ?? "";
  }

  // 构建 sender
  const senderId = item.sender?.id ?? "";
  const senderType = item.sender?.sender_type ?? "unknown";
  let senderName;
  if (senderId && senderType === "user") {
    senderName = nameResolver(senderId);
  }
  const sender = { id: senderId, sender_type: senderType };
  if (senderName) sender.name = senderName;

  // 构建 mentions（简化格式）
  let mentions;
  if (item.mentions && item.mentions.length > 0) {
    mentions = item.mentions.map((m) => ({
      key: m.key ?? "",
      id: extractMentionOpenId(m.id),
      name: m.name ?? "",
    }));
  }

  // 转换 create_time（毫秒时间戳字符串 → ISO 8601 +08:00）
  const createTime = item.create_time
    ? millisStringToDateTime(item.create_time)
    : "";

  const formatted = {
    message_id: messageId,
    msg_type: msgType,
    content,
    sender,
    create_time: createTime,
    deleted: item.deleted ?? false,
    updated: item.updated ?? false,
  };

  // 可选字段：thread_id / reply_to
  // 有 thread_id 时只展示 thread_id；无 thread_id 但有 parent_id 时展示为 reply_to
  if (item.thread_id) {
    formatted.thread_id = item.thread_id;
  } else if (item.parent_id) {
    formatted.reply_to = item.parent_id;
  }
  if (mentions) formatted.mentions = mentions;

  return formatted;
}

/**
 * 批量格式化消息列表。
 *
 * 先批量解析所有 sender 的名字，再逐条格式化。
 *
 * @param {Array} items - 飞书 IM API 返回的 message items
 * @param {object} sdk  - 代理 SDK（由 _cli.js 的 buildProxyClient 构建）
 * @param {object} opts - SDK 调用选项（包含 user token 标记）
 * @returns {Promise<Array>} 格式化后的消息列表
 */
export async function formatMessageList(items, sdk, opts) {
  const nameResolver = (openId) => nameCache.get(openId);

  // 1. 把 mention 自带的名字写入缓存（免费信息）
  for (const item of items) {
    for (const m of item.mentions ?? []) {
      const openId = extractMentionOpenId(m.id);
      if (openId && m.name) nameCache.set(openId, m.name);
    }
  }

  // 2. 收集所有 user 类型 sender 的 open_id
  const senderIds = [
    ...new Set(
      items
        .map((item) =>
          item.sender?.sender_type === "user" ? item.sender.id : undefined,
        )
        .filter(Boolean),
    ),
  ];

  // 3. 批量解析缓存中缺失的名字
  if (senderIds.length > 0) {
    const missing = senderIds.filter((id) => !nameCache.has(id));
    if (missing.length > 0) {
      await batchResolveUserNames(sdk, opts, missing);
    }
  }

  // 4. 构建 merge_forward 展开所需的回调
  const ctxOverrides = {
    resolveUserName: nameResolver,
    batchResolveNames: async (openIds) => {
      await batchResolveUserNames(sdk, opts, openIds);
    },
    fetchSubMessages: async (messageId) => {
      const res = await sdk.request(
        {
          method: "GET",
          url: `/open-apis/im/v1/messages/${messageId}`,
          params: {
            user_id_type: "open_id",
            card_msg_content_type: "raw_card_content",
          },
        },
        opts,
      );
      if (res.code !== 0) {
        throw new Error(`API error: code=${res.code} msg=${res.msg}`);
      }
      return res.data?.items ?? [];
    },
  };

  // 5. 逐条格式化
  return Promise.all(
    items.map((item) => formatMessageItem(item, nameResolver, ctxOverrides)),
  );
}
