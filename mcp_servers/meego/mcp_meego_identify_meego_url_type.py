"""
# `mcp:meego_identify_meego_url_type`

该接口用于识别MeeGo的URL类型。根据不同的URL类型，返回不同的信息：1.如果是视图链接，返回视图类型、视图ID、筛选器ID和视图模式；2.如果是图表链接，返回图表ID及其对应的视图信息；3.如果是工作项详情链接，返回工作项类型和ID；4.如果只能提取出simpleName，则返回项目详情信息，注意：该工具禁止重复调用

---

**Parameters Schema:**

{"type":"object","properties":{"url":{"type":"string","description":"MeeGo URL，参数示例：\"https://meego.larkoffice.com|meego.feishu.cn|project.feishu.cn/bitsdevops/sprint/detail/6092166577?parentUrl=%2Fbitsdevops%2Fsprint%2Fhomepage\u0026openScene=2\"","properties":{}}},"required":["url"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_identify_meego_url_type", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)