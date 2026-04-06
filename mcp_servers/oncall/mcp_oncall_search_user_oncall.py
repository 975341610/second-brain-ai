"""
# `mcp:oncall_search_user_oncall`

查询指定用户相关的OnCall数据，用户名称、开始时间和结束时间为必填参数，返回用户创建的oncall列表和用户参与但非用户创建的oncall列表，默认获取GPT总结（仅已解决且有权限的OnCall支持），结果导出为xlsx，最大查询10000条记录。

---

**Parameters Schema:**

{"type":"object","properties":{"end_time":{"type":"string","description":"结束时间，格式：YYYY-MM-DD HH:mm，必填","properties":{}},"limit_record_num":{"type":"integer","description":"填写最多需要获取的记录数目。默认是2000，上限是10000","properties":{}},"start_time":{"type":"string","description":"开始时间，格式：YYYY-MM-DD HH:mm，必填","properties":{}},"username":{"type":"string","description":"用户名，英文，可通过邮箱前缀获取，必填","properties":{}}},"required":["username","start_time","end_time"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="oncall", tool_name="mcp:oncall_search_user_oncall", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)