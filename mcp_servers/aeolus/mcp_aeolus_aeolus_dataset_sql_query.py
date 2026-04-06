"""
# `mcp:aeolus_aeolus_dataset_sql_query`

针对指定数据集执行SQL Query

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"dataset_id":{"type":"integer","description":"必填，数据集ID","properties":{}},"sql":{"type":"string","description":"必填，SQL语句","properties":{}}},"required":["base_url","dataset_id","sql"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_dataset_sql_query", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)