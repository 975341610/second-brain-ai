"""
# `mcp:tea_tea_analyze_by_url`

Analyze data from Tea platform URL. Extracts project ID from URL, fetches DSL, performs analysis, and saves results locally. Returns DSL file path and analysis result file path.

---

**Parameters Schema:**

{"type":"object","properties":{"url":{"type":"string","description":"Tea platform URL, e.g., https://data.bytedance.net/tea-next/project/6/event-analysis/xxxxx","properties":{}}},"required":["url"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="tea", tool_name="mcp:tea_tea_analyze_by_url", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)