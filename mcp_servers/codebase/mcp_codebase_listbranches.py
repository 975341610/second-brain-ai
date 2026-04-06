"""
# `mcp:codebase_ListBranches`

List branches.

---

**Parameters Schema:**

{"type":"object","properties":{"PageNumber":{"type":"integer","description":"Pagination number, starts from 1.","properties":{},"minimum":1},"PageSize":{"type":"integer","description":"Pagination size. Maximum 100, default is 10.","properties":{},"minimum":1,"maximum":100},"Query":{"type":"string","description":"Search query, such as `feat` to match `add_new_feat` or `feat/new_page`. Valid only when Type is `all`.","properties":{}},"QueryMode":{"type":"string","description":"Query mode. Default: `substr`.","enum":["substr","prefix","suffix","glob","wildcard"],"properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"Type":{"type":"string","description":"Branch type. Default: `all`.","enum":["all","merged","active","stale","yours"],"properties":{}}},"required":["RepoId"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_ListBranches", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)