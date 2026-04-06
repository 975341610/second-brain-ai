"""
# `mcp:codebase_GetRepository`

Get a repository either by ID (e.g. 123456) or path (e.g. path/to/repo). Either of the `Id` or `Path` must be provided.

---

**Parameters Schema:**

{"type":"object","properties":{"Id":{"type":"string","description":"Optional. The ID of the repository.","properties":{}},"Path":{"type":"string","description":"Optional. The full path of the repository like \"path/to/repo\". You can get the repo ID by known repo path.","properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_GetRepository", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)