"""
# `mcp:codebase_ListCommitDiffFiles`

List the diff files (diff metadata or diff patch) between two commits (or a single commit). Large diff files will be pruned.

---

**Parameters Schema:**

{"type":"object","properties":{"Context":{"type":"integer","description":"How many lines of diff context should be returned. Default is 3.","properties":{}},"Excludes":{"type":"array","description":"Excludes diff files that match the patterns (supports wlidcard). If empty, no diff files will be excluded.","properties":{},"items":{"type":"string","properties":{}}},"FilesOnly":{"type":"boolean","description":"Whether to return only the diff file metadata. Default is false.","properties":{}},"FromCommit":{"type":"string","description":"The commit ID to list diff files from. If empty, it will returns the diff for the commit `ToCommit` only.","properties":{}},"Includes":{"type":"array","description":"Includes diff files that match the patterns (supports wlidcard). If empty, all diff files will be included.","properties":{},"items":{"type":"string","properties":{}}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"ToCommit":{"type":"string","description":"The commit ID to list diff files to.","properties":{}}},"required":["RepoId","FromCommit","ToCommit"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_ListCommitDiffFiles", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)