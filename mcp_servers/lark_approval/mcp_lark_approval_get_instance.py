"""
# `mcp:lark_approval_get_instance`

获取飞书原生审批实例详情（仅支持原生审批）；若为第三方审批实例，请使用 get_third_party_instance。

---

**Parameters Schema:**

{"type":"object","properties":{"instance_id":{"type":"string","description":"required, 审批实例 code（飞书原生审批实例 ID）","properties":{}}},"required":["instance_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_approval", tool_name="mcp:lark_approval_get_instance", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)