"""
# `mcp:codebase_ListCommits`

List commits.

---

**Parameters Schema:**

{"type":"object","properties":{"Author":{"type":"string","description":"Show commits authored by a specific author's username.","properties":{}},"PageNumber":{"type":"integer","description":"Pagination number, starts from 1.","properties":{},"minimum":1},"PageSize":{"type":"integer","description":"Pagination size. Default is 10.","properties":{},"minimum":1,"maximum":100},"Path":{"type":"string","description":"List commit history for the given path, empty for the whole repository.","properties":{}},"Query":{"type":"string","description":"Show commits with message (includes title and body) that matches the specified pattern.","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"Revision":{"type":"string","description":"The revision to list commits from.","properties":{}}},"required":["RepoId","Revision"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_ListCommits", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)