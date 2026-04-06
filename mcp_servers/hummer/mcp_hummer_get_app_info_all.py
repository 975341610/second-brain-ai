"""
# `mcp:hummer_get_app_info_all`

获取可查询的安卓应用信息，返回appId，appName，packageName

---

**Parameters Schema:**

{"type":"object","properties":{}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="hummer", tool_name="mcp:hummer_get_app_info_all", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)