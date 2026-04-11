"""
# `mcp:lark_validate_template_report`

Validate whether a generated report meets the requirements of a Lark/Feishu document template. This tool is specifically designed for Feishu template scenarios. DO NOT use this tool in technical solution/proposal generation scenarios. It compares the template file and the generated report file to check completeness, structure consistency, placeholder replacement, format correctness, and content quality. Use this tool in the final validation task before creating the Lark document to ensure the report fully satisfies all template requirements. The tool will return detailed validation results including any issues found and suggestions for improvement.

---

**Parameters Schema:**

{"type":"object","properties":{"report_path":{"type":"string","description":"必填，生成的报告文件路径 (*.lark.md)","properties":{}},"template_path":{"type":"string","description":"必填，模版文件路径 (*.lark.md)","properties":{}},"validation_round":{"type":"integer","description":"可选，当前是第几轮验证（默认为1）。轮次越高，验证越宽容，避免反复修改","properties":{}}},"required":["report_path","template_path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_validate_template_report", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)