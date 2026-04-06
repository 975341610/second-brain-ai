"""
# `mcp:a_map_maps_direction_driving`

驾车路径规划 API 可以根据用户起终点经纬度坐标规划以小客车、轿车通勤出行的方案，并且返回通勤方案的数据。

---

**Parameters Schema:**

{"type":"object","properties":{"destination":{"type":"string","description":"目的地经度，纬度，坐标格式为：经度，纬度","properties":{}},"origin":{"type":"string","description":"出发点经度，纬度，坐标格式为：经度，纬度","properties":{}}},"required":["origin","destination"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="a_map", tool_name="mcp:a_map_maps_direction_driving", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)