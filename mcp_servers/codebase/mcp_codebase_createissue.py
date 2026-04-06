"""
# `mcp:codebase_CreateIssue`

Create an issue in a repository.

---

**Parameters Schema:**

{"type":"object","properties":{"AssigneeIds":{"type":"array","description":"Optional. List of user IDs to assign to the issue.","properties":{},"items":{"type":"string","properties":{}}},"Description":{"type":"string","description":"Optional. Description of the issue.","properties":{}},"DueDate":{"type":"string","description":"Optional. Due date for the issue. e.g. `2006-01-02`.","properties":{}},"LabelIds":{"type":"array","description":"Optional. List of label IDs to apply to the issue.","properties":{},"items":{"type":"string","properties":{}}},"ParentIssueId":{"type":"string","description":"Optional. Parent issue ID to create this as a sub-issue.","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"Status":{"type":"string","description":"Optional. Initial status for the issue. Default: \"backlog\".","enum":["todo","done","canceled","in_progress","backlog"],"properties":{}},"Title":{"type":"string","description":"Title of the issue.","properties":{}}},"required":["RepoId","Title"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_CreateIssue", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)