"""
# `mcp:image_search_image_search`

image_search is a tool that finds existing web images and downloading them locally with mandatory AI-powered evaluation. 
	All searched images are compliant and usable without copyright issues. Requires evaluation_prompt to define specific use case requirements. 
	Usage:
	- Use this tool when user's requirement is related to images.
	- Also use when creating web pages, HTML content, or any visual artifacts that would benefit from images. 
	- Use for presentations or when users need visual materials with local file access.

---

**Parameters Schema:**

{"type":"object","properties":{"evaluation_prompt":{"type":"string","description":"[Required] prompt for evaluating downloaded images. This is crucial as it defines the specific use case and requirements for image selection. Maximum 300 characters. Examples: 'suitable for business presentation', 'appropriate for children content', 'high quality for website banner', etc.","properties":{}},"num":{"type":"integer","description":"Number of images to search for. default 5, max 15","properties":{}},"query":{"type":"string","description":"The image search keyword or phrase. Can be in English, Chinese","properties":{}}},"required":["query","num","evaluation_prompt"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="image_search", tool_name="mcp:image_search_image_search", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)