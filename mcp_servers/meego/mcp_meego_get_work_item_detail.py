"""
# `mcp:meego_get_work_item_detail`

get work item detail from meego work item link

---

**Parameters Schema:**

{"type":"object","properties":{"result_file_path":{"type":"string","description":"必填，工作项查询结果的文件存储路径，将输出为markdown 文件，例如：work_item_detail.md。重点注意：如果文件名已存在，会覆盖原文件，尽量避免文件名重名！。","properties":{}},"url":{"type":"string","description":"必填，Work item links, 必须满足格式https://meego.larkoffice.com|meego.feishu.cn|project.feishu.cn/{simpleName}/{workItemType}/detail/{workItemId} 的格式，否则拒绝访问","properties":{}}},"required":["url"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_get_work_item_detail", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)