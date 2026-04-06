"""
# `mcp:a_map_maps_bicycling`

骑行路径规划用于规划骑行通勤方案，规划时会考虑天桥、单行线、封路等情况。最大支持 500km 的骑行路线规划

---

**Parameters Schema:**

{"type":"object","properties":{"destination":{"type":"string","description":"目的地经纬度，坐标格式为：经度，纬度","properties":{}},"origin":{"type":"string","description":"出发点经纬度，坐标格式为：经度，纬度","properties":{}}},"required":["origin","destination"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="a_map", tool_name="mcp:a_map_maps_bicycling", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)