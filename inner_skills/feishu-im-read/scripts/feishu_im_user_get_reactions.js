import { runCli, assertOk } from "./internal/_cli.js";

await runCli(async ({ sdk, opts, input }) => {
  sdk.authReason = "获取消息表情回复";
  const p = input ?? {};

  if (!p.message_id) {
    throw new Error("message_id 是必填参数（格式：om_xxx）");
  }
  if (!/^om_/.test(p.message_id)) {
    throw new Error("message_id 格式不正确，应以 om_ 开头");
  }

  const query = {
    user_id_type: "open_id",
  };
  if (p.reaction_type) {
    query.reaction_type = p.reaction_type;
  }
  if (p.page_size) {
    query.page_size = Math.min(Math.max(1, Number(p.page_size)), 50);
  }
  if (p.page_token) {
    query.page_token = p.page_token;
  }

  const res = await sdk.im.v1.messageReaction.list(
    {
      path: { message_id: p.message_id },
      params: query,
    },
    opts,
  );
  assertOk(res);

  const items = (res.data?.items ?? []).map((item) => ({
    reaction_id: item.reaction_id,
    emoji_type: item.reaction_type?.emoji_type,
    operator_id: item.operator?.operator_id,
    operator_type: item.operator?.operator_type,
    action_time: item.action_time,
  }));

  return {
    reactions: items,
    total: items.length,
    has_more: res.data?.has_more ?? false,
    page_token: res.data?.page_token ?? null,
  };
});
