"""
# `mcp:devmind_query_analysis_dimension`

Query the specific analysis dimension related to the user

---

**Parameters Schema:**

{"type":"object","properties":{"analysis_dimension":{"type":"string","description":"The analysis dimension for generating visual analytical charts extracted from the user's input prompt, include time dimension","properties":{}},"analysis_metric":{"type":"string","description":"The analysis metric for generating visual analytical charts extracted from the user's input prompt","properties":{}},"filter_condition":{"type":"string","description":"The filtering conditions for generating visual analytical charts extracted from the user's input prompt, include time condition dimension","properties":{}},"model_id":{"type":"string","description":"The ID of the data model to query","properties":{}}},"required":["model_id","analysis_metric","analysis_dimension","filter_condition"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_query_analysis_dimension", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)