"""
# `mcp:aeolus_aeolus_dataset_lineage`

获取风神数据集血缘/关联资源信息（dataSetLineage）：返回该数据集关联的仪表盘(dashboard)与图表(report)列表，常用字段包括data.resourceList[].resourceId/resourceName/resourceType/resourceOwner/resourceFolder/role

---

**Parameters Schema:**

{"type":"object","properties":{"app_id":{"type":"integer","description":"必填，APP ID（必须传入）","properties":{}},"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"dataset_id":{"type":"integer","description":"必填，数据集ID","properties":{}}},"required":["base_url","app_id","dataset_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_dataset_lineage", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)