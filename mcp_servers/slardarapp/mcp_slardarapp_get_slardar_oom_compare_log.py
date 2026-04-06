"""
# `mcp:SlardarApp_get_slardar_oom_compare_log`

获取Java OOM不同版本不同时间段的数据，包括两个时间段的OOM崩溃的基础数据、大对象和小对象列表

---

**Parameters Schema:**

{"type":"object","properties":{"aid":{"type":"number","description":"app在slardar中的唯一标识","properties":{}},"base_app_version":{"type":"string","description":"基础组大版本号","properties":{}},"base_end_time":{"type":"number","description":"基础组结束时间戳","properties":{}},"base_start_time":{"type":"number","description":"基础组开始时间戳","properties":{}},"base_update_version_code":{"type":"number","description":"基础组小版本号","properties":{}},"compare_app_version":{"type":"string","description":"对照组大版本号","properties":{}},"compare_end_time":{"type":"number","description":"对照组结束时间戳","properties":{}},"compare_start_time":{"type":"number","description":"对照组开始时间戳","properties":{}},"compare_update_version_code":{"type":"number","description":"对照组小版本号","properties":{}},"region":{"type":"string","description":"时区","properties":{}}},"required":["aid","base_start_time","compare_start_time","base_end_time","compare_end_time"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_slardar_oom_compare_log", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)