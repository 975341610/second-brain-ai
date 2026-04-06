"""
# `resolve_library_id`

Resolves library IDs by searching the knowledge base for libraries matching the given name. Returns a list of matching libraries with their IDs, descriptions, and metadata.

USAGE GUIDELINES:
- You MUST call this function before get_library_docs to obtain a valid library ID.
- This tool works for BOTH internal libraries (from code.byted.org like "code.byted.org/middleware/hertz/byted") AND public libraries (from github.com, golang.org, etc). 
- You Must use this tool for any libraries you're not familiar with. DO NOT guess or assume how a library works based on similar libraries or general knowledge
	
QUERY CONSTRUCTION:
- Preferred format: <LanguageToken> <canonical library or ecosystem term>
- Examples: Go Gin, Go GORM, Java Spring, TypeScript WebSocket, Python FastAPI
- If the user gives only a feature, add an ecosystem/framework anchor:
  	Good: Go router gin, Java JWT spring
- Include common aliases/abbreviations (e.g., Gin, GORM, Spring, Kafka) and keep it short (2-5 words)
- If the LanguageToken is uncertain, infer from context (code snippet, file extension, keywords) or omit it and rely on feature + ecosystem.

---

**Parameters Schema:**

{"type":"object","properties":{"library_name":{"type":"string","description":"required, Search term for finding libraries","properties":{}},"source":{"type":"string","description":"optional, Source to search from: 'internal' (from code.byted.org) or 'public' (from github.com, golang.org, etc)","properties":{}}},"required":["library_name"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="dev_library_docs", tool_name="resolve_library_id", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)