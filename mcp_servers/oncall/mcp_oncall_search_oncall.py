"""
# `mcp:oncall_search_oncall`

基于租户搜索OnCall数据，支持指定时间范围、租户ID或租户名称，可选获取群聊详情，结果导出为xlsx。租户名称必须准确，系统会自动将租户名称转换为租户ID进行搜索。注意：如果用户提供了OnCall平台的URL链接，请优先使用search_oncall_from_url工具。

---

**Parameters Schema:**

{"type":"object","properties":{"end_time":{"type":"string","description":"结束时间，格式：YYYY-MM-DD HH:mm，如不提供默认为当前时间","properties":{}},"is_solved":{"type":"integer","description":"是否已解决，1-已解决，0-未解决","properties":{}},"limit_record_num":{"type":"integer","description":"填写最多需要获取的记录数目。默认是2000，上限是2000","properties":{}},"need_chat_detail":{"type":"boolean","description":"是否需要获取每个Oncall群聊详情，为true则在搜索工单的同时获取所有群聊详情，默认不获取","properties":{}},"start_time":{"type":"string","description":"开始时间，格式：YYYY-MM-DD HH:mm，如不提供默认为5天前","properties":{}},"tenant_id":{"type":"integer","description":"租户ID，与租户名称二选一","properties":{}},"tenant_name":{"type":"string","description":"租户名称，必须准确，与租户ID二选一。当提供租户名称时，会自动查询对应的租户ID","properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="oncall", tool_name="mcp:oncall_search_oncall", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)