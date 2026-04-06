"""
# `mcp:SlardarOS_os_get_multi_media_source_repos`

根据用户提供多媒体问题缺陷单对应 rom_version，获取到对媒体领域的源代码仓储列表信息

---

**Parameters Schema:**

{"type":"object","properties":{"rom_version":{"type":"string","description":"缺陷系统版本信息, 是一个OS系统版本的格式,类似 2.0.2.0-20260313-065507-NIGHTLY-user-N1-b799-userroot 这种格式","properties":{}}},"required":["rom_version"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarOS", tool_name="mcp:SlardarOS_os_get_multi_media_source_repos", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)