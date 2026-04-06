"""
# `mcp:SlardarApp_autofix_get_slardar_issue_thread_backtraces`

根据用户提供的Slardar issue链接，分页查询slardar issue下某个event中所有线程的详细信息，包括线程名、调用栈、CPU使用率等，支持搜索。可以获取retrace后的堆栈，Android的search_token不用传

---

**Parameters Schema:**

{"type":"object","properties":{"link":{"type":"string","description":"Slardar issue详情页链接","properties":{}},"page_no":{"type":"integer","description":"页号，从0开始","properties":{}},"page_size":{"type":"integer","description":"页大小，最大值5","properties":{}},"search_token":{"type":"string","description":"搜索的key，支持简单字符串和正则表达式","properties":{}}},"required":["link","page_no","page_size"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_autofix_get_slardar_issue_thread_backtraces", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)