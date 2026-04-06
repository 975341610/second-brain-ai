"""
# `deploy_backend`

Specify a directory to deploy a backend service to user. The directory can be a relative path (e.g. '.'). The directory should only contain essential files, verify the files list before deploy them.
Only supports FastAPI applications created by aime_create_fastapi_app.

---

**Parameters Schema:**

{"type":"object","properties":{"directory":{"type":"string","description":"the directory to deploy, it should contain a FastAPI application (app.py or main.py)","properties":{}}},"required":["directory"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="deploy", tool_name="deploy_backend", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)