"""
# `mcp:SlardarApp_autofix_get_flight_history`

获取某个libra ab实验的操作历史

---

**Parameters Schema:**

{"type":"object","properties":{"flight_id":{"type":"integer","description":"实验的唯一标识，别名：fid","properties":{}}},"required":["flight_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_autofix_get_flight_history", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)