"""
# `mcp:SlardarApp_get_issue_detail`

根据用户提供的Slardar issue链接，获取某个issue的基础信息，包括issue负责人、lark交流群、业务信息、issue状态、issue等级、issue标题等信息

---

**Parameters Schema:**

{"type":"object","properties":{"slardar_link":{"type":"string","description":"Slardar issue链接, 以https://slardar.bytedance.net/或者https://t.wtturl.cn开始的完整URL","properties":{},"format":"uri"}},"required":["slardar_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_issue_detail", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)