"""
# `mcp:codebase_GetUserStatistics`

Get user statistics for a specific user.
It returns the statistics information of the specified user.

---

**Parameters Schema:**

{"type":"object","properties":{"NaturalYear":{"type":"integer","description":"Optional. Natural year to fetch statistics for. Data available only from 2022 onwards.","properties":{}},"RelativeDays":{"type":"integer","description":"Optional. Relative time range in days to fetch statistics for. Enum values: 7 / 30 / 180 / 365. Defaults to 365 if both RelativeDays and NaturalYear are not provided.","properties":{}},"UserId":{"type":"string","description":"Optional. ID of the user to fetch statistics for. Returns self if both Id and Username are empty.","properties":{}},"Username":{"type":"string","description":"Optional. Username of the user to fetch statistics for. Returns self if both Id and Username are empty.","properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="mcp:codebase_GetUserStatistics", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)