"""
# `mcp:SlardarApp_get_slardar_doc_content`

获取Slardar异常参考解决方案的内容

---

**Parameters Schema:**

{"type":"object","properties":{"names":{"type":"array","description":"参考文档的名称","properties":{},"items":{"type":"string","description":"单个参考文档的名称","properties":{}}},"slardar_link":{"type":"string","description":"Slardar issue链接","properties":{}}},"required":["slardar_link","names"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_slardar_doc_content", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)