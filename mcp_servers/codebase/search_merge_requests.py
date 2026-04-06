"""
# `search_merge_requests`

search merged merge requests by username and time range across all(default) or specified repositories, returns a json file path containing results grouped by repository, MRs within the file are sorted by time in descending order

---

**Parameters Schema:**

{"type":"object","properties":{"repo_paths":{"type":"array","description":"Optional repository paths to filter merge requests (e.g., ['ugc/tiktok', 'ugc/douyin']). If not specified, searches all repositories.","properties":{},"items":{"type":"string","properties":{}}},"since":{"type":"string","description":"Filter merge requests updated after this time. In RFC3339 format (e.g. '2006-01-02T15:04:05Z07:00').","properties":{}},"until":{"type":"string","description":"Filter merge requests updated before this time. In RFC3339 format (e.g. '2006-01-02T15:04:05Z07:00').","properties":{}},"username":{"type":"string","description":"Codebase username to filter merge requests by author. Must be a valid user ID (e.g., 'zhangsan.001'). Do not use Chinese display names or mixed formats.","properties":{}}},"required":["username"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="search_merge_requests", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)