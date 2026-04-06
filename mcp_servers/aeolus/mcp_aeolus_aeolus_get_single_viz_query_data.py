"""
# `mcp:aeolus_aeolus_get_single_viz_query_data`

查询风神可视化查询下的数据（单图或历史），json 格式，数据与页面展示一致

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"history_id":{"type":"integer","description":"与 report_id 二选一，页面参数 id，如果存在，优先设置","properties":{}},"report_id":{"type":"integer","description":"建议指定，在浏览器参数中名字为 rid","properties":{}}},"required":["base_url","history_id","report_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_get_single_viz_query_data", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)