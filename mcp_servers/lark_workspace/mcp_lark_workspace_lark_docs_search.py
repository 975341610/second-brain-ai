"""
# `mcp:lark_workspace_lark_docs_search`

Perform a semantic search within the user's self-authored Lark documents (飞书文档) only. Do not use `browser_goto_and_extraction` for internal Lark content due to permissions; this tool returns document passages directly. Use a single high-quality natural language query, not disjoint keywords.

---

**Parameters Schema:**

{"type":"object","properties":{"create_time":{"type":"object","description":"optional, 文档创建时间范围，包含开始(start)/结束(end)，均为时间字符串。格式: YYYY-MM-DD HH:MM:SS；示例: start=\"2025-01-01 00:00:00\", end=\"2025-12-31 23:59:59\"。","properties":{"end":{"type":"string","description":"时间字符串，格式: YYYY-MM-DD HH:MM:SS","properties":{}},"start":{"type":"string","description":"时间字符串，格式: YYYY-MM-DD HH:MM:SS","properties":{}}},"required":["start","end"]},"owner_emails":{"type":"array","description":"optional, 文档所有者邮箱列表。示例: [\"alice@bytedance.com\", \"bob@bytedance.com\"]。","properties":{},"items":{"type":"string","properties":{}}},"query":{"type":"string","description":"optional, Lark 文档关键词搜索。使用简洁的关键词或短语匹配标题与摘要。示例: \"Codebase CI webshell\", \"发布流程 模板 回退\"。禁止包含指令性谓词（如：请搜索/告诉我）。若 query 为空，则仅根据其他条件（owner_emails/create_time）获取文档。","properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_workspace", tool_name="mcp:lark_workspace_lark_docs_search", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)