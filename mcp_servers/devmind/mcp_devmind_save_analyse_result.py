"""
# `mcp:devmind_save_analyse_result`

Save the analyse result.

---

**Parameters Schema:**

{"type":"object","properties":{"chart_analyse_result":{"type":"string","description":"The chart analyse result to save","properties":{}},"task_id":{"type":"string","description":"The task id to save chart analyse result, 必填","properties":{}},"title":{"type":"string","description":"The title of the chart analyse result, 本次分析结论任务的标题，十个字左右","properties":{}}},"required":["task_id","title","chart_analyse_result"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_save_analyse_result", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)