"""
# `mcp:lark_approval_get_third_party_instance`

获取第三方审批实例详情（仅支持 kani）。请使用 query_my_tasks 返回的 instance_external_id + instance_pc_link 作为入参。

---

**Parameters Schema:**

{"type":"object","properties":{"instance_external_id":{"type":"string","description":"required, 第三方审批实例 ID（来自 query_my_tasks 的 instance_external_id）","properties":{}},"mobile_link":{"type":"string","description":"optional, 第三方审批跳转链接（移动端），用于透传","properties":{}},"pc_link":{"type":"string","description":"required, 第三方审批跳转链接（来自 query_my_tasks 的 instance_pc_link）","properties":{}}},"required":["instance_external_id","pc_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_approval", tool_name="mcp:lark_approval_get_third_party_instance", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)