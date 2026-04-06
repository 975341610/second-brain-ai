"""
# `mcp:SlardarApp_autofix_retrace_stack`

这是一个Slardar的MCP Tool，用来对特定的堆栈进行retrace。
使用场景：用户提供原始堆栈，希望能获取堆栈对应的具体符号、文件、行号等信息时，调用此工具，传入对应的参数。（目前os只支持Android，retrace类型只支持native堆栈）
参数包括：
1. slardar_link：一个Slardar链接，工具需要从此链接中解析出来必要的信息。如果传了这个参数，必须是stack参数对应的slardar链接；如果没有链接，请传必要的aid、os、crash_libs参数！
2. retrace_type：待retrace的堆栈类型（目前支持：native和java）
3. stack：需要retrace的堆栈，必须有该参数
4. crash_libs：非必须，但是如果没有Slardar_link就必须传，类型：[]interface{lib_name string, lib_uuid string}

---

**Parameters Schema:**

{"type":"object","properties":{"aid":{"type":"integer","description":"app标识","properties":{}},"crash_libs":{"type":"array","description":"非必须，但是如果没有Slardar_link就必须传，类型：[]interface{lib_name string, lib_uuid string}","properties":{},"items":{"type":"object","properties":{"lib_name":{"type":"string","properties":{}},"lib_uuid":{"type":"string","properties":{}}},"additionalProperties":false,"required":["lib_name","lib_uuid"]}},"os":{"type":"string","description":"系统类型","properties":{}},"retrace_type":{"type":"string","description":"待retrace的堆栈类型（目前支持：native和java）","properties":{}},"slardar_link":{"type":"string","description":"一个Slardar链接，工具需要从此链接中解析出来必要的信息。","properties":{}},"stack":{"type":"string","description":"需要retrace的堆栈，必须有该参数","properties":{}}},"required":["retrace_type","stack","os"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_autofix_retrace_stack", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)