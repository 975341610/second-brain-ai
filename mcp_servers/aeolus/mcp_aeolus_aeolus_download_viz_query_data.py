"""
# `mcp:aeolus_aeolus_download_viz_query_data`

下载风神看板下图表的数据为csv文件，可以通过调节limit参数获取大于图表展示的数据内容，建议在aeolus_get_viz_query_data获取到数据后预览分析后，再使用此工具下载，支持单图或整页面(sheet)批量

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"dashboard_id":{"type":"integer","description":"必填，Dashboard ID","properties":{}},"limit":{"type":"integer","description":"下载行数上限，默认1000000","properties":{}},"report_filters":{"type":"object","description":"可选，图表过滤器覆盖配置：key 为 reportId，value 为 Filters 数组；每个 Filters 的 id 为 dimMetId，val 支持包含 null","properties":{},"additionalProperties":{"type":"array","properties":{},"items":{"type":"object","properties":{"anchor_offset":{"type":"integer","description":"锚点偏移量，仅在date_mode为relative时，可选值：0,1，例如anchor_offset: 0，datetime_unit: day 表示查询今天，anchor_offset: 1，datetime_unit: day 表示查询昨天，不要填写其他值","properties":{}},"date_mode":{"type":"string","description":"可选，仅对日期类型生效，可选值：relative,absolute，如设置，必须配合val和datetime_unit使用","properties":{}},"datetime_unit":{"type":"string","description":"时间单位，仅在date_mode为relative时，可选值：day,week,month,quarter,year","properties":{}},"id":{"type":"string","description":"过滤器ID，图表的过滤项可能存在同名但不同数据集的过滤器ID，所以必须过滤器ID和val必须严格对上","properties":{}},"val":{"type":"array","description":"过滤器值列表，支持包含 null（用 JSON null 表达空值），对与非时间类型的值，通过aeolus_get_filter_options获取可选值，当过滤类型为时间类型并且是absolute模式，val的值有且只能是start和end时间的值，格式为YYYY-MM-DD HH:MM:SS，如果模式为relative，val表示相对的时间单位数量，为一个整数","properties":{},"items":{"type":"string","properties":{}}}},"required":["id","val","date_mode","datetime_unit","anchor_offset"]}}},"report_id":{"type":"integer","description":"可选，Report ID，不传表示下载该看板下所有图表","properties":{}},"report_name":{"type":"string","description":"下载文件名（不含扩展名），为空则使用 report_\u003creportId\u003e","properties":{}},"sheet_id":{"type":"integer","description":"可选，Sheet ID","properties":{}}},"required":["base_url","dashboard_id","report_id","sheet_id","report_name","limit","report_filters"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_download_viz_query_data", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)