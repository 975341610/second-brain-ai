"""
# `mcp:SlardarApp_autofix_get_issue_ios_lib_info`

获取一个iOS event中的调用栈中某一个非系统栈帧的git信息，返回data.git_info.url 为对应栈帧方法对应的git链接（eg：https://code.byted.org/ugc-android/HighPerformanceView/blame/cb15bc79b088d523bc74a1e3ad47455c71170311//library/src/main/java/com/bytedance/highperformanceview/layout/MeasureOnceRelativeLayout2.java#L1114）仓库名：ugc-android/HighPerformanceView CommitID：cb15bc79b088d523bc74a1e3ad47455c71170311

---

**Parameters Schema:**

{"type":"object","properties":{"commit_id":{"type":"string","properties":{}},"file_name":{"type":"string","properties":{}},"file_path":{"type":"string","properties":{}},"lib_name":{"type":"string","properties":{}},"line":{"type":"string","description":"栈帧对应文件行号，例如：24","properties":{}},"slardar_link":{"type":"string","properties":{},"format":"uri"}},"required":["slardar_link","commit_id","file_name","file_path","lib_name","line"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_autofix_get_issue_ios_lib_info", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)