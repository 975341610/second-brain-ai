"""
# `mcp:codebase_ListMergeRequests`

List merge requests in a repository.

---

**Parameters Schema:**

{"type":"object","properties":{"Author":{"type":"string","description":"Optional. Filter by the author's username.","properties":{}},"CommitId":{"type":"string","description":"Optional. The commit ID must be complete.","properties":{}},"Draft":{"type":"boolean","description":"Optional. Draft means not ready to be reviewed or merged.","properties":{}},"Labels":{"type":"array","properties":{},"items":{"type":"string","properties":{}}},"PageNumber":{"type":"integer","description":"Optional. Pagination number, starts from 1.","properties":{},"minimum":1},"PageSize":{"type":"integer","description":"Optional. Pagination size. Default is 10.","properties":{},"minimum":1,"maximum":100},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"ReviewStatus":{"type":"string","description":"Optional. Filter by review status.","enum":["pending","passed","disapproved"],"properties":{}},"Reviewer":{"type":"string","description":"Optional. Filter by the reviewer's username.","properties":{}},"SortBy":{"type":"string","description":"Optional.","enum":["CreatedAt","UpdatedAt"],"properties":{}},"SortOrder":{"type":"string","description":"Optional.","enum":["Asc","Desc"],"properties":{}},"SourceBranch":{"type":"string","description":"Optional. Filter by the source branch name.","properties":{}},"Status":{"type":"string","description":"Optional. Filter by merge request status.","enum":["open","closed","merged"],"properties":{}},"TargetBranch":{"type":"string","description":"Optional. Filter by the target branch name.","properties":{}},"Title":{"type":"string","description":"Optional.","properties":{}}},"required":["RepoId"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_ListMergeRequests", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)