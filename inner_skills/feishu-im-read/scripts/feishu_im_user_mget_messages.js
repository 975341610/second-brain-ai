import { runCli, assertOk } from "./internal/_cli.js";
import { formatMessageList } from "./internal/_format.js";

const MAX_MESSAGE_IDS = 50;

async function mgetMessages(sdk, opts, messageIds) {
  const queryStr = messageIds
    .map((id) => `message_ids=${encodeURIComponent(id)}`)
    .join("&");
  const res = await sdk.request(
    {
      method: "GET",
      url: `/open-apis/im/v1/messages/mget?${queryStr}`,
      params: { user_id_type: "open_id", card_msg_content_type: "raw_card_content" },
    },
    opts,
  );
  assertOk(res);
  return res.data?.items ?? [];
}

await runCli(async ({ sdk, opts, input }) => {
  sdk.authReason = "批量获取消息详情";
  const p = input ?? {};

  let ids = p.message_ids;
  if (!ids || !Array.isArray(ids) || ids.length === 0) {
    if (typeof ids === "string") {
      ids = ids.split(",").map((s) => s.trim()).filter(Boolean);
    }
    if (!ids || ids.length === 0) {
      throw new Error("message_ids 是必填参数，需要提供至少一个消息 ID（om_xxx 格式）");
    }
  }

  if (ids.length > MAX_MESSAGE_IDS) {
    throw new Error(`message_ids 最多支持 ${MAX_MESSAGE_IDS} 个，当前提供了 ${ids.length} 个`);
  }

  for (const id of ids) {
    if (!/^om_/.test(id)) {
      throw new Error(`无效的消息 ID: ${id}，消息 ID 必须以 om_ 开头`);
    }
  }

  const items = await mgetMessages(sdk, opts, ids);
  const messages = await formatMessageList(items, sdk, opts);

  return {
    messages,
    total: messages.length,
  };
});
