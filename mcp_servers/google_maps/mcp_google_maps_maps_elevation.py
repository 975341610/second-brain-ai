"""
# `mcp:google_maps_maps_elevation`

Get elevation data for locations on the earth

---

**Parameters Schema:**

{"type":"object","properties":{"locations":{"type":"array","description":"Array of locations to get elevation for","properties":{},"items":{"type":"object","properties":{"latitude":{"type":"number","properties":{}},"longitude":{"type":"number","properties":{}}},"required":["latitude","longitude"]}}},"required":["locations"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="google_maps", tool_name="mcp:google_maps_maps_elevation", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)