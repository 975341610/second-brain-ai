"""
# `mcp:aeolus_aeolus_list_apps`

列出用户有权限的Aeolus APP列表

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}}},"required":["base_url"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_list_apps", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)