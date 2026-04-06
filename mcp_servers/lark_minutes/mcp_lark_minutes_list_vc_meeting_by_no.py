"""
# `mcp:lark_minutes_list_vc_meeting_by_no`

根据飞书视频会议号查询历史会议记录。会议号为 9 位数字，例如：962064997；也可从会议链接中提取，链接格式如 vc.larkoffice.com/j/962064997。start_time 和 end_time 为必填，时间为 unix 时间戳（秒）。

---

**Parameters Schema:**

{"type":"object","properties":{"end_time":{"type":"string","description":"必填，查询结束时间，unix 时间戳（秒）","properties":{}},"meeting_no":{"type":"string","description":"必填，9 位数字会议号，例如：962064997","properties":{}},"page_size":{"type":"integer","description":"可选，分页大小，默认 20","properties":{}},"page_token":{"type":"string","description":"可选，分页 token，首次请求不填","properties":{}},"start_time":{"type":"string","description":"必填，查询开始时间，unix 时间戳（秒）","properties":{}}},"required":["meeting_no","start_time","end_time","page_token","page_size"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_minutes", tool_name="mcp:lark_minutes_list_vc_meeting_by_no", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)