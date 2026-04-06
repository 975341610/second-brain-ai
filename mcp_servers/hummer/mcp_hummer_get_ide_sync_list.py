"""
# `mcp:hummer_get_ide_sync_list`

查询一段时间内的IDE Sync数据列表，返回总条数，以及每条数据的信息，包含ID，IDE Sync的用户Email，耗时，开始时间，packageName，成功状态，错误信息

---

**Parameters Schema:**

{"type":"object","properties":{"appId":{"type":"string","description":"查询应用的AppId","properties":{}},"email":{"type":"string","description":"用户邮箱地址，查询特定用户数据时传","properties":{}},"endDate":{"type":"string","description":"查询的终止日期，格式为YYYY-MM-DD","properties":{}},"page":{"type":"number","description":"查询的页码，从0开始","properties":{}},"size":{"type":"number","description":"查询的每页大小，默认为10","properties":{}},"startDate":{"type":"string","description":"查询的起始日期，格式为YYYY-MM-DD","properties":{}}},"required":["appId","startDate","endDate","page","size"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="hummer", tool_name="mcp:hummer_get_ide_sync_list", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)