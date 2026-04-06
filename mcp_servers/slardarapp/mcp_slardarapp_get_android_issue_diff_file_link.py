"""
# `mcp:SlardarApp_get_android_issue_diff_file_link`

这是一个获取diff文件链接的mcp，用来获取获取引入崩溃的版本或者是引入崩溃的bits打包链接跟未出现崩溃的版本或者未崩溃的bits打包链接的diff文件在tos上的链接， 通过提供以下参数：issue_link、bits_app_id、base_update_version(未出现崩溃的版本号)、compare_update_version(崩溃版本的版本号)、base_bits_url(未出现崩溃的bits打包链接)、compare_bits_url(崩溃的bits打包链接)，可以获diff文件在tos上的链接。

---

**Parameters Schema:**

{"type":"object","properties":{"base_update_version":{"type":"integer","description":"引入崩溃的小版本号","properties":{}},"compare_update_version":{"type":"integer","description":"引入崩溃的小版本号","properties":{}},"end_time":{"type":"integer","description":"崩溃的结束时间","properties":{}},"issue_link":{"type":"string","description":"Slardar issue链接, 以https://slardar.bytedance.net/或者https://t.wtturl.cn开始的完整URL","properties":{},"format":"uri"},"start_time":{"type":"integer","description":"崩溃的起始时间","properties":{}}},"required":["issue_link","base_update_version","compare_update_version"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_android_issue_diff_file_link", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)