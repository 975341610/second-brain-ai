"""
# `mcp:aeolus_aeolus_dataset_dim_met`

Dateset Dimension和Metric获取

---

**Parameters Schema:**

{"type":"object","properties":{"base_url":{"type":"string","description":"Aeolus域名，默认https://data.bytedance.net","properties":{}},"dataset_id":{"type":"integer","description":"必填，数据集ID","properties":{}},"need_conf":{"type":"boolean","description":"是否需要配置，默认false，一般不需要，配置包含了数据集的基本信息(baseConf)，数据血缘与SQL逻辑（nodeConf），调度配置（syncConf）等，除非维度和指标信息不满足，否则不要轻易开启","properties":{}}},"required":["base_url","dataset_id","need_conf"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="aeolus", tool_name="mcp:aeolus_aeolus_dataset_dim_met", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)