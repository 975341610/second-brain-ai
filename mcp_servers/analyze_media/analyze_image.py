"""
# `analyze_image`

Call a multimodal LLM API to analyze and understand image files ONLY. This tool ONLY accepts image files (PNG/JPG/JPEG/GIF/WEBP). For any non-image files(text files, code files, etc.), use read tool instead.

Use cases:
- OCR: Extract and recognize text that appears WITHIN images (e.g., screenshots, photos of documents, diagrams with labels)
- Image Inspection: Detect quality issues, defects, or visual problems
- Image Recognition: Identify and describe objects, people, scenes, UI elements in images
- Image Comparison: Analyze visual similarity or differences between images

- DO NOT read text files or other non-image files using this tool. Use read tool instead.


---

**Parameters Schema:**

{"type":"object","properties":{"paths":{"type":"array","description":"the paths of the image files, supports up to 10 images","properties":{},"items":{"type":"string","properties":{}}},"task":{"type":"string","description":"the message to send to the vision LLM","properties":{}}},"required":["task","paths"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="analyze_media", tool_name="analyze_image", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)