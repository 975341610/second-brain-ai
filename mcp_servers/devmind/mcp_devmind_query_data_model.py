"""
# `mcp:devmind_query_data_model`

Query the specific public data model

---

**Parameters Schema:**

{"type":"object","properties":{"analysis_dimension":{"type":"string","description":"The analysis dimension for generating visual analytical charts extracted from the user's input prompt, include time dimension","properties":{}},"analysis_metric":{"type":"string","description":"The analysis metric for generating visual analytical charts extracted from the user's input prompt","properties":{}},"analysis_model":{"type":"string","description":"The analysis data model for generating visual analytical charts extracted from the user's input prompt","properties":{}},"filter_condition":{"type":"string","description":"The filtering conditions for generating visual analytical charts extracted from the user's input prompt, include time condition dimension","properties":{}},"raw_query":{"type":"string","description":"用户输入的prompt的原生输入，来源于模版参数raw_query，原封不动的取给我，不需要做任何改动。The raw query of the public data model to query, extract the user's prompt (raw_query) exactly as it is, no modifications of any kind are needed.","properties":{}},"task_id":{"type":"string","description":"The ID of the task to query, 必填","properties":{}}},"required":["raw_query","task_id","analysis_model","analysis_metric","analysis_dimension","filter_condition"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_query_data_model", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)