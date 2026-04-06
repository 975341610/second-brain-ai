"""
# `mcp:meego_upload_attachment`

Upload attachment to meego work item attachment field, the field key is the key of the attachment type field

---

**Parameters Schema:**

{"type":"object","properties":{"field_key":{"type":"string","description":"必填，附件类型字段的 key","properties":{}},"file_path":{"type":"string","description":"必填，要上传的文件路径","properties":{}},"url":{"type":"string","description":"必填，Work item links, 必须满足格式https://meego.larkoffice.com|meego.feishu.cn|project.feishu.cn/{simpleName}/{workItemType}/detail/{workItemId} 的格式，否则拒绝访问","properties":{}}},"required":["url","field_key","file_path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_upload_attachment", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)