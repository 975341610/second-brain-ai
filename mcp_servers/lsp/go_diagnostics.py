"""
# `go_diagnostics`

Retrieve code diagnostics (errors and warnings) from the language server (LSP) for the current workspace.
	Note: This tool is only available for Go projects.

---

**Parameters Schema:**

{"type":"object","properties":{}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lsp", tool_name="go_diagnostics", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)