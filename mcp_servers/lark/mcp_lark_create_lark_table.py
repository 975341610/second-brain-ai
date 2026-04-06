"""
# `mcp:lark_create_lark_table`

将文件转换为飞书表格或多维表格。支持以下格式：(1. 飞书表格(sheets/table)：支持 xlsx、csv、xls 文件 (2. 飞书多维表格(Base)：支持 xlsx、csv 文件。
Convert files to Lark sheets/table or Lark Base. Supported formats: (1. Lark Sheets: supports xlsx, csv, xls files (2. Lark Base: supports xlsx, csv files

---

**Parameters Schema:**

{"type":"object","properties":{"file_path":{"type":"string","description":"必填，文件绝对路径，支持多种文件格式：1. xlsx、csv、xls文件转飞书表格；2. xlsx、csv文件转飞书多维表格。比如：/workspace/iris_e7c707a5-ae78-42d0-b045-1882a9f0a4d7/data.csv，注意：1. 禁止填url 2. 文件路径必须真实存在（提前使用命令行工具确认文件路径）","properties":{}},"table_type":{"type":"string","description":"可选，指定转换的目标表格类型，可选值：sheets(电子表格)、base(多维表格)，默认根据文件类型自动选择","properties":{}},"title":{"type":"string","description":"必填，表格标题","properties":{}}},"required":["file_path","title","table_type"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_create_lark_table", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)