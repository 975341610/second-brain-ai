"""
# `mcp:byted_fe_knowledge_get_ui_lib_list_knowledge`

获取指定组件库的简要信息和组件列表

---

**Parameters Schema:**

{"type":"object","properties":{"libName":{"type":"string","description":"组件库名称，如 @tod-m/materials，不提供则获取所有支持的组件库列表","properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="byted_fe_knowledge", tool_name="mcp:byted_fe_knowledge_get_ui_lib_list_knowledge", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)