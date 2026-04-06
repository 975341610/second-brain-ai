"""
# `mcp:a_map_maps_text_search`

关键词搜，根据用户传入关键词，搜索出相关的POI

---

**Parameters Schema:**

{"type":"object","properties":{"city":{"type":"string","description":"查询城市","properties":{}},"keywords":{"type":"string","description":"搜索关键词","properties":{}},"types":{"type":"string","description":"POI类型，比如加油站","properties":{}}},"required":["keywords"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="a_map", tool_name="mcp:a_map_maps_text_search", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)