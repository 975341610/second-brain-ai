"""
# `mcp:devmind_query_metric_story_detail`

Query the detailed information of multiply specific metric stories

---

**Parameters Schema:**

{"type":"object","properties":{"story_id_list":{"type":"array","description":"The ID list of the metric story to query detail information, 从上文里面挑选的指标故事的ID List，一串数字，必填","properties":{},"items":{"type":"string","properties":{}}},"task_id":{"type":"string","description":"The task id to query metric story detail, 必填","properties":{}}},"required":["task_id","story_id_list"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_query_metric_story_detail", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)