"""
# `mcp:lark_lark_global_comment`

post a global comment to a specified lark document

---

**Parameters Schema:**

{"type":"object","properties":{"comment":{"type":"string","description":"必填。评论正文，支持 Markdown。建议格式：\n- 普通文本段落，不要过长；\n- 若需引用文档，请直接粘贴完整链接（支持 /docx/、/docs/、/sheet/、/sheets/、/wiki/、/base/）；\n- 若需 @ 人员，请使用邮箱形式，例如：@username.123@bytedance.com；\n- 可使用列表、引用块、代码块等 Markdown 语法；\n工具会自动按顺序提取【文本段、链接、@人员】形成 segments，用于后续请求拼装。","properties":{}},"document_url":{"type":"string","description":"必填，要更新的飞书文档完整链接，比如：https://bytedance.larkoffice.com/docx/TIPddm2mLog88Sxeq7JccYL3nJh","properties":{}}},"required":["document_url","comment"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_lark_global_comment", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)