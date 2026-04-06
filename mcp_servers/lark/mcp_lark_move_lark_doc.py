"""
# `mcp:lark_move_lark_doc`

批量迁移已有飞书文档到指定目录（文件夹、知识空间节点或用户个人空间）。如果文档所有者是系统账号（aime），会自动先转移所有权给用户再执行后续操作。Move existing Lark documents to a specified folder, wiki node, or user's personal space in batch.

---

**Parameters Schema:**

{"type":"object","properties":{"document_urls":{"type":"array","description":"必填，待迁移的飞书文档 URL 列表，如 [\"https://bytedance.larkoffice.com/docx/xxx\", \"https://bytedance.larkoffice.com/sheets/yyy\"]","properties":{},"items":{"type":"string","properties":{}}},"target_location":{"type":"string","description":"可选，目标位置的 token。target_type 为 folder 时填文件夹 token，为 wiki 时填知识空间节点 token，为 personal 时不需要填","properties":{}},"target_type":{"type":"string","description":"必填，目标类型：personal（转移到用户个人空间）、folder（移动到指定文件夹）、wiki（移动到指定知识空间节点）","properties":{}}},"required":["document_urls","target_type"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_move_lark_doc", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)