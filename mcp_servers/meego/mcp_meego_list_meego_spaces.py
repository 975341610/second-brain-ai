"""
# `mcp:meego_list_meego_spaces`

list meego spaces that user has access permission in meego, return a list contains the union set among all public meego spaces, user self's meego spaces and plugin-installed meego spaces, default sort by user access time desc. Also important: the meego space list maybe huge, ask user which or a set of meego spaces that user is interested in, do not choose meego space by your opinion!

---

**Parameters Schema:**

{"type":"object","properties":{"simple_name":{"type":"array","description":"非必填，空间名称列表, 空间名称例如：feishu-test","properties":{},"items":{"type":"string","properties":{}}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_list_meego_spaces", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)