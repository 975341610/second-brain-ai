"""
# `mcp:google_maps_maps_place_details`

Get detailed information about a specific place

---

**Parameters Schema:**

{"type":"object","properties":{"place_id":{"type":"string","description":"The place ID to get details for","properties":{}}},"required":["place_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="google_maps", tool_name="mcp:google_maps_maps_place_details", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)