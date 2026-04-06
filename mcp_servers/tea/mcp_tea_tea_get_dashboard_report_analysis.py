"""
# `mcp:tea_tea_get_dashboard_report_analysis`

获取指定 dashboard report 的 analysis 结果

---

**Parameters Schema:**

{"type":"object","properties":{"dashboard_id":{"type":"string","description":"必填，Dashboard ID","properties":{}},"end_time":{"type":"string","description":"可选，查询结束时间，ISO 8601 格式（含时区），如 '2025-02-01T23:59:59+08:00'，不填则由服务端决定默认区间","properties":{}},"project_id":{"type":"string","description":"必填，DataFinder Project ID","properties":{}},"report_id":{"type":"string","description":"必填，Report ID","properties":{}},"start_time":{"type":"string","description":"可选，查询开始时间，ISO 8601 格式（含时区），如 '2025-01-31T00:00:00+08:00'，不填则由服务端决定默认区间","properties":{}}},"required":["project_id","dashboard_id","report_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="tea", tool_name="mcp:tea_tea_get_dashboard_report_analysis", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)