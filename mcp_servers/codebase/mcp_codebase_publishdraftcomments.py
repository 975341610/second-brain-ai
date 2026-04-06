"""
# `mcp:codebase_PublishDraftComments`

Publish all draft comments previously created in this merge request.

---

**Parameters Schema:**

{"type":"object","properties":{"Number":{"type":"integer","description":"The number of the merge request.","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"ReviewContent":{"type":"string","description":"Optional. The summary review content to include for publishing.","properties":{}}},"required":["RepoId","Number"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_PublishDraftComments", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)