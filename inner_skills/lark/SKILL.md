# MCP Skill: lark

Lark can do the following things:
- Lark document/sheet/bitable downloader
  * For bitable (multi-dimensional table): only downloads the original table as a single CSV file, without views or other tables. Consider using lark_bitable skill tools for comprehensive bitable analysis.
- Generate a Lark/Feishu document from a markdown file
- Update an existing Lark document by modifying specific blocks. Each block is marked with <!-- BLOCK_N | block_id --> at the start and <!-- END_BLOCK_N --> at the end. Supports update (modify content or delete when content is empty) and insert operations
- Mark specified comments as resolved in a Lark document.
- Convert csv、xlsx、xls files to Lark/Feishu sheets/table or Lark/Feishu Base. (将csv、xlsx、xls文件转换为飞书表格或多维表格)
- Batch move existing Lark documents to a specified folder, wiki node, or user's personal space, with optional secure label setting. Auto-transfers ownership if owned by system account. (批量迁移飞书文档到指定文件夹、知识空间节点或用户个人空间，自动处理系统账号文档的所有权转移)
- Validate template reports in Feishu template scenarios to ensure they meet all template requirements.
- Get Lark user info by extracted user id from email or get all members info of a chat group by chat_id
- Post a global comment to a Lark document
- Post an inline (block-anchored) comment to a specific paragraph in a Lark docx document; automatically locates the target block by matching anchor_text against the document content
- Get current user's avatar and download locally

## Available Tools

### mcp_lark_lark_download
- **Description**: download file from the lark url, save locally, and return file path list, example: ["doc_title_xxx.lark.md", "sheet_title_xxx.xlsx"]
- **Usage**: `python3 inner_skills/lark/mcp_lark_lark_download.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"document_url":{"type":"string","description":"required, lark document/sheet url, example: https://domain.larkoffice.com/docx/CCzFdEVGXoyLpmxxxxxx, https://bytedance.larkoffice.com/sheets/xxxxx?sheet=xxxxx","properties":{}}},"required":["document_url"]}`

### mcp_lark_create_lark_doc
- **Description**: Create a Lark document based on a Markdown file (.lark.md), whenever possible, prioritize using .lark.md files, the .lark.md file content must strictly follow Feishu/lark specific rules, as list in Lark Markdown Formatting. Do not call this tool multiple times in a single task. This will return a Lark/Feishu link, they are the actual final Lark/Feishu documents. There is no need to further verify them. By default, documents are saved in the system cloud drive unless the user explicitly requests a specific target location (folder, wiki node, or personal space) or secure label (L1-L4).
- **Usage**: `python3 inner_skills/lark/mcp_lark_create_lark_doc.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"file_path":{"type":"string","description":"必填，文件绝对路径，支持 Markdown文件（.lark.md），比如：/workspace/iris_e7c707a5-ae78-42d0-b045-1882a9f0a4d7/demo.lark.md，注意：1. 禁止填url 2. 尽量优先使用 .lark.md 文件，文件内容必须遵循 Feishu/lark specific rules, as list in Lark Markdown Formatting","properties":{}},"secure_label":{"type":"string","description":"可选，文档密级：L1（公开）、L2（内部）、L3（保密）、L4（机密）","properties":{}},"target_location":{"type":"string","description":"可选，目标位置的 token，可以是文件夹 token 或 wiki 节点 token。target_type 为 folder 或 wiki 时必填","properties":{}},"target_type":{"type":"string","description":"可选，目标类型：personal（转移到用户个人空间）、folder（移动到指定文件夹）、wiki（移动到指定知识空间节点）。不填则文档保留在系统云盘中","properties":{}},"title":{"type":"string","description":"必填，文档标题。注意：1. 标题中务必不要包含用户的名字 2. 标题避免冗长 3. 在标题中减少使用括号、冒号等，最多使用一次 4. 标题中不要包含额外说明","properties":{}}},"required":["file_path","title"]}`

