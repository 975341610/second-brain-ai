"""
# `mcp:lark_lark_get_avatar`

get current user's Lark avatar url and download locally

---

**Parameters Schema:**

{"type":"object","properties":{}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_lark_get_avatar", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)