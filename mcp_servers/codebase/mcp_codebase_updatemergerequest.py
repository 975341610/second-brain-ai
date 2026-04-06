"""
# `mcp:codebase_UpdateMergeRequest`

Update a merge request.

---

**Parameters Schema:**

{"type":"object","properties":{"AutoMerge":{"type":"boolean","description":"Whether to enable auto merge.","properties":{}},"Description":{"type":"string","description":"The new description of the merge request.","properties":{}},"Draft":{"type":"boolean","description":"Whether the merge request is a draft. Draft means not ready to be reviewed or merged.","properties":{}},"Number":{"type":"integer","description":"The number of the merge request.","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"Title":{"type":"string","description":"The new title of the merge request.","properties":{}},"WorkItemIds":{"type":"array","description":"The IDs of the work items (like Meego tickets) to link to the merge request.","properties":{},"items":{"type":"string","properties":{}}}},"required":["RepoId","Number"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_UpdateMergeRequest", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)