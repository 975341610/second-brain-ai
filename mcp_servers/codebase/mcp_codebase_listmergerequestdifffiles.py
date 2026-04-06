"""
# `mcp:codebase_ListMergeRequestDiffFiles`

List the diff files (diff metadata or diff patch) of a merge request on the latest version. Large diff files will be pruned.

---

**Parameters Schema:**

{"type":"object","properties":{"Context":{"type":"integer","description":"How many lines of diff context should be returned. Default is 3.","properties":{}},"Excludes":{"type":"array","description":"Excludes diff files that match the patterns (supports wlidcard). If empty, no diff files will be excluded.","properties":{},"items":{"type":"string","properties":{}}},"FilesOnly":{"type":"boolean","description":"Whether to return only the diff file metadata. Default is false.","properties":{}},"Includes":{"type":"array","description":"Includes diff files that match the patterns (supports wlidcard). If empty, all diff files will be included.","properties":{},"items":{"type":"string","properties":{}}},"Number":{"type":"integer","description":"The number of the merge request.","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}}},"required":["RepoId","Number"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_ListMergeRequestDiffFiles", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)