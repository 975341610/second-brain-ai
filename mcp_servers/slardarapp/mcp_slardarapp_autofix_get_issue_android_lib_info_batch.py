"""
# `mcp:SlardarApp_autofix_get_issue_android_lib_info_batch`

批量获取Android 堆栈对应的git信息。
注意：参数stack_lines是字符串数组类型，需要传native堆栈，堆栈中的每一行栈帧都必须包含so名字，不要裁剪

---

**Parameters Schema:**

{"type":"object","properties":{"aid":{"type":"integer","properties":{}},"crash_type":{"type":"string","description":"崩溃类型","properties":{}},"os":{"type":"string","description":"系统：Android or iOS","properties":{}},"region":{"type":"string","description":"所属区域，cn、maliva等","properties":{}},"release_build":{"type":"string","properties":{}},"stack_lines":{"type":"array","description":"需要获取git信息的堆栈，字符串数组类型，传native堆栈","properties":{},"items":{"type":"string","properties":{}}}},"required":["aid","os","region","stack_lines","release_build","crash_type"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_autofix_get_issue_android_lib_info_batch", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)