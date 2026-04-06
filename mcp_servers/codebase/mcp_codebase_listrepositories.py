"""
# `mcp:codebase_ListRepositories`

List repositories with various filters.
If you want to get a repository by known repo ID or path (e.g. path/to/repo), it's better to use `GetRepository`.

---

**Parameters Schema:**

{"type":"object","properties":{"ContributedById":{"type":"string","description":"Optional. Filter repositories by contributor ID. Requires that the specified user has contributed to the repository. If `ContributedById` is specified, no other filters are allowed.","properties":{}},"PageNumber":{"type":"integer","description":"Optional. Pagination number, starts from 1.","properties":{},"minimum":1},"PageSize":{"type":"integer","description":"Optional. Pagination size. Maximum 100, default is 10.","properties":{},"minimum":1,"maximum":100},"Query":{"type":"string","description":"Optional. Filter repositories by path. Matches either the full repository path prefix or the prefix of the last segment in the path.","properties":{}},"SortBy":{"type":"string","description":"Optional. Sort results by either the last activity time (`PushedAt`), repository path (`Path`) or the time of my last contribution (`ContributedAt`). Default is `ContributedAt`.","enum":["PushedAt","Path","ContributedAt"],"properties":{}},"SortOrder":{"type":"string","description":"Optional. Sort order: `Asc` or `Desc`.","enum":["Asc","Desc"],"properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_ListRepositories", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)