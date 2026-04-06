"""
# `mcp:acha_get_panic_detail`

Get the panic detail of the given issue ID from Acha(定位小助手 https://acha.bytedance.net/)
	The url of the panic detail is: https://acha.bytedance.net/error_info?error_info?error_id={error_id}&env_type={env_type}

---

**Parameters Schema:**

{"type":"object","properties":{"env_type":{"type":"string","description":"Environment type: 'default', 'boecn', 'boei18n' or 'ttp'","properties":{}},"error_id":{"type":"string","description":"The ID of the panic issue to query","properties":{}}},"required":["error_id","env_type"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="acha", tool_name="mcp:acha_get_panic_detail", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)