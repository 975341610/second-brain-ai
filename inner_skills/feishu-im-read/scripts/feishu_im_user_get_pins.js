import { runCli, assertOk } from "./internal/_cli.js";
import { formatMessageList } from "./internal/_format.js";

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
  sdk.authReason = "获取置顶消息列表";
  const p = input ?? {};

  if (!p.chat_id) {
    throw new Error("chat_id 是必填参数（格式：oc_xxx）");
  }
  if (!/^oc_/.test(p.chat_id)) {
    throw new Error("chat_id 格式不正确，应以 oc_ 开头");
  }

  const query = {
    chat_id: p.chat_id,
  };
  if (p.page_size) {
    query.page_size = Math.min(Math.max(1, Number(p.page_size)), 50);
  }
  if (p.page_token) {
    query.page_token = p.page_token;
  }

  const res = await sdk.im.v1.pin.list(
    {
      params: query,
    },
    opts,
  );
  assertOk(res);

  const items = res.data?.items ?? [];
  const hasMore = res.data?.has_more ?? false;
  const pageToken = res.data?.page_token ?? null;

  if (items.length === 0) {
    return { pins: [], total: 0, has_more: hasMore, page_token: pageToken };
  }

  const messageIds = items.map((item) => item.message_id).filter(Boolean);
  const rawMessages = messageIds.length > 0 ? await mgetMessages(sdk, opts, messageIds) : [];
  const messages = await formatMessageList(rawMessages, sdk, opts);

  const msgMap = new Map();
  for (const msg of messages) {
    if (msg.message_id) msgMap.set(msg.message_id, msg);
  }

  const pins = items.map((item) => ({
    message_id: item.message_id,
    operator_id: item.operator_id,
    create_time: item.create_time,
    message: msgMap.get(item.message_id) ?? null,
  }));

  return { pins, total: pins.length, has_more: hasMore, page_token: pageToken };
});
