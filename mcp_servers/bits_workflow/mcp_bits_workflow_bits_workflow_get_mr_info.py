"""
# `mcp:bits_workflow_bits_workflow_get_mr_info`

通过给定一个 bits CR 的 URL（参数），可以该 tool 获取 MR 的详细信息，包括：
    - 涉及代码仓库
    - 涉及分支、commit （source commit + base）
    - 等

---

**Parameters Schema:**

{"type":"object","properties":{"crUrl":{"type":"string","description":"CR 的 URL","properties":{},"format":""}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="bits_workflow", tool_name="mcp:bits_workflow_bits_workflow_get_mr_info", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)