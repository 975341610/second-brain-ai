"""
# `mcp:meego_download_attachment`

Download attachment from meego work item details, the uuid is from work item details and in attachment list, e.g: vZyAVRtAS0aBYZdaimkDry9-feGpyjo8CuLiyL2vrwGv11yy6DfeuO4BmBRmS-NFDEuJzyiOD4RftcrpGfie0SWoJ9IcDlVJwXlf38iQqMI=

---

**Parameters Schema:**

{"type":"object","properties":{"attachment_uuid":{"type":"string","description":"必填，附件UUID，通过工作项详情接口获取","properties":{}},"file_name":{"type":"string","description":"必填，下载到本地的文件名","properties":{}},"url":{"type":"string","description":"必填，Work item links, 必须满足格式https://meego.larkoffice.com|meego.feishu.cn|project.feishu.cn/{simpleName}/{workItemType}/detail/{workItemId} 的格式，否则拒绝访问","properties":{}}},"required":["url","attachment_uuid","file_name"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_download_attachment", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)