"""
# `mcp:byted_fe_knowledge_get_ui_lib_knowledge`

获取指定组件库的指定组件的详细使用说明和示例代码

---

**Parameters Schema:**

{"type":"object","properties":{"component":{"type":"string","description":"组件名称，如 XOncall","properties":{}},"library":{"type":"string","description":"组件库名称，如 @tod-m/materials","properties":{}}},"required":["library","component"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="byted_fe_knowledge", tool_name="mcp:byted_fe_knowledge_get_ui_lib_knowledge", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)