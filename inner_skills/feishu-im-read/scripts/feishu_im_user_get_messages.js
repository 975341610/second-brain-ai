import { runCli, assertOk, DEFAULT_P2P_LANE_ID } from "./internal/_cli.js";
import { dateTimeToSecondsString, parseTimeRangeToSeconds } from "./internal/_time.js";
import { formatMessageList } from "./internal/_format.js";

function sortRuleToSortType(rule) {
  return rule === "create_time_asc" ? "ByCreateTimeAsc" : "ByCreateTimeDesc";
}

function resolveTimeRange(p) {
  if (p.relative_time) {
    return parseTimeRangeToSeconds(p.relative_time);
  }
  return {
    start: p.start_time ? dateTimeToSecondsString(p.start_time) : undefined,
    end: p.end_time ? dateTimeToSecondsString(p.end_time) : undefined,
  };
}

async function resolveP2PChatId(sdk, opts, openId) {
  const res = await sdk.im.v1.chat_p2p.batch_query(
    {
      data: { chatter_ids: [openId] },
      params: { user_id_type: "open_id" },
    },
    opts,
  );
  assertOk(res);
  const chats = res.data?.p2p_chats ?? [];
  if (chats.length === 0) {
    throw new Error(`未找到与 open_id=${openId} 的单聊会话。可能没有单聊记录。`);
  }
  return chats[0].chat_id;
}

await runCli(async ({ sdk, opts, input }) => {
  sdk.authReason = "获取单聊或群聊历史消息";
  const p = input ?? {};
  const laneId = process.env.IRIS_LANE_ID;

  // 公开环境隐私限制（laneId 为 default_p2p_lane_id 时是私聊场景，不限制）
  if (laneId && laneId !== DEFAULT_P2P_LANE_ID) {
    if (p.open_id) {
      throw new Error("当前处于群聊环境中，无法获取私聊消息记录。仅允许获取当前群聊的消息。");
    }
    if (p.chat_id && p.chat_id !== laneId) {
      throw new Error("当前处于群聊环境中，仅允许获取当前群聊的消息记录，不可访问其他会话。");
    }
    // 未指定 chat_id 时默认使用当前群聊
    if (!p.chat_id) {
      p.chat_id = laneId;
    }
  }

  if (p.open_id && p.chat_id) {
    throw new Error("open_id 和 chat_id 不能同时提供，请只传其中一个");
  }
  if (!p.open_id && !p.chat_id) {
    throw new Error("open_id 和 chat_id 必须提供其中一个");
  }
  if (p.relative_time && (p.start_time || p.end_time)) {
    throw new Error("relative_time 和 start_time/end_time 不能同时使用");
  }

  let chatId = p.chat_id;
  if (p.open_id) {
    chatId = await resolveP2PChatId(sdk, opts, p.open_id);
  }

  const time = resolveTimeRange(p);
  const res = await sdk.im.v1.message.list(
    {
      params: {
        container_id_type: "chat",
        container_id: chatId,
        start_time: time.start,
        end_time: time.end,
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
  const hasMore = res.data?.has_more ?? false;
  const pageToken = res.data?.page_token;
  return { messages, has_more: hasMore, page_token: pageToken };
});