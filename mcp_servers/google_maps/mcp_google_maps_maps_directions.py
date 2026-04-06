"""
# `mcp:google_maps_maps_directions`

Get directions between two points

---

**Parameters Schema:**

{"type":"object","properties":{"destination":{"type":"string","description":"Ending point address or coordinates","properties":{}},"mode":{"type":"string","description":"Travel mode (driving, walking, bicycling, transit)","enum":["driving","walking","bicycling","transit"],"properties":{}},"origin":{"type":"string","description":"Starting point address or coordinates","properties":{}}},"required":["origin","destination"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="google_maps", tool_name="mcp:google_maps_maps_directions", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)