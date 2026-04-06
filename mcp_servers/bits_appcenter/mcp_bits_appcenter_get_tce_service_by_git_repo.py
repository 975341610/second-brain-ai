"""
# `mcp:Bits-AppCenter_get_tce_service_by_git_repo`

通过代码仓库查询关联的TCE服务

---

**Parameters Schema:**

{"type":"object","properties":{"app_env":{"type":"string","description":"app env, prod or ppe_xxx","properties":{}},"repo":{"type":"string","description":"git repo name","properties":{}},"tce_env":{"type":"string","description":"prod or boe","properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="Bits-AppCenter", tool_name="mcp:Bits-AppCenter_get_tce_service_by_git_repo", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)