"""
# `mcp:SlardarApp_get_app_common_filter_list`

可以获取到某个页面下支持的筛选项，可以用于获取到每个可用筛选项的具体详情，dimension为这个字段的具体名称，mapKey为这个字段存储数据的内部key。

---

**Parameters Schema:**

{"type":"object","properties":{"link":{"type":"string","description":"Slardar issue详情页链接","properties":{}},"page_no":{"type":"integer","description":"页号，从0开始","properties":{}},"page_size":{"type":"integer","description":"页大小，默认值50，最大值100","properties":{}}},"required":["link","page_no","page_size"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="SlardarApp", tool_name="mcp:SlardarApp_get_app_common_filter_list", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)