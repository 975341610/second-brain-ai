"""
# `mcp:tea_tea_list_dashboards`

获取指定 DataFinder Project 下的看板目录树（递归展开所有层级的目录和看板）

---

**Parameters Schema:**

{"type":"object","properties":{"project_id":{"type":"string","description":"必填，DataFinder Project ID","properties":{}}},"required":["project_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="tea", tool_name="mcp:tea_tea_list_dashboards", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)