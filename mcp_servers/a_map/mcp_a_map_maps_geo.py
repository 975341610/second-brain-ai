"""
# `mcp:a_map_maps_geo`

将详细的结构化地址转换为经纬度坐标。支持对地标性名胜景区、建筑物名称解析为经纬度坐标

---

**Parameters Schema:**

{"type":"object","properties":{"address":{"type":"string","description":"待解析的结构化地址信息","properties":{}},"city":{"type":"string","description":"指定查询的城市","properties":{}}},"required":["address"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="a_map", tool_name="mcp:a_map_maps_geo", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)