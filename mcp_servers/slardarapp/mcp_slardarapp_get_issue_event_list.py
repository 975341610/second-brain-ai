"""
# `mcp:SlardarApp_get_issue_event_list`

根据用户提供的Slardar issue链接，获取异常issue下的一个event详情，查询某段时间范围内，某个event日志详情，其中包含异常调用栈、异常原因、设备环境信息、CommitID等信息。

---

**Parameters Schema:**

{"type":"object","properties":{"slardar_link":{"type":"string","description":"Slardar issue链接, 以https://slardar.bytedance.net/或者https://t.wtturl.cn开始的完整URL","properties":{},"format":"uri"}},"required":["slardar_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_issue_event_list", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)