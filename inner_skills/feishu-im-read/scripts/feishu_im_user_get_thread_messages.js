import { runCli, assertOk } from "./internal/_cli.js";
import { formatMessageList } from "./internal/_format.js";

function sortRuleToSortType(rule) {
  return rule === "create_time_asc" ? "ByCreateTimeAsc" : "ByCreateTimeDesc";
}

await runCli(async ({ sdk, opts, input }) => {
  sdk.authReason = "获取话题回复消息";
  const p = input ?? {};
  if (!p.thread_id) throw new Error("missing thread_id");

  const res = await sdk.im.v1.message.list(
    {
      params: {
        container_id_type: "thread",
        container_id: p.thread_id,
        sort_type: sortRuleToSortType(p.sort_rule),
        page_size: p.page_size ?? 50,
        page_token: p.page_token,
        card_msg_content_type: "raw_card_content",
      },
    },
    opts,
  );
  assertOk(res);

  const items = res.data?.items ?? [];
  const messages = await formatMessageList(items, sdk, opts);
  return {
    messages,
    has_more: res.data?.has_more ?? false,
    page_token: res.data?.page_token,
  };
});

