"""
# `copilot_gpt`

Provide informal, direct answers to user questions by analyzing trajectory.
Give concise, straightforward responses without formal diagnosis. Examples:
- For template document verification: Simply answer "Yes" or "No"  
- For calculation explanations: Answer directly based on trajectory
- For calculation errors: Just inform "calculation error detected" without formal diagnosis

---

**Parameters Schema:**

{"type":"object","properties":{"query":{"type":"string","description":"your question or issue to get a direct answer from LLM","properties":{}}},"required":["query"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="copilot_diagnose", tool_name="copilot_gpt", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)