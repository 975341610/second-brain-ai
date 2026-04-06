"""
# `mcp:okr_okr_get_information`

Get OKR information by URL

---

**Parameters Schema:**

{"type":"object","properties":{"quarter_range":{"type":"string","description":"optional，quarterly range when querying OKRs. Candidates: 'Q1', 'Q2', 'Q3', 'Q4', 'FULL_YEAR', you have no other options besides these","properties":{}},"scope":{"type":"string","description":"required, the scope of okr, which only can be 'Team' or 'Individual'","properties":{}},"url":{"type":"string","description":"optional, the URL containing the OKR information.","properties":{}},"year":{"type":"integer","description":"optional，the year when querying OKR ","properties":{}}},"required":["scope"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="okr", tool_name="mcp:okr_okr_get_information", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)