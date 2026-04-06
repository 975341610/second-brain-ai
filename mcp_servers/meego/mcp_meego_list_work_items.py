"""
# `mcp:meego_list_work_items`

Query the detailed information of work items, and save the results to a file. This tool supports two query types: 1. Query work items within a specified space and time interval 2. Query the current user's work items within a specified time interval in all spaces. IMPORTANT: This tool CANNOT handle view-related work items, view-based queries, or other conditional queries!!!.

---

**Parameters Schema:**

{"type":"object","properties":{"end_time":{"type":"string","description":"必填，结束时间，格式为yyyy-MM-dd","properties":{}},"result_file_path":{"type":"string","description":"必填，工作项查询结果的文件存储路径，将输出为Excel文件，例如：work_items_xxx.xlsx。重点注意：如果文件名已存在，会覆盖原文件，尽量避免文件名重名！。","properties":{}},"simple_name":{"type":"string","description":"必填，空间名称，如果为空字符串，则查询范围为当前用户的所有空间","properties":{}},"start_time":{"type":"string","description":"必填，开始时间，格式为yyyy-MM-dd，如果用户没指定，建议填三个月前，注意：start_time和end_time的差不要超过一年","properties":{}},"user_email":{"type":"string","description":"选填，指定查询某个用户的工作项","properties":{}},"work_item_types":{"type":"array","description":"必填，工作项类型,枚举可选值可从空间详情中获取，参数示例：[\"story\"]","properties":{},"items":{"type":"string","properties":{}}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_list_work_items", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)