"""
# `mcp:bits_workflow_bits_workflow_get_mr_info`

Retrieve MR detailed information by a Bits MR URL (only use this tool when the URL strictly follows the format: https://bits.bytedance.net/devops/{project_id}/code/detail/{cr_id}), including associated code repositories, branches, commits, and other data.

---

**Parameters Schema:**

{"type":"object","properties":{"crUrl":{"type":"string","description":"CR 的 URL","properties":{},"format":""}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:bits_workflow_bits_workflow_get_mr_info", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)