"""
# `mcp:lark_sheets_update_lark_update_sheet`

Update a specific sheet within Lark spreadsheet from a source xlsx: align rows/cols then batch update cell ranges

---

**Parameters Schema:**

{"type":"object","properties":{"document_url":{"type":"string","description":"必填，待更新的飞书表格链接","properties":{}},"sheet_name":{"type":"string","description":"必填，工作表名称","properties":{}},"source_file_path":{"type":"string","description":"必填，源xlsx文件绝对路径","properties":{}}},"required":["document_url","sheet_name","source_file_path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_sheets_update", tool_name="mcp:lark_sheets_update_lark_update_sheet", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)