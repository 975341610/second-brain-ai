"""
# `mcp:meego_list_work_item_by_relation`

查询与指定工作项存在工作项关联的工作项列表,如'测试工作项关联'为需求和缺陷的关联字段(relation_key),可查询该需求工作项实例下绑定的缺陷列表

---

**Parameters Schema:**

{"type":"object","properties":{"relation_key":{"type":"string","description":"必填，关联关系key，如 blocks, relates_to 等","properties":{}},"relation_work_item_type_key":{"type":"string","description":"必填，关联工作项类型，如 story, issue 等","properties":{}},"result_file_path":{"type":"string","description":"必填，工作项查询结果的文件存储路径，将输出为Excel文件，例如：related_work_items_xxx.xlsx。重点注意：如果文件名已存在，会覆盖原文件，尽量避免文件名重名！。","properties":{}},"simple_name":{"type":"string","description":"必填，空间名称","properties":{}},"work_item_id":{"type":"integer","description":"必填，工作项ID","properties":{}},"work_item_type_key":{"type":"string","description":"必填，工作项类型，如 story, issue 等","properties":{}}},"required":["simple_name","work_item_type_key","work_item_id","relation_work_item_type_key","relation_key","result_file_path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="meego", tool_name="mcp:meego_list_work_item_by_relation", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)