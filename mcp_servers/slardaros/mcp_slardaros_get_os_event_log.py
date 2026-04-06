"""
# `mcp:SlardarOS_get_os_event_log`

获取os上报异常聚类问题issue下某个event上报时的原始日志

---

**Parameters Schema:**

{"type":"object","properties":{"device_id":{"type":"string","description":"设备did","properties":{}},"event_id":{"type":"string","description":"事件event_id","properties":{}},"event_type":{"type":"string","description":"事件类型","properties":{}},"slardar_os_link":{"type":"string","description":"SlardarOS issue链接, 以https://slardar.bytedance.net/node/os_detail/issue开头, 或者以 https://t.wtturl.cn/开头的短链接","properties":{},"format":"uri"}},"required":["slardar_os_link","event_id","device_id","event_type"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarOS", tool_name="mcp:SlardarOS_get_os_event_log", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)