"""
# `mcp:devmind_insight_report_get_task_data`

Fetch task data for the given task_instance_id. The request body MUST be a valid GetTaskDataReq built from the previous step (task_instance_id + metric_params[]). Each metric_params item must specify metric_id, dim_query_list, and detail_data according to the user_prompt and metric_infos.

---

**Parameters Schema:**

{"type":"object","properties":{"metric_params":{"type":"array","description":"metric params","properties":{},"items":{"type":"object","properties":{"detail_data":{"type":"boolean","description":"detail data","properties":{}},"dim_query_list":{"type":"array","description":"dim query list","properties":{},"items":{"type":"string","properties":{}}},"metric_id":{"type":"string","description":"metric id","properties":{}}},"required":["metric_id","dim_query_list","detail_data"]}},"task_instance_id":{"type":"string","description":"task instance id","properties":{}}},"required":["task_instance_id","metric_params"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_insight_report_get_task_data", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)