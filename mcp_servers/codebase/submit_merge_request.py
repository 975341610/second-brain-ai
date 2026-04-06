"""
# `submit_merge_request`

Submit a merge request to codebase

---

**Parameters Schema:**

{"type":"object","properties":{"description":{"type":"string","description":"description of the merge request","properties":{}},"draft":{"type":"boolean","description":"whether to create a draft merge request, defaults to true","properties":{}},"repo_name":{"type":"string","description":"name of the repository to submit merge request","properties":{}},"source_branch":{"type":"string","description":"source branch to submit merge request","properties":{}},"target_branch":{"type":"string","description":"target branch to submit merge request","properties":{}},"title":{"type":"string","description":"title of the merge request","properties":{}}},"required":["repo_name","source_branch","target_branch","title","description","draft"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="submit_merge_request", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)