"""
# `deploy_frontend`

Preview a compiled static site directory. The directory can be a relative path (e.g. '.'). The directory should only contain essential files; verify the file list before deploying.
For frontend projects based on frameworks like Vue or React, first compile the project into static files, then use this tool to create a preview deployment.
The deployment uses index.html as the entry point. Only include necessary static files (html, css, js, images, etc.).
Note: For managed repositories, this tool returns a routing handoff and does not upload files directly.

---

**Parameters Schema:**

{"type":"object","properties":{"directory":{"type":"string","description":"the directory to deploy, it should contain an index.html as the entry point","properties":{}}},"required":["directory"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="deploy", tool_name="deploy_frontend", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)