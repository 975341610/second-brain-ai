"""
# `mcp:aeolus_aeolus_get_my_authorized_resources`

获取用户在 Aeolus 平台上有授权的资源列表（分页获取），这是作为缺少上下文的冷启动的首选工具

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"limit":{"type":"integer","description":"分页大小limit，默认20","properties":{}},"offset":{"type":"integer","description":"分页起始offset，默认0","properties":{}}},"required":["base_url","offset","limit"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_get_my_authorized_resources", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)