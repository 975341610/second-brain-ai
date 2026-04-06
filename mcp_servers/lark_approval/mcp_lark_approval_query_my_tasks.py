"""
# `mcp:lark_approval_query_my_tasks`

查询待我审批的审批任务列表（审批人是当前用户，默认近30天，任务状态默认 PENDING）。若返回列表中存在 instance_external_id 不为空的任务，代表为第三方审批单，需要使用 instance_external_id 查询第三方工单详情。

---

**Parameters Schema:**

{"type":"object","properties":{"page_size":{"type":"integer","description":"optional, 分页大小，范围 5~200，默认 10","properties":{}},"page_token":{"type":"string","description":"optional, 分页 token，第一次请求可不填","properties":{}},"start_time_from":{"type":"string","description":"optional, 任务开始时间（按 task.start_time 过滤），支持 YYYY-MM-DD 或 YYYY-MM-DD HH:mm:ss。start_time_to 为空时默认取当前时间；start_time_from 为空时默认按 end-30d 推导。","properties":{}},"start_time_to":{"type":"string","description":"optional, 任务结束时间（按 task.start_time 过滤），支持 YYYY-MM-DD 或 YYYY-MM-DD HH:mm:ss。start_time_to 为空时默认取当前时间；start_time_from 为空时默认按 end-30d 推导。","properties":{}},"task_status":{"type":"string","description":"optional, 任务状态，如 PENDING/REJECTED/APPROVED/TRANSFERRED/DONE/RM_REPEAT/PROCESSED/ALL。默认 PENDING","properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_approval", tool_name="mcp:lark_approval_query_my_tasks", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)