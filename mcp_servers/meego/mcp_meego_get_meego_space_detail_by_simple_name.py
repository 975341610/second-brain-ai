"""
# `mcp:meego_get_meego_space_detail_by_simple_name`

该接口用于根据空间简称获取空间详情信息，返回值为一个map，key为simple_name，value为空间详情信息，包括空间名称、空间描述、空间管理员、空间成员、空间业务线等信息。注意：该工具不要重复调用

---

**Parameters Schema:**

{"type":"object","properties":{"simple_name":{"type":"string","description":"空间简称, 只能通过列表或者搜索空间之类的接口获得， 参数示例：\"feishu-test\"","properties":{}}},"required":["simple_name"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_get_meego_space_detail_by_simple_name", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)