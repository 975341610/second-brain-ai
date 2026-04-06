"""
# `mcp:lark_workspace_analyze_work_find_lark_docs`

根据 MR 和 OKR 自动分析重点工作方向，从用户历史文档中查找相关参考资料。以 MR 内容为主 OKR 为辅，自动识别重要事项并按方向归纳，最后匹配相关文档作为参考

---

**Parameters Schema:**

{"type":"object","properties":{"end_date":{"type":"string","description":"必填，查询结束日期，格式为YYYY-MM-DD","properties":{}},"merged_request_file_path":{"type":"string","description":"必填，MR 文件路径，包含用户的 Merge Request 信息","properties":{}},"okr_file_path_list":{"type":"array","description":"可选，OKR 文件路径列表，包含用户的 OKR 信息","properties":{},"items":{"type":"string","properties":{}}},"start_date":{"type":"string","description":"必填，查询开始日期，格式为YYYY-MM-DD","properties":{}},"user_name":{"type":"string","description":"必填，要查询的用户名，必须是ID，例如：zhangsan.001","properties":{}}},"required":["merged_request_file_path","okr_file_path_list","user_name","start_date","end_date"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_workspace", tool_name="mcp:lark_workspace_analyze_work_find_lark_docs", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)