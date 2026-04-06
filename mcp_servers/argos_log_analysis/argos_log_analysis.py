"""
# `argos_log_analysis`

Argos log analysis tool can do the following things:
1. Get logs through multiple methods: by Log ID only, by Log ID + PSM list, or by PSM + keywords with advanced filtering (include/exclude keywords, case sensitivity, AND/OR logic), etc. Please ensure all necessary information (LogID, PSM, time range, keywords) is provided to avoid query failures.
2. Perform statistical analysis of logs, extract critical error logs, and locate key issues.
3. Associate logs with corresponding source code and provide troubleshooting guidance.

```param="task"
Describe the task you want argos log analysis to complete in natural language.
```


---

**Parameters Schema:**

{"type":"object","properties":{"persona":{"type":"string","description":"The persona of the argos log analysis agent. The description should give out background context and the specific goals, but not detailed datapoints or libraries to use.","properties":{}},"task":{"type":"string","description":"A self contained task prompt that can be completed by the argos log analysis agent. The description should give out background context and the specific goals, but not detailed datapoints or libraries to use.","properties":{}}},"required":["persona","task"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="argos_log_analysis", tool_name="argos_log_analysis", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)