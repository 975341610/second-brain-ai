"""
# `mcp:devmind_query_metric_story`

Query the specific metric story

---

**Parameters Schema:**

{"type":"object","properties":{"analysis_metric_story":{"type":"string","description":"The analysis metric story for generating visual analytical charts extracted from the user's input prompt. 只要相关的指标故事，不需要其他的描述类似时间用户人等的分词","properties":{}},"raw_query":{"type":"string","description":"用户输入的prompt的原生输入，来源于模版参数raw_query，原封不动的取给我，不需要做任何改动。The raw query of the public data model to query, extract the user's prompt (raw_query) exactly as it is, no modifications of any kind are needed.","properties":{}},"task_id":{"type":"string","description":"The task id to save chart analyse result, 必填","properties":{}}},"required":["task_id","raw_query","analysis_metric_story"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_query_metric_story", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)