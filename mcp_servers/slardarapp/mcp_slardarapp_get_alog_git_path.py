"""
# `mcp:SlardarApp_get_alog_git_path`

根据源文件名称、 commitID 等信息获取对应的 git url

---

**Parameters Schema:**

{"type":"object","properties":{"aid":{"type":"number","description":"应用 ID","properties":{}},"commit_info":{"type":"array","description":"多个文件名及其 commitID","properties":{},"items":{"type":"object","properties":{"commit_id":{"type":"string","description":"commit ID","properties":{}},"file_name":{"type":"string","description":"源文件名称","properties":{}},"line":{"type":"string","description":"源代码所在行号","properties":{}}},"required":["commit_id","line","file_name"]}}},"required":["aid","commit_info"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_alog_git_path", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)