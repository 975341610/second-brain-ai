"""
# `mcp:SlardarApp_get_oom_crash_releated_matrix_issue_trend`

根据用户提供的slardar issue链接和时间戳，获取某个oom crash issue在一个时间段内关联到的matrix的issue信息及其上报趋势

---

**Parameters Schema:**

{"type":"object","properties":{"end_timestamp":{"type":"integer","description":"结束时间戳","properties":{}},"issue_link":{"type":"string","description":"Slardar issue链接, 以https://slardar.bytedance.net/或者https://t.wtturl.cn开始的完整URL","properties":{}},"start_timestamp":{"type":"integer","description":"开始时间戳","properties":{}}},"required":["issue_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_oom_crash_releated_matrix_issue_trend", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)