"""
# `mcp:aeolus_aeolus_get_viz_query_data`

查询风神看板下图表的数据，json格式，数据与页面上展示一致，report_filters表示图表的过滤器配置，public表示看板公共筛选器通常可以对多个数据图表生效，self表示图表自身配置的筛选器

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"dashboard_id":{"type":"integer","description":"必填，Dashboard ID","properties":{}},"report_filters":{"type":"object","description":"可选，图表的过滤器配置，一个 reportId 对应一个 Filters 结构体，id 表示过滤器 id，val 表示过滤器值列表","properties":{},"additionalProperties":{"type":"array","properties":{},"items":{"type":"object","properties":{"anchor_offset":{"type":"integer","description":"锚点偏移量，仅在date_mode为relative时，可选值：0,1，例如anchor_offset: 0，datetime_unit: day 表示查询今天，anchor_offset: 1，datetime_unit: day 表示查询昨天，不要填写其他值","properties":{}},"date_mode":{"type":"string","description":"可选，仅对日期类型生效，可选值：relative,absolute，如设置，必须配合val和datetime_unit使用","properties":{}},"datetime_unit":{"type":"string","description":"时间单位，仅在date_mode为relative时，可选值：day,week,month,quarter,year","properties":{}},"id":{"type":"string","description":"过滤器ID，图表的过滤项可能存在同名但不同数据集的过滤器ID，所以必须过滤器ID和val必须严格对上","properties":{}},"val":{"type":"array","description":"过滤器值列表，支持包含 null（用 JSON null 表达空值），对与非时间类型的值，通过aeolus_get_filter_options获取可选值，当过滤类型为时间类型并且是absolute模式，val的值有且只能是start和end时间的值，格式为YYYY-MM-DD HH:MM:SS，如果模式为relative，val表示相对的时间单位数量，为一个整数","properties":{},"items":{"type":"string","properties":{}}}},"required":["id","val","date_mode","datetime_unit","anchor_offset"]}}},"report_id":{"type":"integer","description":"建议指定，Report ID，也就是图表id，如果不指定，将会批量下载看板内所有图表数据，如果图表过多可能造成上下文巨大，酌情处理","properties":{}},"sheet_id":{"type":"integer","description":"可选，Sheet ID，不指定则只能返回默认页面图表数据，强烈建议先通过aeolus_dashboard_and_sheet确认有哪些页面","properties":{}}},"required":["base_url","dashboard_id","sheet_id","report_id","report_filters"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_get_viz_query_data", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)