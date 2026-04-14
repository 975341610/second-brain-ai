import { runCli, assertOk, DEFAULT_P2P_LANE_ID } from "./internal/_cli.js";
import { dateTimeToSecondsString, parseTimeRangeToSeconds } from "./internal/_time.js";
import { formatMessageList } from "./internal/_format.js";

function resolveTimeRange(p) {
  if (p.relative_time) {
    return parseTimeRangeToSeconds(p.relative_time);
  }
  return {
    start: p.start_time ? dateTimeToSecondsString(p.start_time) : undefined,
    end: p.end_time ? dateTimeToSecondsString(p.end_time) : undefined,
  };
}

function buildSearchData(p, time) {
  const data = {
    query: p.query ?? "",
    start_time: time.start,
    end_time: time.end,
  };
  if (Array.isArray(p.sender_ids) && p.sender_ids.length > 0) data.from_ids = p.sender_ids;
  if (p.chat_id) data.chat_ids = [p.chat_id];
  if (Array.isArray(p.mention_ids) && p.mention_ids.length > 0)
    data.at_chatter_ids = p.mention_ids;
  if (p.message_type) data.message_type = p.message_type;
  if (p.sender_type && p.sender_type !== "all") data.from_type = p.sender_type;
  if (p.chat_type) data.chat_type = p.chat_type === "group" ? "group_chat" : "p2p_chat";
  return data;
}

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
    sdk.authReason = "跨会话搜索消息记录";
    const p = input ?? {};
    const laneId = process.env.IRIS_LANE_ID;

    // 公开环境隐私限制（laneId 为 default_p2p_lane_id 时是私聊场景，不限制）
    if (laneId && laneId !== DEFAULT_P2P_LANE_ID) {
      if (p.chat_type === "p2p") {
        throw new Error("当前处于群聊环境中，无法搜索私聊消息。仅允许搜索当前群聊的消息。");
      }
      if (p.chat_id && p.chat_id !== laneId) {
        throw new Error("当前处于群聊环境中，仅允许搜索当前群聊的消息，不可搜索其他会话。");
      }
      // 限定到当前群聊
      p.chat_id = laneId;
      p.chat_type = "group";
    }

    // 至少需要一个过滤条件
    if (p.relative_time && (p.start_time || p.end_time)) {
    throw new Error("relative_time 和 start_time/end_time 不能同时使用");
  }

  const hasAnyFilter =
    p.query !== undefined ||
    (Array.isArray(p.sender_ids) && p.sender_ids.length > 0) ||
    !!p.chat_id ||
    (Array.isArray(p.mention_ids) && p.mention_ids.length > 0) ||
    !!p.message_type ||
    !!p.sender_type ||
    !!p.chat_type ||
    !!p.relative_time ||
    !!p.start_time ||
    !!p.end_time;
  if (!hasAnyFilter) {
    throw new Error("至少需要提供一个过滤条件");
  }

  const time = resolveTimeRange(p);
  const start = time.start ?? "978307200";
  const end = time.end ?? Math.floor(Date.now() / 1000).toString();
  const data = buildSearchData(p, { start, end });

  const searchRes = await sdk.search.message.create(
    {
      data,
      params: {
        user_id_type: "open_id",
        page_size: p.page_size ?? 50,
        page_token: p.page_token,
      },
    },
    opts,
  );
  assertOk(searchRes);
  const ids = searchRes.data?.items ?? [];
  const hasMore = searchRes.data?.has_more ?? false;
  const pageToken = searchRes.data?.page_token;

  if (ids.length === 0) {
    return { messages: [], has_more: hasMore, page_token: pageToken };
  }

  const items = await mgetMessages(sdk, opts, ids);
  const messages = await formatMessageList(items, sdk, opts);
  const result = { messages, has_more: hasMore, page_token: pageToken };
  if (laneId) {
    result.notice = "当前处于公开环境，搜索范围已自动限定为当前群聊。";
  }
  return result;
});

