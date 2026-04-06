"""
# `mcp:aeolus_aeolus_get_filter_options`

获取图表过滤器可选项，根据指定的Dashboard ID、Report ID、Sheet ID和过滤器ID，返回该过滤器的所有可选项。注意过滤器为聚合多个数据集（dataset）的，存在同名过滤器

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"dashboard_id":{"type":"integer","description":"可选，Dashboard ID","properties":{}},"dataset_id":{"type":"integer","description":"必填，数据集ID，表明过滤器所属的数据集。","properties":{}},"filter_id":{"type":"integer","description":"必填，过滤器ID，别名DimMetID","properties":{}},"keyword":{"type":"string","description":"可选，搜索关键词","properties":{}},"report_id":{"type":"integer","description":"可选，Report ID","properties":{}},"sheet_id":{"type":"integer","description":"可选，Sheet ID","properties":{}}},"required":["base_url","dashboard_id","sheet_id","report_id","filter_id","dataset_id","keyword"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_get_filter_options", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)