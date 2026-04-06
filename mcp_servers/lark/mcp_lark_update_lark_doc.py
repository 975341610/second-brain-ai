"""
# `mcp:lark_update_lark_doc`

Update an existing Lark document by modifying specific blocks. Existing blocks are wrapped with <!-- BLOCK_N | block_id --> and <!-- END_BLOCK_N --> markers, while new content for insert operations is raw content without any block markers. For insert operations, new content is inserted AFTER the specified block's END marker (<!-- END_BLOCK_N -->). Supports update (modify content or delete when content is empty) and insert operations.

---

**Parameters Schema:**

{"type":"object","properties":{"document_url":{"type":"string","description":"必填，要更新的飞书文档完整链接，比如：https://bytedance.larkoffice.com/docx/TIPddm2mLog88Sxeq7JccYL3nJh","properties":{}},"markdown_file_path":{"type":"string","description":"选填，修改内容来源的 Markdown 文件路径，用于处理图片等相对路径资源","properties":{}},"modifications":{"type":"array","description":"必填，block 修改列表。支持 update（更新/删除）和 insert（插入）两种操作","properties":{},"items":{"type":"object","properties":{"block_id":{"type":"string","description":"必填，飞书 block 的真实 ID，对应 \u003c!-- BLOCK_1 | xxx --\u003e 中的 xxx 部分","properties":{}},"block_number":{"type":"string","description":"必填，block 标识，格式如 BLOCK_1，对应下载文档时生成的 \u003c!-- BLOCK_1 | xxx --\u003e 中的标识，insert 类型时可使用 BLOCK_BEGIN 表示在文档最开始插入","properties":{}},"content":{"type":"string","description":"修改后的内容，遵循 Lark Markdown 格式。update 类型：content 不为空时更新内容，content 为空时删除该 block；insert 类型：必填","properties":{}},"modification_type":{"type":"string","description":"必填，修改类型：update（更新该 block 内容，content 为空时表示删除）、insert（在该 block 的 END 标记后插入新内容，即 \u003c!-- END_BLOCK_N --\u003e 之后）","properties":{}}},"required":["block_number","block_id","content","modification_type"]}}},"required":["document_url","modifications","markdown_file_path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_update_lark_doc", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)