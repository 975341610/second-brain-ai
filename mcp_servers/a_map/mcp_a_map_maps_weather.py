"""
# `mcp:a_map_maps_weather`

根据城市名称或者标准adcode查询指定城市的天气

---

**Parameters Schema:**

{"type":"object","properties":{"city":{"type":"string","description":"城市名称或者adcode","properties":{}}},"required":["city"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="a_map", tool_name="mcp:a_map_maps_weather", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)