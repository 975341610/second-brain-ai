"""
# `mcp:codebase_SearchIssues`

Search issues across repositories or within a specific repository.

---

**Parameters Schema:**

{"type":"object","properties":{"Assignee":{"type":"string","description":"Optional. Filter by assignee username. Only returns issues assigned to the specified user.","properties":{}},"DueDateSince":{"type":"string","description":"Optional. Filter issues with due dates on or after this date. Use RFC3339 format (e.g. \"2024-01-15T00:00:00Z\").","properties":{}},"DueDateUntil":{"type":"string","description":"Optional. Filter issues with due dates on or before this date. Use RFC3339 format (e.g. \"2024-12-31T23:59:59Z\").","properties":{}},"PageSize":{"type":"integer","description":"Optional. Number of issues to return per page. Must be between 1-100. Default: 10.","properties":{},"minimum":1,"maximum":100},"PageToken":{"type":"string","description":"Optional. Pagination token from previous response. Leave empty to get the first page.","properties":{}},"Query":{"type":"string","description":"Optional. Search text to match against issue titles and descriptions. Supports partial matching.","properties":{}},"RepoId":{"type":"string","description":"Optional. Repository to search in. Can be repository ID (e.g. \"123456\") or full path (e.g. \"company/project\"). If not specified, searches across all accessible repositories.","properties":{}},"SortBy":{"type":"string","description":"Optional. Sort field: \"CreatedAt\" (when issue was created) or \"UpdatedAt\" (when issue was last modified). Default: \"UpdatedAt\".","enum":["CreatedAt","UpdatedAt"],"properties":{}},"SortOrder":{"type":"string","description":"Optional. Sort direction: \"Asc\" (oldest first) or \"Desc\" (newest first). Default: \"Desc\".","enum":["Asc","Desc"],"properties":{}},"Status":{"type":"string","description":"Optional. Filter by issue status. Available options: \"backlog\" (not started), \"todo\" (ready to work), \"in_progress\" (being worked on), \"done\" (completed), \"canceled\" (abandoned).","enum":["todo","done","canceled","in_progress","backlog"],"properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_SearchIssues", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)