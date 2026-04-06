"""
# `mcp:SlardarOS_autofix_get_slardar_os_issue_main_log`

根据用户提供的Slardar OS issue链接，获取这个issue的关键信息，崩溃线程调用栈、异常类型、崩溃原因、崩溃附带参数、关键栈帧git信息、预分析结果

---

**Parameters Schema:**

{"type":"object","properties":{"slardar_os_link":{"type":"string","description":"SlardarOS issue链接，以 https://slardar.bytedance.net/node/os_detail开头,或者以 https://t.wtturl.cn/开头的短链接","properties":{}}},"required":["slardar_os_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarOS", tool_name="mcp:SlardarOS_autofix_get_slardar_os_issue_main_log", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)