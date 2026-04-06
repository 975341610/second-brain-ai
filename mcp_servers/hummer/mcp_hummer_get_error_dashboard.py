"""
# `mcp:hummer_get_error_dashboard`

查询一段时间内的总编译次数和编译错误次数，以及这段时间内每天的编译错误次数

---

**Parameters Schema:**

{"type":"object","properties":{"appId":{"type":"string","description":"查询应用的AppId","properties":{}},"email":{"type":"string","description":"用户邮箱地址，查询特定用户数据时传","properties":{}},"endDate":{"type":"string","description":"查询的终止日期，格式为YYYY-MM-DD","properties":{}},"increment":{"type":"string","description":"1表示只查询增量编译，2表示只查询全量编译，不传值则默认查询所有编译，默认应为1，查询release时应传2","enum":["1","2"],"properties":{}},"packageName":{"type":"string","description":"查询应用的packageName","properties":{}},"startDate":{"type":"string","description":"查询的起始日期，格式为YYYY-MM-DD","properties":{}},"type":{"type":"string","description":"1表示查询异常错误，2表示查询普通错误，0表示查询所有错误","enum":["0","1","2"],"properties":{}},"variant":{"type":"string","description":"查询的variant，默认应查询debug","enum":["debug","release"],"properties":{}}},"required":["appId","packageName","variant","increment","startDate","endDate","type"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="hummer", tool_name="mcp:hummer_get_error_dashboard", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)