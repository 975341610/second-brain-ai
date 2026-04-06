"""
# `mcp:lark_approval_query_instances`

查询我发起的审批单

---

**Parameters Schema:**

{"type":"object","properties":{"instance_status":{"type":"string","description":"optional, 审批实例状态，如 PENDING/APPROVED/REJECTED/CANCELED/ALL。默认 PENDING，如果不设置的话，查询的是ALL","properties":{}},"start_time_from":{"type":"string","description":"optional, 查询开始时间，支持 YYYY-MM-DD 或 YYYY-MM-DD HH:mm:ss。start_time_to 为空时默认取当前时间；start_time_from 为空时默认按 end-7d 推导。","properties":{}},"start_time_to":{"type":"string","description":"optional, 查询结束时间，支持 YYYY-MM-DD 或 YYYY-MM-DD HH:mm:ss。start_time_to 为空时默认取当前时间。若仅设置 start_time_to，将自动按 end-7d 推导 start_time_from。","properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_approval", tool_name="mcp:lark_approval_query_instances", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)