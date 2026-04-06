"""
# `mcp:bits_analysis_list_issues`

List issues in a specific repository on the Bits Analysis platform
Notes for using the `list_issues` tools:
* The `repo_name` parameter is required and must specify the name of the git repository.
* The `scene` parameter is required and should be chosen from the available options: quality_analysis, merge_check, deploy_check, resolution_check.
* The `rule_name` parameter is optional and can be provided to filter issues by specific rules.
* The `rule_names` parameter is optional and can be provided to filter issues by multiple rules.
* The `resolution_id` parameter is required only when `scene` is set to `resolution_check`. In this case, `resolution_id` corresponds to the specific resolution ID.
* The `page` parameter defaults to 1; valid values must be >= 1.
* The `per_page` parameter defaults to 100; valid values must be within [1, 100].
* The `merge_request_id` required only when the scene is merge_check, it can be obtained from codebase merge request link such as https://code.byted.org/xx/yy/merge_requests/1234, 1234 is the merge request id.


---

**Parameters Schema:**

{"type":"object","properties":{"assignee_names":{"type":"array","description":"list of assignee names of the issue","properties":{},"items":{"type":"string","properties":{}}},"file_path_prefix":{"type":"string","description":"file path prefix of the issue","properties":{}},"merge_request_id":{"type":"number","description":"required only when the scene is merge_check, it can be obtained from codebase merge request link such as https://code.byted.org/xx/yy/merge_requests/1234, 1234 is the merge request id","properties":{}},"page":{"type":"number","description":"Page number, default 1, must be \u003e= 1","properties":{}},"per_page":{"type":"number","description":"Number of issues per page, default 100, range 1-100","properties":{}},"repo_name":{"type":"string","description":"The repo name is in form of `x/y`","properties":{}},"resolution_id":{"type":"number","description":"Optional, required only when the scene is resolution_check, specifies the ID of the governance project; not needed for other scenarios，resolution in chinese is \"专项\"","properties":{}},"rule_names":{"type":"array","description":"filter by rule names","properties":{},"items":{"type":"string","properties":{}}},"scene":{"type":"string","description":"scenario name, enum values: quality_analysis, merge_check, deploy_check, resolution_check","properties":{}},"severities":{"type":"array","description":"filter by severities, e.g. \"critical\", \"error\", \"warning\", \"info\"","properties":{},"items":{"type":"string","properties":{}}}},"required":["scene","page","per_page","repo_name"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="bits_analysis", tool_name="mcp:bits_analysis_list_issues", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)