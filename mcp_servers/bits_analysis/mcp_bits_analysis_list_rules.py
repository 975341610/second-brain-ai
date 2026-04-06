"""
# `mcp:bits_analysis_list_rules`

List rules metadata in the Bits Analysis platform
Notes for using the `list_rules` tools:
* The `language` parameter is optional and can be provided to filter rules by specific programming languages.
* The `key_word` parameter is optional and can be provided to search rules by keywords.
* The `page` parameter is required and must specify the page number.
* The `per_page` parameter is required and must specify the number of rules per page.
* The `page` parameter defaults to 1; valid values must be >= 1.
* The `per_page` parameter defaults to 20; valid values must be within [1, 100].


---

**Parameters Schema:**

{"type":"object","properties":{"key_word":{"type":"string","description":"keyword to search","properties":{}},"language":{"type":"string","description":"language of the rule, e.g. \"Python\", \"Java\", \"Go\"","properties":{}},"page":{"type":"number","description":"Page number, default 1","properties":{}},"per_page":{"type":"number","description":"Number of rules per page, default 20","properties":{}}}}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="bits_analysis", tool_name="mcp:bits_analysis_list_rules", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)