"""
# `mcp:aeolus_aeolus_list_datasets`

获取指定APP下的数据集树（dataSetTreeViewV2），注意roleList不为空的item表示当前用户有权限访问的

---

**Parameters Schema:**

{"type":"object","properties":{"app_id":{"type":"integer","description":"必填，APP ID","properties":{}},"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}}},"required":["base_url","app_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_list_datasets", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)