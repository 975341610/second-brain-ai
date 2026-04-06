"""
# `add_merge_request_discussion`

only for posting a global comment on a merge request, fully aware of the potential consequences: using this tool may lead to the loss of association between the comment and the code. If it is an update but not a new comment, the comment ID must be provided.

---

**Parameters Schema:**

{"type":"object","properties":{"comment":{"type":"object","description":"global comment to create","properties":{"content":{"type":"string","description":"Discussion of the mr.","properties":{}},"id":{"type":"string","description":"comment id, must be provided when update comment","properties":{}}},"required":["content","id"]},"number":{"type":"integer","description":"the number of the merge request","properties":{}},"repo_name":{"type":"string","description":"codebase repo name, eg group/repo","properties":{}}},"required":["repo_name","number","comment"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="add_merge_request_discussion", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)