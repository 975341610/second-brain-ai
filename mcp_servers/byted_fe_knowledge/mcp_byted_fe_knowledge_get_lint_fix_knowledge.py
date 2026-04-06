"""
# `mcp:byted_fe_knowledge_get_lint_fix_knowledge`

获取指定 Lint 规则名的修复知识，如 eslint 规则名 no-useless-escape，字节前端代码规范工具规则名 byted_s_react_jsx_key 等

---

**Parameters Schema:**

{"type":"object","properties":{"ruleName":{"type":"string","description":"规则名，如 no-useless-escape 或 byted_s_react_jsx_key 等","properties":{}}},"required":["ruleName"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="byted_fe_knowledge", tool_name="mcp:byted_fe_knowledge_get_lint_fix_knowledge", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)