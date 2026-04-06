"""
# `mcp:SlardarApp_get_alog_content`

根据用户提供的时间范围、设备 ID/用户 ID、应用 ID、操作系统、地域等信息，获取指定设备/用户某个时间段内的 alog 日志内容

---

**Parameters Schema:**

{"type":"object","properties":{"aid":{"type":"integer","description":"应用ID","properties":{}},"device_id":{"type":"string","description":"设备ID，和用户ID二选一即可，同时传递时优先取用设备ID，设备ID和用户ID不可同时为空","properties":{}},"end_time":{"type":"integer","description":"需要获取的日志的结束时间，以秒为精度的时间戳，保留整数","properties":{}},"os":{"type":"string","description":"操作系统，目前仅支持 iOS 或 Android","properties":{}},"region":{"type":"string","description":"地域，目前仅支持 cn","properties":{}},"start_time":{"type":"integer","description":"需要获取的日志的起始时间，以秒为精度的时间戳，保留整数","properties":{}},"user_id":{"type":"string","description":"用户ID，和设备ID二选一即可，同时传递时优先取用设备ID，设备ID和用户ID不可同时为空","properties":{}}},"required":["start_time","end_time","aid","os","region"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_alog_content", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)