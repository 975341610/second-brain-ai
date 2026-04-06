"""
# `mcp:meego_update_work_item`

Update an existing work item. IMPORTANT: 1) Before using this tool, you must first call list_work_items or get_work_item_detail to retrieve current field values. 2) This tool updates specified fields by completely replacing their previous values, not by appending to them. For example, when updating role-member fields, you must include ALL roles and members in your update, not just the ones you want to change. 3) Field values will be completely overwritten with the new values provided.

---

**Parameters Schema:**

{"type":"object","properties":{"simple_name":{"type":"string","description":"Required, workspace name","properties":{}},"update_fields":{"type":"array","description":"Required, list of field-value pairs to update, IMPORTANT: 该字段的格式必须和你拿到的当前工作项的field_value一致， 禁止使用其他格式, 所有涉及到人员的field需要填入userKey","properties":{},"items":{"type":"object","properties":{"field_alias":{"type":"string","properties":{}},"field_key":{"type":"string","properties":{}},"field_type_key":{"type":"string","properties":{}},"field_value":{"type":"null","properties":{}},"target_state":{"type":"object","properties":{"state_key":{"type":"string","properties":{}},"transition_id":{"type":"integer","properties":{}}}}}}},"work_item_id":{"type":"integer","description":"Required, work item ID to update","properties":{}},"work_item_type_key":{"type":"string","description":"Required, work item type key,必填，工作项类型, 枚举值可选：story，issue","properties":{}}},"required":["simple_name","work_item_type_key","work_item_id","update_fields"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_update_work_item", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)