"""
# `mcp:SlardarApp_autofix_get_slardar_issue_main_log`

根据用户提供的Slardar issue链接，获取这个issue的关键信息，崩溃线程调用栈、异常类型、崩溃原因、崩溃附带参数、关键栈帧git信息、预分析结果

---

**Parameters Schema:**

{"type":"object","properties":{"slardar_link":{"type":"string","description":"Slardar issue详情页链接","properties":{}}},"required":["slardar_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_autofix_get_slardar_issue_main_log", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)