"""
# `mcp:SlardarApp_get_issue_alog_content`

根据 Slardar issue 链接获取 n 台设备的 alog 日志，并指定日志时间范围

---

**Parameters Schema:**

{"type":"object","properties":{"after_time":{"type":"integer","description":"问题发生后 n 秒的日志","properties":{}},"before_time":{"type":"integer","description":"问题发生前 n 秒的日志","properties":{}},"id_count":{"type":"integer","description":"需要获取的最大设备数量","properties":{}},"issue_link":{"type":"string","description":"Slardar issue 链接","properties":{}}},"required":["issue_link","id_count"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_issue_alog_content", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)