"""
# `mcp:devmind_insight_report_get_task_and_metric_info`

Get the task_instance_id, user_prompt, and the list of metric_infos required for this task. You MUST use these fields to construct the GetTaskDataReq for the next tool: insight_report_get_task_data.

---

**Parameters Schema:**

{"type":"object","properties":{"execute_id":{"type":"string","description":"The ID of task to execute","properties":{}}},"required":["execute_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_insight_report_get_task_and_metric_info", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)