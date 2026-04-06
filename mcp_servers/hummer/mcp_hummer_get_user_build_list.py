"""
# `mcp:hummer_get_user_build_list`

查询用户一段时间内的编译数据列表，返回包括总条数，以及每条数据的信息，包括：appId，packageName，是否增量，开始时间，构建耗时，成功状态，hummer 链接等

---

**Parameters Schema:**

{"type":"object","properties":{"email":{"type":"string","description":"用户邮箱","properties":{}},"endDate":{"type":"string","description":"查询的终止日期，格式为 YYYY-MM-DD","properties":{}},"machine":{"type":"string","description":"查询的机器类型，可选 PC、RemoteX、AirCode、CI、空","enum":["PC","RemoteX","AirCode","CI"],"properties":{}},"page":{"type":"number","description":"查询的页码，默认为 0","properties":{},"default":0},"size":{"type":"number","description":"查询的每页大小，默认为 10","properties":{},"default":10},"startDate":{"type":"string","description":"查询的起始日期，格式为 YYYY-MM-DD","properties":{}},"variant":{"type":"string","description":"查询的variant，可选 debug、release、空","enum":["debug","release"],"properties":{}}},"required":["email","startDate","endDate"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="hummer", tool_name="mcp:hummer_get_user_build_list", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)