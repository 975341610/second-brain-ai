"""
# `mcp:Bits-AppCenter_bits_app_center_get_sot`

获取SOT文件的详细信息

---

**Parameters Schema:**

{"type":"object","properties":{"path":{"type":"array","description":"path of this sot with filename, relative to git root","properties":{},"items":{"type":"string","properties":{}}},"repo":{"type":"string","description":"git repo of this sot","properties":{}}},"required":["repo","path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="Bits-AppCenter", tool_name="mcp:Bits-AppCenter_bits_app_center_get_sot", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)