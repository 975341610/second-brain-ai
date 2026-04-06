"""
# `mcp:tea_tea_list_apps`

列出当前用户有权限访问的Tea/DataFinder APP(项目)列表

---

**Parameters Schema:**

{"type":"object","properties":{}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="tea", tool_name="mcp:tea_tea_list_apps", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)