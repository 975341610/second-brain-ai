"""
# `mcp:hummer_get_build_list`

查询一段时间内的编译数据列表，返回总条数，以及每条数据的信息，包含ID，编译用户的Email，Configuration耗时，dexBuild耗时，dexMerge耗时，kotlin耗时，task执行耗时，transform耗时，总耗时，开始时间，packageName，成功状态，错误信息

---

**Parameters Schema:**

{"type":"object","properties":{"appId":{"type":"string","description":"查询应用的AppId","properties":{}},"buildSuccess":{"type":"string","description":"查询的构建成功状态，不传值则默认查询所有状态，success表示只查询成功的编译，failure表示只查询失败的编译","properties":{}},"email":{"type":"string","description":"用户邮箱地址，查询特定用户数据时传","properties":{}},"endDate":{"type":"string","description":"查询的终止日期，格式为YYYY-MM-DD","properties":{}},"increment":{"type":"string","description":"1表示只查询增量编译，2表示只查询全量编译，不传值则默认查询所有编译，查询release时应传2","enum":["1","2"],"properties":{}},"packageName":{"type":"string","description":"查询应用的packageName","properties":{}},"page":{"type":"number","description":"查询的页码，从0开始","properties":{}},"size":{"type":"number","description":"查询的每页大小，默认为10","properties":{}},"startDate":{"type":"string","description":"查询的起始日期，格式为YYYY-MM-DD","properties":{}},"variant":{"type":"string","description":"查询的variant，默认应查询debug","enum":["debug","release"],"properties":{}}},"required":["appId","packageName","variant","startDate","endDate","page","size"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="hummer", tool_name="mcp:hummer_get_build_list", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)