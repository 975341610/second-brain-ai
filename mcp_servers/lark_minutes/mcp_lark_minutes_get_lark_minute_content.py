"""
# `mcp:lark_minutes_get_lark_minute_content`

获取飞书妙记（Lark Minutes）的内容，包括基础信息、AI 总结、章节摘要、待办事项，以及会议纪要文档链接。输入 minute_token 或 meeting_id 之一即可。minute_token 可从妙记链接中提取，例如：https://bytedance.larkoffice.com/minutes/obcnoz63eily28go3baa82ru 中的 obcnoz63eily28go3baa82ru。

---

**Parameters Schema:**

{"type":"object","properties":{"meeting_id":{"type":"string","description":"视频会议 ID，与 minute_token 二选一。","properties":{}},"minute_token":{"type":"string","description":"妙记 token，与 meeting_id 二选一。可从妙记 URL 末段提取。","properties":{}}},"required":["minute_token","meeting_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_minutes", tool_name="mcp:lark_minutes_get_lark_minute_content", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)