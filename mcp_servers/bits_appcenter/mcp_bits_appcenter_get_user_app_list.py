"""
# `mcp:Bits-AppCenter_get_user_app_list`

获取用户名下的app列表，如果用户名下没有应用，输出一个链接，提示用户去创建：https://bits.bytedance.net/app_center/rollout/app/create

---

**Parameters Schema:**

{"type":"object","properties":{"username":{"type":"string","description":"username to query app list may left empty will use current user","properties":{}}},"required":["username"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="Bits-AppCenter", tool_name="mcp:Bits-AppCenter_get_user_app_list", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)