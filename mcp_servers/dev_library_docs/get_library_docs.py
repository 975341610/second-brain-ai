"""
# `get_library_docs`

Fetches up-to-date documentation for a library. You must call 'resolve_library_id' first to obtain the exact library ID required to use this tool, .

USAGE GUIDELINES:
- This tool works for BOTH internal libraries (from code.byted.org like "code.byted.org/middleware/hertz/byted") AND public libraries (from github.com, golang.org, etc). 
- You Must use this tool for any libraries you're not familiar with. DO NOT guess or assume how a library works based on similar libraries or general knowledge.
- Always get multiple library docs in parallel when possible. Aim for combined coverage code snippets ≥ 40 when possible.
- If an '@docs/' variant exists for a target, search the '@docs/' library first as higher priority.

QUERY CONSTRUCTION (KEEP IT SIMPLE AND EXPLICIT):
- Preferred format: <LanguageToken> <key intent terms> (e.g., Go HTTP routing, Java JWT middleware).
- Focus on core nouns/verbs from the user intent; avoid noise terms.
- Include specific framework or feature keywords if present in the selected libraries.
- If the LanguageToken is uncertain, try to infer from context (code snippet, file extension, keywords).

WORKFLOW:
1. Resolve library candidates
  - resolve_library_id(library_name=<user_query>, top_n=<k>)
2. Choose libraries
  - include all relevant libraries.
3. Build search query
  - Apply the QUERY CONSTRUCTION rules.
  - Use the preferred format: "<LanguageToken> <key intent terms>"
4. Fetch docs in parallel
  - get_library_docs(library_id=<library_id>, topic=<constructed_query>)


---

**Parameters Schema:**

{"type":"object","properties":{"library_id":{"type":"string","description":"required, The library ID to get docs for (e.g. middleware/hertz, @docs/Hertz, /react-hook-form/documentation)","properties":{}},"source":{"type":"string","description":"required, Source to fetch from: 'internal' or 'public'. Default is internal. 'internal' means from code.byted.org like 'code.byted.org/middleware/hertz/byted', 'public' means from github.com, golang.org, etc.","properties":{}},"topic":{"type":"string","description":"required, Search by topic, e.g. 'hertz server middleware'","properties":{}}},"required":["library_id","topic","source"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="dev_library_docs", tool_name="get_library_docs", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)