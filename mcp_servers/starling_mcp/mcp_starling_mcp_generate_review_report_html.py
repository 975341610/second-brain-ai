"""
# `mcp:Starling_MCP_generate_review_report_html`

Generate an HTML report for reviewing translation recommendations

---

**Parameters Schema:**

{"type":"object","properties":{"namespaceId":{"type":"number","description":"Starling Namespace ID","properties":{}},"projectId":{"type":"number","description":"Starling Project ID","properties":{}},"translations":{"type":"array","description":"The translation data to generate report from","properties":{},"items":{"type":"object","properties":{"key":{"type":"string","properties":{}},"recommend_translation":{"type":"string","properties":{}},"source_text":{"type":"string","properties":{}},"starling_translation":{"type":"string","properties":{}},"text_context":{"type":"string","properties":{}}},"required":["key","source_text","recommend_translation","text_context"]}}},"required":["translations"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="Starling_MCP", tool_name="mcp:Starling_MCP_generate_review_report_html", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)