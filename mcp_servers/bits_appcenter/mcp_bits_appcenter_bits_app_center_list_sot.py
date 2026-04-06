"""
# `mcp:Bits-AppCenter_bits_app_center_list_sot`

列出SOT列表，SOT是某个项目的IAC文件目录

---

**Parameters Schema:**

{"type":"object","properties":{"path":{"type":"string","description":"path of this sot with filename, relative to git root","properties":{}},"repo":{"type":"string","description":"git repo of this sot","properties":{}}},"required":["repo","path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="Bits-AppCenter", tool_name="mcp:Bits-AppCenter_bits_app_center_list_sot", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)