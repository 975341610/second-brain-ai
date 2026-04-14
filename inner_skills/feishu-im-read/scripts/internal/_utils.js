export function buildAuthCard(params) {
  const { verificationUriComplete, expiresMin, scope, reason } = params;
  const inAppUrl = toInAppWebUrl(verificationUriComplete);
  const multiUrl = {
    url: inAppUrl,
    pc_url: inAppUrl,
    android_url: inAppUrl,
    ios_url: inAppUrl,
  };

  const scopeDesc = formatScopeDescription(scope);
  
  const elements = [
    // 授权说明
    {
      tag: "markdown",
      content: scopeDesc,
      text_size: "normal",
    },
    // 申请理由
    ...(reason ? [{
        tag: "markdown",
        content: `**申请理由**：${reason}`,
        text_size: "normal",
    }] : []),
    // 授权按钮（small，靠右）
    {
      tag: "column_set",
      flex_mode: "none",
      horizontal_align: "right",
      columns: [
        {
          tag: "column",
          width: "auto",
          elements: [
            {
              tag: "button",
              text: { tag: "plain_text", content: "前往授权" },
              type: "primary",
              size: "medium",
              multi_url: multiUrl,
            },
          ],
        },
      ],
    },
    // 失效时间提醒
    {
      tag: "markdown",
      content: `<font color='grey'>授权链接将在 ${expiresMin} 分钟后失效，届时需重新发起</font>`,
      text_size: "notation",
    },
  ];

  return {
    schema: "2.0",
    config: {
      wide_screen_mode: false,
      style: {
        color: {
          "light-yellow-bg": {
            light_mode: "rgba(255, 214, 102, 0.12)",
            dark_mode: "rgba(255, 214, 102, 0.08)",
          },
        },
      },
    },
    header: {
      title: {
        tag: "plain_text",
        content: "需要您的授权才能继续"
      },
      template: "blue",
      padding: "12px 12px 12px 12px",
      icon: {
        tag: "standard_icon",
        token: "lock-chat_filled"
      },
    },
    body: { elements },
  };
}

export function buildAuthSuccessCard() {
  return {
    schema: "2.0",
    config: { wide_screen_mode: false },
    header: {
      title: { tag: "plain_text", content: "授权成功" },
      template: "green",
      padding: "12px 12px 12px 12px",
      icon: { tag: "standard_icon", token: "yes_filled" },
    },
    body: {
      elements: [
        {
          tag: "markdown",
          content: "您的飞书账号已成功授权，正在为您继续执行操作。\n\n<font color='grey'>如需撤销授权，可随时告诉我。</font>",
        },
      ],
    },
  };
}

export function buildAuthFailedCard(message, scope, appReason) {
  const elements = [
    {
      tag: "markdown",
      content: message || "授权链接已过期，请重新发起授权。",
    },
  ];

  if (scope) {
    const scopes = scope.split(/\s+/).filter(Boolean);
    if (scopes.length > 0) {
      elements.push({
        tag: "markdown",
        content: "**所需权限**：\n" + scopes.map((s) => `- ${s}`).join("\n"),
        text_size: "normal",
      });
    }
  }

  if (appReason) {
    elements.push({
      tag: "markdown",
      content: `**申请理由**：${appReason}`,
      text_size: "normal",
    });
  }

  return {
    schema: "2.0",
    config: { wide_screen_mode: false },
    header: {
      title: { tag: "plain_text", content: "授权未完成" },
      template: "yellow",
      padding: "12px 12px 12px 12px",
      icon: { tag: "standard_icon", token: "warning_filled" },
    },
    body: {
      elements: elements,
    },
  };
}

function formatScopeDescription(scope) {
  const scopes = scope?.split(/\s+/).filter(Boolean);
  const desc = "授权后，应用将能够以您的身份执行相关操作。";
  if (!scopes?.length) return desc;
  return desc + "\n\n**所需权限**：\n" + scopes.map((s) => `- ${s}`).join("\n");
}

function toInAppWebUrl(targetUrl) {
  const encoded = encodeURIComponent(targetUrl);
  const lkMeta = encodeURIComponent(JSON.stringify({
    "page-meta": {
      showNavBar: "false",
      showBottomNavBar: "false",
    },
  }));
  return ("https://applink.feishu.cn/client/web_url/open" +
    `?mode=sidebar-semi&max_width=800&reload=false&url=${encoded}&lk_meta=${lkMeta}`);
}
