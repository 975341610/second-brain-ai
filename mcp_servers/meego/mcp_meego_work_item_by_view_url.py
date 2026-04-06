"""
# `mcp:meego_work_item_by_view_url`

通过Meego视图URL获取全量的工作项列表，支持四种视图类型：1. 全景视图(multiProjectView)：获取跨空间的工作项 2. Story视图(storyView)：获取需求列表 3. Issue视图(issueView)：获取缺陷列表 4. 自定义工作项视图(workObjectView)：获取指定类型的工作项。重要提示：如果链接符合上述视图URL格式，必须调用本工具获取workitem，不要调用其他工具。当获取meego视图图表类数据时，将会忽略result_file_path参数，并将数据文件和截图等素材存放于当前工作区（pwd）

---

**Parameters Schema:**

{"type":"object","properties":{"end_date":{"type":"string","description":"查询结束日期（仅对甘特图有效），格式为YYYY-MM-DD，默认值为当前日期。","properties":{}},"result_file_path":{"type":"string","description":"工作项查询结果的文件存储路径，必须为一个xlsx文件,例如：view_items_xxx.xlsx。重点注意：如果文件名已存在，会覆盖原文件，尽量避免文件名重名！","properties":{}},"start_date":{"type":"string","description":"查询开始日期（仅对甘特图有效），格式为YYYY-MM-DD，默认值为当前日期的前一个月。","properties":{}},"view_url":{"type":"string","description":"工作项视图的URL，支持以下四种格式：1. 全景视图：https://meego.larkoffice.com|project.feishu.cn/{simpleName}/multiProjectView/{viewId} 2. Story视图：https://meego.larkoffice.com|project.feishu.cn/{simpleName}/storyView/{viewId} 3. Issue视图：https://meego.larkoffice.com|project.feishu.cn/{simpleName}/issueView/{viewId} 4. 自定义工作项视图：https://meego.larkoffice.com|project.feishu.cn/{simpleName}/workObjectView/{workItemType}/{viewId}。","properties":{}}},"required":["view_url","result_file_path","start_date","end_date"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_work_item_by_view_url", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)