"""
# `mcp:SlardarOS_get_os_issue_event_list`

根据用户提供的SlardarOS issue链接，获取异常issue下的一个event详情，查询某段时间范围内，某个event日志详情，其中包含异常调用栈、异常原因、设备环境、系统属性等

---

**Parameters Schema:**

{"type":"object","properties":{"slardar_os_link":{"type":"string","description":"SlardarOS issue链接，以 https://slardar.bytedance.net/node/os_detail开头,或者以 https://t.wtturl.cn/开头的短链接","properties":{},"format":"uri"}},"required":["slardar_os_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarOS", tool_name="mcp:SlardarOS_get_os_issue_event_list", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)