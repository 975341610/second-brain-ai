"""
# `mcp:meego_create_work_item`

创建新的工作项，仅支持单个创建。调用此工具之前，必须调用获取创建工作项元信息工具(get_work_item_metadata)获取必填字段信息。

---

**Parameters Schema:**

{"type":"object","properties":{"simple_name":{"type":"string","description":"必填，空间名称","properties":{}},"work_items":{"type":"array","description":"必填，工作项列表，用于批量创建工作项","properties":{},"items":{"type":"object","properties":{"field_value_pairs":{"type":"array","description":"必填，工作项字段值对，如果字段为人员相关字段，必须填user key","properties":{},"items":{"type":"object","properties":{"field_alias":{"type":"string","properties":{}},"field_key":{"type":"string","properties":{}},"field_type_key":{"type":"string","properties":{}},"field_value":{"type":"null","properties":{}},"target_state":{"type":"object","properties":{"state_key":{"type":"string","properties":{}},"transition_id":{"type":"integer","properties":{}}}}}}},"name":{"type":"string","description":"必填，工作项名称","properties":{}},"template_id":{"type":"integer","description":"选填，工作项模板ID，从metadata接口中的template字段的options中获取，选择对应的value，对于指定了类型的工作项，必须找到并指定模板ID","properties":{}},"work_item_type":{"type":"string","description":"必填，工作项类型, 枚举值可选：story，issue","properties":{}}},"required":["work_item_type","name","field_value_pairs","template_id"]}}},"required":["simple_name","work_items"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_create_work_item", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)