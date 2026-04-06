"""
# `mcp:aeolus_aeolus_dashboard_and_sheet`

获取Dashboard与Sheet配置（dashboardAndSheet）,注意reportFilters为当前sheet页面下所有report的过滤器配置

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"dashboard_id":{"type":"integer","description":"必填，Dashboard ID","properties":{}},"sheet_id":{"type":"integer","description":"可选，Sheet ID","properties":{}}},"required":["base_url","dashboard_id","sheet_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_dashboard_and_sheet", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)