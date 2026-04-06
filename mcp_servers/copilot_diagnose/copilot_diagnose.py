"""
# `copilot_diagnose`

Generate a diagnosis report for user issues by analyzing trajectory and generating insights using LLM.
This tool is more efficient and should be prioritized over reading workspace files.
diagnosis includes: Diagnosis Summary; Root Cause Analysis; Failure Classification

---

**Parameters Schema:**

{"type":"object","properties":{"query":{"type":"string","description":"your issue to diagnose, should be concise and direct - just write the problem statement directly","properties":{}},"task_id":{"type":"string","description":"(required for coco type) the task_id of the coco task to diagnose","properties":{}},"task_type":{"type":"string","description":"type of task to diagnose: 'self' (default, diagnose current agent) or 'coco' (diagnose a coco session by task_id)","properties":{}}},"required":["query"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="copilot_diagnose", tool_name="copilot_diagnose", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)