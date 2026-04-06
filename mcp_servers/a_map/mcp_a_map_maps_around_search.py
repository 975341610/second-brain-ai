"""
# `mcp:a_map_maps_around_search`

周边搜，根据用户传入关键词以及坐标location，搜索出radius半径范围的POI

---

**Parameters Schema:**

{"type":"object","properties":{"keywords":{"type":"string","description":"搜索关键词","properties":{}},"location":{"type":"string","description":"中心点经度纬度","properties":{}},"radius":{"type":"string","description":"搜索半径","properties":{}}},"required":["location"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="a_map", tool_name="mcp:a_map_maps_around_search", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)