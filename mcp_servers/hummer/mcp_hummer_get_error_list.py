"""
# `mcp:hummer_get_error_list`

查询一段时间内的编译错误数据列表，返回每条数据的信息，包含ID，错误数，影响用户数，错误堆栈

---

**Parameters Schema:**

{"type":"object","properties":{"appId":{"type":"string","description":"查询应用的AppId","properties":{}},"email":{"type":"string","description":"用户邮箱地址，查询特定用户数据时传","properties":{}},"endDate":{"type":"string","description":"查询的终止日期，格式为YYYY-MM-DD","properties":{}},"packageName":{"type":"string","description":"查询应用的packageName","properties":{}},"page":{"type":"number","description":"查询的页码，从0开始","properties":{}},"size":{"type":"number","description":"查询的每页大小，默认为30","properties":{}},"startDate":{"type":"string","description":"查询的起始日期，格式为YYYY-MM-DD","properties":{}},"type":{"type":"string","description":"1表示查询异常错误，2表示查询普通错误，0表示查询所有错误","enum":["0","1","2"],"properties":{}}},"required":["appId","packageName","startDate","endDate","page","size","type"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="hummer", tool_name="mcp:hummer_get_error_list", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)