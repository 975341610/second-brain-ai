"""
# `mcp:a_map_maps_distance`

距离测量 API 可以测量两个经纬度坐标之间的距离,支持驾车、步行以及球面距离测量

---

**Parameters Schema:**

{"type":"object","properties":{"destination":{"type":"string","description":"终点经度，纬度，坐标格式为：经度，纬度","properties":{}},"origins":{"type":"string","description":"起点经度，纬度，可以传多个坐标，使用竖线隔离，比如120,30|120,31，坐标格式为：经度，纬度","properties":{}},"type":{"type":"string","description":"距离测量类型,1代表驾车距离测量，0代表直线距离测量，3步行距离测量","properties":{}}},"required":["origins","destination"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="a_map", tool_name="mcp:a_map_maps_distance", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)