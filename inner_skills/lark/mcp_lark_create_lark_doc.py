"""
# `mcp:lark_create_lark_doc`

Create a Lark document based on a Markdown file (.lark.md), whenever possible, prioritize using .lark.md files, the .lark.md file content must strictly follow Feishu/lark specific rules, as list in Lark Markdown Formatting. Do not call this tool multiple times in a single task. This will return a Lark/Feishu link, they are the actual final Lark/Feishu documents. There is no need to further verify them. By default, documents are saved in the system cloud drive unless the user explicitly requests a specific target location (folder, wiki node, or personal space) or secure label (L1-L4).

---

**Parameters Schema:**

{"type":"object","properties":{"file_path":{"type":"string","description":"必填，文件绝对路径，支持 Markdown文件（.lark.md），比如：/workspace/iris_e7c707a5-ae78-42d0-b045-1882a9f0a4d7/demo.lark.md，注意：1. 禁止填url 2. 尽量优先使用 .lark.md 文件，文件内容必须遵循 Feishu/lark specific rules, as list in Lark Markdown Formatting","properties":{}},"secure_label":{"type":"string","description":"可选，文档密级：L1（公开）、L2（内部）、L3（保密）、L4（机密）","properties":{}},"target_location":{"type":"string","description":"可选，目标位置的 token，可以是文件夹 token 或 wiki 节点 token。target_type 为 folder 或 wiki 时必填","properties":{}},"target_type":{"type":"string","description":"可选，目标类型：personal（转移到用户个人空间）、folder（移动到指定文件夹）、wiki（移动到指定知识空间节点）。不填则文档保留在系统云盘中","properties":{}},"title":{"type":"string","description":"必填，文档标题。注意：1. 标题中务必不要包含用户的名字 2. 标题避免冗长 3. 在标题中减少使用括号、冒号等，最多使用一次 4. 标题中不要包含额外说明","properties":{}}},"required":["file_path","title"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark", tool_name="mcp:lark_create_lark_doc", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)