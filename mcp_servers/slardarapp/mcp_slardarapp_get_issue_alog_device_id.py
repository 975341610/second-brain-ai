"""
# `mcp:SlardarApp_get_issue_alog_device_id`

根据 Slardar issue 链接获取 n 个包含 alog 的 DeviceID 及其对应的 issue 发生时间

---

**Parameters Schema:**

{"type":"object","properties":{"id_count":{"type":"integer","description":"需要获取的 id 最大数量","properties":{}},"issue_link":{"type":"string","description":"Slardar issue 链接","properties":{}}},"required":["issue_link","id_count"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_issue_alog_device_id", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)