"""
# `mcp:meego_create_work_item_from_file`

从JSON文件中读取参数并创建工作项，仅支持单个创建。文件中应包含与create_work_item工具参数相同的JSON格式，包含simple_name和work_items字段，文件必须是一个标准json，其中不要包含任何转义字符。

---

**Parameters Schema:**

{"type":"object","properties":{"file_path":{"type":"string","description":"必填，JSON文件路径，文件内容应符合创建工作项的格式要求","properties":{}}},"required":["file_path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_create_work_item_from_file", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)