"""
# `mcp:devmind_insight_report_data`

Query data for a specific insight report, including metric data

---

**Parameters Schema:**

{"type":"object","properties":{"query_date":{"type":"string","description":"Date to query in YYYY-MM-DD format","properties":{}},"report_id":{"type":"string","description":"The ID of the insight report to query","properties":{}},"time_granularity":{"type":"string","description":"Time granularity for the query. Valid values include: 日、周、双周、月、双月、季度、半年、年、半年绩效周期、全年绩效周期","properties":{}}},"required":["report_id","time_granularity","query_date"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_insight_report_data", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)