"""
# `mcp:devmind_manage_favorite`

Create or delete a favorite metric

---

**Parameters Schema:**

{"type":"object","properties":{"status":{"type":"string","description":"Status: '1' to create, '0' to delete","properties":{}},"story_id":{"type":"string","description":"The ID of the story metric to manage","properties":{}}},"required":["story_id","status"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_manage_favorite", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)