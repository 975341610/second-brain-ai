"""
# `mcp:lark_lark_user_info`

get Lark user info by emails, or get all members info of a chat group by chat_id

---

**Parameters Schema:**

{"type":"object","properties":{"chat_id":{"type":"string","description":"optional, chat id, e.g oc_1234567890. either emails or chat_id is required","properties":{}},"emails":{"type":"array","description":"optional, email array, e.g ['zhangsan.001@bytedance.com']. either emails or chat_id is required","properties":{},"items":{"type":"string","properties":{}}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_lark_user_info", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)