### mcp_lark_create_lark_table
- **Description**: 将文件转换为飞书表格或多维表格。支持以下格式：(1. 飞书表格(sheets/table)：支持 xlsx、csv、xls 文件 (2. 飞书多维表格(Base)：支持 xlsx、csv 文件。
Convert files to Lark sheets/table or Lark Base. Supported formats: (1. Lark Sheets: supports xlsx, csv, xls files (2. Lark Base: supports xlsx, csv files
- **Usage**: `python3 inner_skills/lark/mcp_lark_create_lark_table.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"file_path":{"type":"string","description":"必填，文件绝对路径，支持多种文件格式：1. xlsx、csv、xls文件转飞书表格；2. xlsx、csv文件转飞书多维表格。比如：/workspace/iris_e7c707a5-ae78-42d0-b045-1882a9f0a4d7/data.csv，注意：1. 禁止填url 2. 文件路径必须真实存在（提前使用命令行工具确认文件路径）","properties":{}},"table_type":{"type":"string","description":"可选，指定转换的目标表格类型，可选值：sheets(电子表格)、base(多维表格)，默认根据文件类型自动选择","properties":{}},"title":{"type":"string","description":"必填，表格标题","properties":{}}},"required":["file_path","title","table_type"]}`

### mcp_lark_move_lark_doc
- **Description**: 批量迁移已有飞书文档到指定目录（文件夹、知识空间节点或用户个人空间）。如果文档所有者是系统账号（aime），会自动先转移所有权给用户再执行后续操作。Move existing Lark documents to a specified folder, wiki node, or user's personal space in batch.
- **Usage**: `python3 inner_skills/lark/mcp_lark_move_lark_doc.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"document_urls":{"type":"array","description":"必填，待迁移的飞书文档 URL 列表，如 [\"https://bytedance.larkoffice.com/docx/xxx\", \"https://bytedance.larkoffice.com/sheets/yyy\"]","properties":{},"items":{"type":"string","properties":{}}},"target_location":{"type":"string","description":"可选，目标位置的 token。target_type 为 folder 时填文件夹 token，为 wiki 时填知识空间节点 token，为 personal 时不需要填","properties":{}},"target_type":{"type":"string","description":"必填，目标类型：personal（转移到用户个人空间）、folder（移动到指定文件夹）、wiki（移动到指定知识空间节点）","properties":{}}},"required":["document_urls","target_type"]}`

### mcp_lark_update_lark_doc
- **Description**: Update an existing Lark document by modifying specific blocks. Existing blocks are wrapped with <!-- BLOCK_N | block_id --> and <!-- END_BLOCK_N --> markers, while new content for insert operations is raw content without any block markers. For insert operations, new content is inserted AFTER the specified block's END marker (<!-- END_BLOCK_N -->). Supports update (modify content or delete when content is empty) and insert operations.
- **Usage**: `python3 inner_skills/lark/mcp_lark_update_lark_doc.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"document_url":{"type":"string","description":"必填，要更新的飞书文档完整链接，比如：https://bytedance.larkoffice.com/docx/TIPddm2mLog88Sxeq7JccYL3nJh","properties":{}},"markdown_file_path":{"type":"string","description":"选填，修改内容来源的 Markdown 文件路径，用于处理图片等相对路径资源","properties":{}},"modifications":{"type":"array","description":"必填，block 修改列表。支持 update（更新/删除）和 insert（插入）两种操作","properties":{},"items":{"type":"object","properties":{"block_id":{"type":"string","description":"必填，飞书 block 的真实 ID，对应 \u003c!-- BLOCK_1 | xxx --\u003e 中的 xxx 部分","properties":{}},"block_number":{"type":"string","description":"必填，block 标识，格式如 BLOCK_1，对应下载文档时生成的 \u003c!-- BLOCK_1 | xxx --\u003e 中的标识，insert 类型时可使用 BLOCK_BEGIN 表示在文档最开始插入","properties":{}},"content":{"type":"string","description":"修改后的内容，遵循 Lark Markdown 格式。update 类型：content 不为空时更新内容，content 为空时删除该 block；insert 类型：必填","properties":{}},"modification_type":{"type":"string","description":"必填，修改类型：update（更新该 block 内容，content 为空时表示删除）、insert（在该 block 的 END 标记后插入新内容，即 \u003c!-- END_BLOCK_N --\u003e 之后）","properties":{}}},"required":["block_number","block_id","content","modification_type"]}}},"required":["document_url","modifications","markdown_file_path"]}`

### mcp_lark_resolve_lark_doc_comments
- **Description**: Mark specified comments as resolved in a Lark document. Use after handling feedback from document comments.
- **Usage**: `python3 inner_skills/lark/mcp_lark_resolve_lark_doc_comments.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"comment_ids":{"type":"array","description":"必填，要标记为已解决的飞书文档评论 ID 列表","properties":{},"items":{"type":"string","properties":{}}},"document_url":{"type":"string","description":"必填，飞书文档完整链接，比如：https://bytedance.larkoffice.com/docx/TIPddm2mLog88Sxeq7JccYL3nJh","properties":{}}},"required":["document_url","comment_ids"]}`

### mcp_lark_lark_user_info
- **Description**: get Lark user info by emails, or get all members info of a chat group by chat_id
- **Usage**: `python3 inner_skills/lark/mcp_lark_lark_user_info.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"chat_id":{"type":"string","description":"optional, chat id, e.g oc_1234567890. either emails or chat_id is required","properties":{}},"emails":{"type":"array","description":"optional, email array, e.g ['zhangsan.001@bytedance.com']. either emails or chat_id is required","properties":{},"items":{"type":"string","properties":{}}}}}`

### mcp_lark_validate_template_report
- **Description**: Validate whether a generated report meets the requirements of a Lark/Feishu document template. This tool is specifically designed for Feishu template scenarios. DO NOT use this tool in technical solution/proposal generation scenarios. It compares the template file and the generated report file to check completeness, structure consistency, placeholder replacement, format correctness, and content quality. Use this tool in the final validation task before creating the Lark document to ensure the report fully satisfies all template requirements. The tool will return detailed validation results including any issues found and suggestions for improvement.
- **Usage**: `python3 inner_skills/lark/mcp_lark_validate_template_report.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"report_path":{"type":"string","description":"必填，生成的报告文件路径 (*.lark.md)","properties":{}},"template_path":{"type":"string","description":"必填，模版文件路径 (*.lark.md)","properties":{}},"validation_round":{"type":"integer","description":"可选，当前是第几轮验证（默认为1）。轮次越高，验证越宽容，避免反复修改","properties":{}}},"required":["report_path","template_path"]}`

### mcp_lark_lark_get_avatar
- **Description**: get current user's Lark avatar url and download locally
- **Usage**: `python3 inner_skills/lark/mcp_lark_lark_get_avatar.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{}}`

### mcp_lark_lark_global_comment
- **Description**: post a global comment to a specified lark document
- **Usage**: `python3 inner_skills/lark/mcp_lark_lark_global_comment.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"comment":{"type":"string","description":"必填。评论正文，支持 Markdown。建议格式：\n- 普通文本段落，不要过长；\n- 若需引用文档，请直接粘贴完整链接（支持 /docx/、/docs/、/sheet/、/sheets/、/wiki/、/base/）；\n- 若需 @ 人员，请使用邮箱形式，例如：@username.123@bytedance.com；\n- 可使用列表、引用块、代码块等 Markdown 语法；\n工具会自动按顺序提取【文本段、链接、@人员】形成 segments，用于后续请求拼装。","properties":{}},"document_url":{"type":"string","description":"必填，要更新的飞书文档完整链接，比如：https://bytedance.larkoffice.com/docx/TIPddm2mLog88Sxeq7JccYL3nJh","properties":{}}},"required":["document_url","comment"]}`

### mcp_lark_lark_inline_comment
- **Description**: post an inline (block-anchored) comment to a specific paragraph in a lark docx document
- **Usage**: `python3 inner_skills/lark/mcp_lark_lark_inline_comment.py '{"param": "value"}'`
- **Schema**: `{"type":"object","properties":{"anchor_text":{"type":"string","description":"要评论的目标段落的原文片段（逐字引用，越精确越好）。工具会自动在文档中搜索最匹配的段落并将评论锚定到对应 block。block_id 与 anchor_text 至少填一个。","properties":{}},"block_id":{"type":"string","description":"可选。若已知目标段落的 block_id 可直接填写，跳过文本搜索。block_id 与 anchor_text 至少填一个。","properties":{}},"comment":{"type":"string","description":"必填。评论正文。支持普通文本、@用户（邮箱形式如 @user@bytedance.com）、飞书文档链接（链接会渲染为可点击链接）。","properties":{}},"document_url":{"type":"string","description":"必填，飞书文档完整链接，例如：https://bytedance.larkoffice.com/docx/TIPddm2mLog88Sxeq7JccYL3nJh","properties":{}}},"required":["document_url","anchor_text","block_id","comment"]}`

