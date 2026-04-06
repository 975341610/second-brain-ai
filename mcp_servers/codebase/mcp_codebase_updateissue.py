"""
# `mcp:codebase_UpdateIssue`

Update an existing issue.

---

**Parameters Schema:**

{"type":"object","properties":{"AssigneeIds":{"type":"array","description":"Optional. New list of user IDs to assign to the issue. If not provided, assignees remain unchanged. If empty array is provided, all assignees will be removed.","properties":{},"items":{"type":"string","properties":{}}},"Description":{"type":"string","description":"Optional. New description for the issue.","properties":{}},"DueDate":{"type":"string","description":"Optional. New due date for the issue. e.g. \"2006-01-02\". Set to empty string to clear due date.","properties":{}},"Number":{"type":"integer","description":"The number of the issue.","properties":{}},"ParentIssueId":{"type":"string","description":"Optional. New parent issue ID to change the parent-child relationship.","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"Status":{"type":"string","description":"Optional. New status for the issue. Available options: \"backlog\" (not started), \"todo\" (ready to work), \"in_progress\" (being worked on), \"done\" (completed), \"canceled\" (abandoned).","enum":["todo","done","canceled","in_progress","backlog"],"properties":{}},"Title":{"type":"string","description":"Optional. New title for the issue.","properties":{}}},"required":["RepoId","Number"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_UpdateIssue", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)