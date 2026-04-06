"""
# `mcp:codebase_ListMergeRequestComments`

List comments in a merge request.

---

**Parameters Schema:**

{"type":"object","properties":{"Number":{"type":"integer","description":"The number of the merge request.","properties":{}},"Outdated":{"type":"boolean","description":"Optional. Filter by outdated comments. Set to false to exclude outdated comments; set to true to include only outdated comments. If not set, returns all comments regardless of outdated status.","properties":{}},"PageNumber":{"type":"integer","description":"Optional. Pagination number, starts from 1.","properties":{},"minimum":1},"PageSize":{"type":"integer","description":"Optional. Pagination size. Default is no limit.","properties":{},"minimum":1,"maximum":100},"Query":{"type":"string","description":"Optional. Filter by comment content.","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"Status":{"type":"string","description":"Optional. Filter by comment status. If not set, returns both open and resolved comments.","enum":["open","resolved"],"properties":{}}},"required":["RepoId","Number"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_ListMergeRequestComments", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)