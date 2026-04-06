"""
# `html_vision`

Verify if a webpage is available and functional. This tool will render the webpage as an image, capture console logs, and analyze the page to determine if it's working properly.
	Note: this tool only performs static checks, not interactive testing. For local HTML files, use file:///path/to/file.html directly - no need to start a local server.

---

**Parameters Schema:**

{"type":"object","properties":{"task":{"type":"string","description":"specific static verification points to check (visual-only, no interactive testing)","properties":{}},"url":{"type":"string","description":"the url of html destination, https://xxx for deployed url and file:///path/xxx.html for local file","properties":{}}},"required":["task","url"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="deploy", tool_name="html_vision", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)