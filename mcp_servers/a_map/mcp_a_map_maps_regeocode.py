"""
# `mcp:a_map_maps_regeocode`

将一个高德经纬度坐标转换为行政区划地址信息

---

**Parameters Schema:**

{"type":"object","properties":{"location":{"type":"string","description":"经纬度","properties":{}}},"required":["location"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="a_map", tool_name="mcp:a_map_maps_regeocode", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)