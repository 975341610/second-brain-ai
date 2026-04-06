"""
# `mcp:codebase_GetCommit`

Get a specific commit.

---

**Parameters Schema:**

{"type":"object","properties":{"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"Revision":{"type":"string","description":"The commit ID or other git reference (branch, tag).","properties":{}}},"required":["RepoId","Revision"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_GetCommit", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)