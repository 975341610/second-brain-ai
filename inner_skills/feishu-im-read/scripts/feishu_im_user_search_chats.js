import { runCli, assertOk } from "./internal/_cli.js";

await runCli(async ({ sdk, opts, input }) => {
  sdk.authReason = "按名称搜索群聊获取 chat_id";
  const p = input ?? {};

  if (!p.query) {
    throw new Error("必须提供 query 参数（群聊名称关键词）");
  }

  const res = await sdk.im.v1.chat.search(
    {
      params: {
        query: p.query,
        user_id_type: "open_id",
        page_size: p.page_size ?? 100,
        page_token: p.page_token,
      },
    },
    opts,
  );
  assertOk(res);

  const items = (res.data?.items ?? []).map((chat) => ({
    chat_id: chat.chat_id,
    name: chat.name,
    avatar: chat.avatar,
    description: chat.description,
    chat_status: chat.chat_status,
    external: chat.external,
    tenant_key: chat.tenant_key,
  }));

  // 多个结果时，精确匹配群名的排在最前面
  const exact = items.filter((c) => c.name === p.query);
  const rest = items.filter((c) => c.name !== p.query);
  const sorted = [...exact, ...rest];

  return {
    chats: sorted,
    exact_match: exact.length > 0 ? exact[0] : null,
    has_more: res.data?.has_more ?? false,
    page_token: res.data?.page_token,
  };
});
