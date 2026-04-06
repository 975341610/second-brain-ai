"""
# `d2c`

Convert Figma designs into high-quality frontend code outputs as a dedicated sub-agent process.

				When to use?
				1. user content or user provided lark document contains figma design url(starts with https://www.figma.com/design/)
				2. user content requests to convert a figma design to frontend code
				3. user content requests to generate frontend code based on a figma design
				4. user explicitly requests the d2c agent tool
				
				Must follow:
				1. Must retrieve UI library component knowledge (for all components to be used) before JSX refactoring.

				Strictly forbidden:
				1. Make any content changes unrelated to the d2c output
			

---

**Parameters Schema:**

{"type":"object","properties":{"meta":{"type":"string","description":"可选：元数据","properties":{}},"node_id":{"type":"string","description":"可选：Figma 节点 ID，覆盖 URL 中的 node-id","properties":{}},"output_language":{"type":"string","description":"The language of the final output","properties":{}},"url":{"type":"string","description":"Figma design URL, usually starts with https://www.figma.com/design/","properties":{}}},"required":["url","node_id","meta","output_language"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="d2c", tool_name="d2c", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)