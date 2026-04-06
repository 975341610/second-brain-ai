"""
# `mcp:codebase_GetIssue`

Get an issue.

---

**Parameters Schema:**

{"type":"object","properties":{"Number":{"type":"integer","description":"The number of the issue.","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}}},"required":["RepoId","Number"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_GetIssue", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)