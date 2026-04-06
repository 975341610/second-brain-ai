"""
# `mcp:bits_workflow_bits_get_all_related_crs`

根据 Bits 的 MR URL，获取对应的 Code Review 信息
- 支持多仓 MR
- 可以获取到涉及代码仓库、涉及分支、commit （source commit + base）等
- Bits MR URL 格式: @https://bits.bytedance.net/devops/1500033282/code/detail/7447158?...

---

**Parameters Schema:**

{"type":"object","properties":{"crUrl":{"type":"string","description":"MR 的 URL","properties":{},"format":""}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="bits_workflow", tool_name="mcp:bits_workflow_bits_get_all_related_crs", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)