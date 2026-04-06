"""
# `mcp:oncall_search_oncall_from_url`

**优先工具**：当用户提供OnCall平台URL链接时，优先使用此工具。基于OnCall搜索URL（https://oncall.bytedance.net/admin/review/all）直接解析并查询数据，支持指定时间范围，可选获取群聊详情，结果导出为xlsx。支持包含filter_fields参数的搜索链接，或包含id参数的工单链接。

---

**Parameters Schema:**

{"type":"object","properties":{"end_time":{"type":"string","description":"可选，结束时间，格式：YYYY-MM-DD HH:mm，如不提供则使用URL中的时间","properties":{}},"limit_record_num":{"type":"integer","description":"可选，填写最多需要获取的记录数目。默认是2000，上限是2000","properties":{}},"need_chat_detail":{"type":"boolean","description":"是否需要获取每个Oncall群聊详情，为true则在搜索工单的同时获取所有群聊详情，默认不获取","properties":{}},"start_time":{"type":"string","description":"可选，开始时间，格式：YYYY-MM-DD HH:mm，如不提供则使用URL中的时间","properties":{}},"url":{"type":"string","description":"[Required] OnCall平台的搜索结果URL。必须是来自 https://oncall.bytedance.net/admin/review/all 页面的完整URL链接。支持两种格式：1. 包含filter_fields查询参数（搜索结果页）；2. 包含id参数（工单详情页）。","properties":{}}},"required":["url"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="oncall", tool_name="mcp:oncall_search_oncall_from_url", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)