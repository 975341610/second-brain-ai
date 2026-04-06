"""
# `mcp:SlardarApp_get_issue_field_percent`

根据用户提供的Slardar issue链接，查询某个issue下，某个字段的属性分布
注意：
1. 先调用另外一个工具，获取维度列表和相关信息
2. 如果不确定field的取值，优先使用"filters"

---

**Parameters Schema:**

{"type":"object","properties":{"field":{"type":"string","description":"字段在对应数据表中的字段名","properties":{}},"map_key":{"type":"string","description":"对于字典类型字段，需要指明具体的map_key","properties":{}},"slardar_link":{"type":"string","properties":{},"format":"uri"}},"required":["slardar_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_issue_field_percent", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)