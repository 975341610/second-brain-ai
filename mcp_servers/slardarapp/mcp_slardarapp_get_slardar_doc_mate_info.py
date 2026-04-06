"""
# `mcp:SlardarApp_get_slardar_doc_mate_info`

获取Slardar异常参考解决方案文档的描述信息

---

**Parameters Schema:**

{"type":"object","properties":{"slardar_link":{"type":"string","description":"Slardar issue链接","properties":{}}},"required":["slardar_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_slardar_doc_mate_info", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)