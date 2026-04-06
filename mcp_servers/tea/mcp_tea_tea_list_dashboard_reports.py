"""
# `mcp:tea_tea_list_dashboard_reports`

获取指定 dashboard 下所有 reports 列表

---

**Parameters Schema:**

{"type":"object","properties":{"dashboard_id":{"type":"string","description":"必填，Dashboard ID","properties":{}},"project_id":{"type":"string","description":"必填，DataFinder Project ID","properties":{}},"with_dashboard_operation":{"type":"boolean","description":"可选，是否返回 dashboard operation 信息，默认 true","properties":{}}},"required":["project_id","dashboard_id","with_dashboard_operation"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="tea", tool_name="mcp:tea_tea_list_dashboard_reports", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)