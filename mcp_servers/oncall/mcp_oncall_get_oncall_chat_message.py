"""
# `mcp:oncall_get_oncall_chat_message`

根据oncall ID查询群聊

---

**Parameters Schema:**

{"type":"object","properties":{"id":{"type":"string","description":"oncall id，此处填写oncall id","properties":{}}},"required":["id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="oncall", tool_name="mcp:oncall_get_oncall_chat_message", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)