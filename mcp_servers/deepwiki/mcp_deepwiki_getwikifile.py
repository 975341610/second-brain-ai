"""
# `mcp:deepwiki_GetWikiFile`

Get a wiki file by RepoID and Path. `RepoId` and `Path` must be provided.

---

**Parameters Schema:**

{"type":"object","properties":{"Path":{"type":"string","description":"The path of the wiki file.","properties":{}},"RepoId":{"type":"string","description":"The ID (e.g. 123456) or path (e.g. codebase/sdk) of the repository.","properties":{}},"VersionId":{"type":"string","description":"Optional. The ID of the wiki version.","properties":{}}},"required":["RepoId","Path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="deepwiki", tool_name="mcp:deepwiki_GetWikiFile", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)