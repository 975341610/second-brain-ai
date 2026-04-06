"""
# `mcp:byted_fe_knowledge_get_icon_lib_knowledge`

字节前端图标库相关知识检索

---

**Parameters Schema:**

{"type":"object","properties":{"query":{"type":"string","description":"用户提问的内容","properties":{}}},"required":["query"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="byted_fe_knowledge", tool_name="mcp:byted_fe_knowledge_get_icon_lib_knowledge", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)