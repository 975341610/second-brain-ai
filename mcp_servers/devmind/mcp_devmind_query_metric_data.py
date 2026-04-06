"""
# `mcp:devmind_query_metric_data`

Query data for a specific metric

---

**Parameters Schema:**

{"type":"object","properties":{"node_id":{"type":"string","description":"ID of the node to query data for. The node ID can be obtained from the results of the ToolQueryBusinessNodes or ToolQueryReportNodes tools. Leave empty to query metrics related to the current user.","properties":{}},"query_date":{"type":"string","description":"Date to query in YYYY-MM-DD format","properties":{}},"story_id":{"type":"string","description":"The ID of the story metric to query","properties":{}},"time_granularity":{"type":"string","description":"Time granularity for the query. Valid values include: 日、周、双周、月、双月、季度、半年、年、半年绩效周期、全年绩效周期","properties":{}}},"required":["story_id","time_granularity","query_date","node_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_query_metric_data", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)