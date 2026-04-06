"""
# `mcp:SlardarApp_autofix_get_issue_anomaly_flights`

采样异常issue下一定数量的did，查询did在对照组（total_version_a_sample_did_count）、实验组（total_version_b_sample_did_count）的命中情况和对照组（total_version_a_resource）、实验组（total_version_b_resource）的流量差异（流量范围0-1），获取与异常issue强关联的libra ab实验列表

---

**Parameters Schema:**

{"type":"object","properties":{"link":{"type":"string","description":"Slardar的issue链接","properties":{}}},"required":["link"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_autofix_get_issue_anomaly_flights", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)