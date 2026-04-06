"""
# `mcp:lark_resolve_lark_doc_comments`

Mark specified comments as resolved in a Lark document. Use after handling feedback from document comments.

---

**Parameters Schema:**

{"type":"object","properties":{"comment_ids":{"type":"array","description":"必填，要标记为已解决的飞书文档评论 ID 列表","properties":{},"items":{"type":"string","properties":{}}},"document_url":{"type":"string","description":"必填，飞书文档完整链接，比如：https://bytedance.larkoffice.com/docx/TIPddm2mLog88Sxeq7JccYL3nJh","properties":{}}},"required":["document_url","comment_ids"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_resolve_lark_doc_comments", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)