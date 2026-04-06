"""
# `mcp:SlardarApp_set_issue_assign_manager`

设置issue处理人

---

**Parameters Schema:**

{"type":"object","properties":{"aid":{"type":"number","description":"可能是一个唯一的数字标识，用于标识特定的问题或实体","properties":{}},"comment_content":{"type":"string","description":"针对问题的评论内容，可为空字符串","properties":{}},"crash_type":{"type":"string","description":"崩溃的类型信息，说明问题是何种崩溃情况","properties":{}},"detail_url":{"type":"string","description":"指向问题详细信息的 URL 链接","properties":{},"format":"uri"},"issue_id":{"type":"string","description":"问题的唯一标识符，用于精确识别特定问题","properties":{}},"issue_level":{"type":"number","description":"问题的严重级别，以数字表示","properties":{}},"issue_title":{"type":"string","description":"问题的标题，概括性地描述问题的内容","properties":{}},"managers":{"type":"array","description":"负责该问题的管理人员列表，成员为字符串形式的姓名","properties":{},"items":{"type":"string","properties":{}}},"op_user":{"type":"string","description":"执行操作的用户姓名","properties":{}},"os":{"type":"string","description":"操作系统的名称，表明问题发生所在的操作系统","properties":{}},"region":{"type":"string","description":"表示问题发生的区域，以代码形式呈现","properties":{}},"sdk":{"type":"boolean","description":"指示是否使用了特定的软件开发工具包，布尔值表示使用或未使用","properties":{}},"sub_issue_id":{"type":"string","description":"子问题的唯一标识符，若不存在子问题则为空字符串","properties":{}}},"required":["aid","os","region","sdk","crash_type","issue_id","issue_title","managers","issue_level","sub_issue_id","comment_content","op_user","detail_url"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_set_issue_assign_manager", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)