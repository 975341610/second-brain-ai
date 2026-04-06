"""
# `mcp:google_maps_maps_reverse_geocode`

Convert coordinates into an address

---

**Parameters Schema:**

{"type":"object","properties":{"latitude":{"type":"number","description":"Latitude coordinate","properties":{}},"longitude":{"type":"number","description":"Longitude coordinate","properties":{}}},"required":["latitude","longitude"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="google_maps", tool_name="mcp:google_maps_maps_reverse_geocode", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)