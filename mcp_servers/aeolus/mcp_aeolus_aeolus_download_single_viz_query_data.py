"""
# `mcp:aeolus_aeolus_download_single_viz_query_data`

下载单个风神图表/历史查询数据为 CSV 文件，不做看板筛选合并，可以通过调节limit参数获取大于图表展示的数据内容，建议在query数据不满足需求后，再使用此工具下载

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"history_id":{"type":"integer","description":"与 report_id 二选一，页面参数 id，如果存在，优先设置","properties":{}},"limit":{"type":"integer","description":"下载行数上限，默认1000000","properties":{}},"report_id":{"type":"integer","description":"与 history_id 二选一，页面参数 rid","properties":{}},"report_name":{"type":"string","description":"下载文件名（不含扩展名），为空则使用图表名/历史查询名","properties":{}}},"required":["base_url","report_id","history_id","report_name","limit"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_download_single_viz_query_data", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)