"""
# `mcp:SlardarApp_get_event_log`

获取issue下某个event上报时的原始日志，支持获取指定json path的值。

---

**Parameters Schema:**

{"type":"object","properties":{"json_paths":{"type":"array","description":"List of JSON path strings to extract specific fields","properties":{},"items":{"type":"string","description":"A single JSON path expression","properties":{}}},"slardar_link":{"type":"string","description":"The URL link for slardar","properties":{},"format":"uri"}},"required":["slardar_link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_event_log", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)