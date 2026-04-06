"""
# `mcp:SlardarApp_get_device_exception_logs`

获取某个设备或者用户在一个时间段内发生的所有异常日志

---

**Parameters Schema:**

{"type":"object","properties":{"aid":{"type":"integer","description":"app的唯一标识符","properties":{}},"did":{"type":"string","description":"设备的唯一标识符。user_id与did只需一个即可。","properties":{}},"end_time":{"type":"integer","description":"结束时间的时间戳。","properties":{}},"os":{"type":"string","description":"操作系统，例如iOS、Android等。","properties":{}},"start_time":{"type":"integer","description":"开始时间的时间戳。","properties":{}},"user_id":{"type":"string","description":"用户的唯一标识符。user_id与did只需一个即可。","properties":{}}},"required":["aid","os","start_time","end_time"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_device_exception_logs", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)