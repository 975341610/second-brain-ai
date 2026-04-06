"""
# `get_merge_request_work_item_list`

get a merge request work item (meego) list

---

**Parameters Schema:**

{"type":"object","properties":{"merge_request_id":{"type":"integer","description":"merge request Id，this Id is the **GetMergeRequest output Id instead of the Number","properties":{}},"repo_id":{"type":"string","description":"codebase repo id","properties":{}}},"required":["repo_id","merge_request_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="get_merge_request_work_item_list", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)