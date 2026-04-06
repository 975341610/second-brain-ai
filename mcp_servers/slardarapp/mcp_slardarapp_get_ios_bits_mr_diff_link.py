"""
# `mcp:SlardarApp_get_ios_bits_mr_diff_link`

这是一个获取bits MR变更内容的mcp工具，用来获取合入某个版本的全部mr中的内容diff文件在tos的下载链接

---

**Parameters Schema:**

{"type":"object","properties":{"app_version":{"type":"string","description":"发生崩溃的版本号","properties":{}},"issue_link":{"type":"string","description":"Slardar issue链接, 以https://slardar.bytedance.net/或者https://t.wtturl.cn开始的完整URL","properties":{},"format":"uri"}},"required":["issue_link","app_version"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_ios_bits_mr_diff_link", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)