"""
# `mcp:hummer_get_important_task_avg_duration`

查询一段时间内的重要Task执行平均耗时，返回这段时间内的重点Task的名称，耗时均值，执行次数，以及这个Task所属类型

---

**Parameters Schema:**

{"type":"object","properties":{"appId":{"type":"string","description":"查询应用的AppId","properties":{}},"endDate":{"type":"string","description":"查询的终止日期，格式为YYYY-MM-DD","properties":{}},"increment":{"type":"string","description":"1表示只查询增量编译，2表示只查询全量编译，不传值则默认查询所有编译，默认应为1，查询release时应传2","enum":["1","2"],"properties":{}},"packageName":{"type":"string","description":"查询应用的packageName","properties":{}},"startDate":{"type":"string","description":"查询的起始日期，格式为YYYY-MM-DD","properties":{}},"variant":{"type":"string","description":"查询的variant，默认应查询debug","enum":["debug","release"],"properties":{}}},"required":["appId","packageName","startDate","endDate","variant","increment"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="hummer", tool_name="mcp:hummer_get_important_task_avg_duration", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)