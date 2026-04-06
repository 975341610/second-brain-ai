"""
# `mcp:codebase_ListMergeRequestCheckRuns`

List check runs for a merge request.

---

**Parameters Schema:**

{"type":"object","properties":{"Number":{"type":"integer","description":"The number of the merge request.","properties":{}},"PageNumber":{"type":"integer","description":"Pagination number, starts from 1.","properties":{}},"PageSize":{"type":"integer","description":"Pagination size. Maximum 100, default is 10.","properties":{}},"Query":{"type":"string","description":"Optional. Search text to match against check run name and description (case-insensitive, substring match).","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"Unsuccessful":{"type":"boolean","description":"`true` means filter unsuccessful check runs (pending, running, failed, warning, etc.). Default is `false`.","properties":{}}},"required":["RepoId","Number","Unsuccessful","PageNumber","PageSize"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_ListMergeRequestCheckRuns", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)