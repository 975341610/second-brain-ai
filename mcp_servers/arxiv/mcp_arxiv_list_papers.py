"""
# `mcp:arxiv_list_papers`

List all downloaded and converted arxiv papers available in local storage

---

**Parameters Schema:**

{"type":"object","properties":{}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="arxiv", tool_name="mcp:arxiv_list_papers", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)