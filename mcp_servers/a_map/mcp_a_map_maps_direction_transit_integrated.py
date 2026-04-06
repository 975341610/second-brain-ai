"""
# `mcp:a_map_maps_direction_transit_integrated`

公交路径规划 API 可以根据用户起终点经纬度坐标规划综合各类公共（火车、公交、地铁）交通方式的通勤方案，并且返回通勤方案的数据，跨城场景下必须传起点城市与终点城市

---

**Parameters Schema:**

{"type":"object","properties":{"city":{"type":"string","description":"公共交通规划起点城市","properties":{}},"cityd":{"type":"string","description":"公共交通规划终点城市","properties":{}},"destination":{"type":"string","description":"目的地经度，纬度，坐标格式为：经度，纬度","properties":{}},"origin":{"type":"string","description":"出发点经度，纬度，坐标格式为：经度，纬度","properties":{}}},"required":["origin","destination","city","cityd"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="a_map", tool_name="mcp:a_map_maps_direction_transit_integrated", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)