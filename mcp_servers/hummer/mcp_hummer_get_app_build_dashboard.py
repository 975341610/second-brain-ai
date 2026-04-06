"""
# `mcp:hummer_get_app_build_dashboard`

查询一段时间内的全量/增量/总构建次数，全量/增量构建平均耗时，以及这段时间内每天的全量/增量明细数据，包括构建次数，构建耗时的均值，P10，P50，P90值，耗时单位为毫秒

---

**Parameters Schema:**

{"type":"object","properties":{"appId":{"type":"string","description":"查询应用的AppId","properties":{}},"endDate":{"type":"string","description":"查询的终止日期，格式为YYYY-MM-DD","properties":{}},"packageName":{"type":"string","description":"查询应用的packageName","properties":{}},"startDate":{"type":"string","description":"查询的起始日期，格式为YYYY-MM-DD","properties":{}},"variant":{"type":"string","description":"查询的variant，默认应查询debug","enum":["debug","release"],"properties":{}}},"required":["appId","packageName","startDate","endDate","variant"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="hummer", tool_name="mcp:hummer_get_app_build_dashboard", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)