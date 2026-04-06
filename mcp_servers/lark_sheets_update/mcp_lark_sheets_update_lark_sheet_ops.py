"""
# `mcp:lark_sheets_update_lark_sheet_ops`

Operate lark sheets: create/copy/delete sheet within a spreadsheet by URL

---

**Parameters Schema:**

{"type":"object","properties":{"document_url":{"type":"string","description":"必填，要操作的飞书表格链接，如 https://bytedance.larkoffice.com/sheets/XXX","properties":{}},"index":{"type":"integer","description":"选填，插入位置索引(从0开始)","properties":{}},"operation":{"type":"string","description":"必填，操作类型：create/copy/delete","properties":{}},"source_sheet_name":{"type":"string","description":"选填，复制/删除时的源sheet名称","properties":{}},"title":{"type":"string","description":"选填，新建或复制时的工作表标题","properties":{}}},"required":["document_url","operation","title","index","source_sheet_name"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_sheets_update", tool_name="mcp:lark_sheets_update_lark_sheet_ops", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)