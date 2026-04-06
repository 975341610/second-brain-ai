"""
# `mcp:lark_workspace_wiki_tree`

获取飞书文档的/wiki树结构，返回文档所属的/wiki树结构，用于查询指定wiki文档所相邻和相关的/wiki文档，如果wiki不存在子节点，则只会返回父节点和相邻节点，如果一个wiki文档内容为空，通常意味着该文档是一个/wiki节点，包含子文档或邻节点，而不是一个具体的/wiki文档，同时注意'目录节点'本身一般不包含文本内容，需要再次调用本工具获取目录节点下的子节点

---

**Parameters Schema:**

{"type":"object","properties":{"document_url":{"type":"string","description":"required, lark wiki url, example: https://bytedance.larkoffice.com/wiki/xxxxx","properties":{}}},"required":["document_url"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_workspace", tool_name="mcp:lark_workspace_wiki_tree", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)