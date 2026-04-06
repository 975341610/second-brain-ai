"""
# `mcp:meego_search_meego_spaces`

通过关键词搜索用户所属下所有的空间信息，该工具用于根据关键字搜索空间，返回空间map，key为simple_name，value为空间详情，空间详情中包括搜索相关度的得分，得分越小表示匹配度越高

---

**Parameters Schema:**

{"type":"object","properties":{"keywords":{"type":"array","description":"关键字列表，用于搜索空间","properties":{},"items":{"type":"string","properties":{}}}},"required":["keywords"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_search_meego_spaces", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)