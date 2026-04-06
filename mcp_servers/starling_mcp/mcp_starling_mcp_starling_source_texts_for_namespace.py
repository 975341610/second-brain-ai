"""
# `mcp:Starling_MCP_starling_source_texts_for_namespace`

获取命名空间的源文本列表

---

**Parameters Schema:**

{"type":"object","properties":{"keyTexts":{"type":"array","description":"检索：精确匹配 keys","properties":{},"items":{"type":"string","properties":{}}},"limit":{"type":"number","description":"翻页最大数量。default: 25，最大值：200","properties":{},"default":25},"namespaceId":{"type":"number","description":"命名空间ID","properties":{}},"offset":{"type":"number","description":"翻页偏移量。default: 0","properties":{},"default":0},"projectId":{"type":"number","description":"项目ID","properties":{}},"starling_access_key":{"type":"string","description":"Starling Access Key","properties":{}},"starling_secret_key":{"type":"string","description":"Starling Secret Key","properties":{}}},"required":["projectId","namespaceId"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="Starling_MCP", tool_name="mcp:Starling_MCP_starling_source_texts_for_namespace", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)