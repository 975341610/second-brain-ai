"""
# `mcp:tea_tea_analyze_by_dsl`

Analyze data using local DSL file. Reads DSL from file, generates page link, renames files according to hash, and performs analysis.

---

**Parameters Schema:**

{"type":"object","properties":{"dsl_file_path":{"type":"string","description":"Path to local DSL file","properties":{}},"project_id":{"type":"integer","description":"Tea project ID","properties":{}}},"required":["dsl_file_path","project_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="tea", tool_name="mcp:tea_tea_analyze_by_dsl", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)