"""
# `mcp:SlardarApp_get_thread_backtrace_aggregate`

获取Slardar某个issue下指定线程调用栈的堆栈聚合数据

---

**Parameters Schema:**

{"type":"object","properties":{"aggr_event_limit":{"type":"integer","description":"采样event数量，默认10，最大100","properties":{}},"link":{"type":"string","description":"Slardar issue链接","properties":{}},"thread_name":{"type":"string","description":"线程名","properties":{}}},"required":["link","thread_name"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_thread_backtrace_aggregate", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)