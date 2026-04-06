"""
# `mcp:deepwiki_ListWikiFilePaths`

List wiki file paths either by RepoId (e.g. 123456) or path (e.g. codebase/sdk). Either of the `Id` or `Path` must be provided.
It returns the file paths of the wiki files, starts with `zh` stands for Chinese, `en` stands for English.

---

**Parameters Schema:**

{"type":"object","properties":{"RepoId":{"type":"string","description":"The ID (e.g. 123456) or path (e.g. codebase/sdk) of the repository.","properties":{}},"VersionId":{"type":"string","description":"Optional. The ID of the wiki version.","properties":{}}},"required":["RepoId"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="deepwiki", tool_name="mcp:deepwiki_ListWikiFilePaths", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)