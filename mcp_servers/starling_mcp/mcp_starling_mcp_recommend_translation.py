"""
# `mcp:Starling_MCP_recommend_translation`

Analyze code content and recommend translations for Chinese text

---

**Parameters Schema:**

{"type":"object","properties":{"content":{"type":"string","description":"The code content to analyze","properties":{}},"namespaceId":{"type":"number","description":"Starling 命名空间 ID，如果填了 Starling 命名空间 ID 也必须填 Starling 项目 ID","properties":{}},"projectId":{"type":"number","description":"Starling 项目 ID，如果填了 Starling 项目 ID 也必须填 Starling 命名空间 ID","properties":{}},"starling_access_key":{"type":"string","description":"Starling Access Key","properties":{}},"starling_secret_key":{"type":"string","description":"Starling Secret Key","properties":{}}},"required":["content"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="Starling_MCP", tool_name="mcp:Starling_MCP_recommend_translation", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)