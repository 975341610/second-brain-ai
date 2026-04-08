"""
# `mcp:lark_lark_inline_comment`

post an inline (block-anchored) comment to a specific paragraph in a lark docx document

---

**Parameters Schema:**

{"type":"object","properties":{"anchor_text":{"type":"string","description":"要评论的目标段落的原文片段（逐字引用，越精确越好）。工具会自动在文档中搜索最匹配的段落并将评论锚定到对应 block。block_id 与 anchor_text 至少填一个。","properties":{}},"block_id":{"type":"string","description":"可选。若已知目标段落的 block_id 可直接填写，跳过文本搜索。block_id 与 anchor_text 至少填一个。","properties":{}},"comment":{"type":"string","description":"必填。评论正文。支持普通文本、@用户（邮箱形式如 @user@bytedance.com）、飞书文档链接（链接会渲染为可点击链接）。","properties":{}},"document_url":{"type":"string","description":"必填，飞书文档完整链接，例如：https://bytedance.larkoffice.com/docx/TIPddm2mLog88Sxeq7JccYL3nJh","properties":{}}},"required":["document_url","anchor_text","block_id","comment"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_lark_inline_comment", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)