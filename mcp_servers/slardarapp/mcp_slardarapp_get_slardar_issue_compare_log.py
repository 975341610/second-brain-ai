"""
# `mcp:SlardarApp_get_slardar_issue_compare_log`

获取崩溃列表页链接的数据与n天前的崩溃列表页的数据合并成Issue对比数据，包括崩溃的基础数据与issue列表、维度分布等分析大盘劣化原因

---

**Parameters Schema:**

{"type":"object","properties":{"base_link":{"type":"string","description":"Slardar崩溃列表链接(基准数据)","properties":{}},"link":{"type":"string","description":"Slardar崩溃列表链接(对比数据)","properties":{}},"time_interval":{"type":"integer","description":"取n天前的数据作为对比数据,不传默认取一周前的数据","properties":{}}},"required":["link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_slardar_issue_compare_log", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)