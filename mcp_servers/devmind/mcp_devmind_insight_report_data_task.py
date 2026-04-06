"""
# `mcp:devmind_insight_report_data_task`

Query task info for a specific insight report, including user's customized prompt and data info about how to analyze this task

---

**Parameters Schema:**

{"type":"object","properties":{"execute_id":{"type":"string","description":"The ID of task to execute","properties":{}}},"required":["execute_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_insight_report_data_task", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)