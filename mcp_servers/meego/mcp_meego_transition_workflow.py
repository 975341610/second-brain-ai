"""
# `mcp:meego_transition_workflow`

Execute workflow state transition for a Meego work item. IMPORTANT: You must first call get_workflow_detail to retrieve valid transition IDs for the work item, also, if you don't what options or what to input for mandatory fields, call `get_work_item_metadata`

---

**Parameters Schema:**

{"type":"object","properties":{"fields":{"type":"array","description":"Optional, fields to update, default empty, if return field is mandatory filled, then retry with values","properties":{},"items":{"type":"object","properties":{"field_alias":{"type":"string","properties":{}},"field_key":{"type":"string","properties":{}},"field_type_key":{"type":"string","properties":{}},"field_value":{"type":"null","properties":{}},"target_state":{"type":"object","properties":{"state_key":{"type":"string","properties":{}},"transition_id":{"type":"integer","properties":{}}}}}}},"node_schedule":{"type":"object","description":"Optional, but usually a state will return Estimates and schedules are required, then must set and retry","properties":{"estimate_end_date":{"type":"integer","properties":{}},"estimate_start_date":{"type":"integer","properties":{}},"owners":{"type":"array","properties":{},"items":{"type":"string","properties":{}}},"points":{"type":"number","properties":{}}}},"role_owners":{"type":"array","description":"Optional, role owners to set","properties":{},"items":{"type":"object","properties":{"name":{"type":"string","properties":{}},"owners":{"type":"array","properties":{},"items":{"type":"string","properties":{}}},"role":{"type":"string","properties":{}}}}},"simple_name":{"type":"string","description":"Required, workspace name","properties":{}},"transition_id":{"type":"integer","description":"Required for state work item types like issue, but no need for workflow types like story","properties":{}},"work_item_id":{"type":"integer","description":"Required, work item ID","properties":{}},"work_item_type_key":{"type":"string","description":"Required, work item type key (e.g., story, issue)","properties":{}}},"required":["simple_name","work_item_type_key","work_item_id","transition_id","role_owners","fields","node_schedule"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_transition_workflow", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)