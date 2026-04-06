"""
# `create_merge_request_comment`

create comments in a codebase MR, result will contain message, all comments, published count and ignore counts. You should use user preferred locale to generate the comments.

---

**Parameters Schema:**

{"type":"object","properties":{"comments":{"type":"array","description":"required, comments list to create","properties":{},"items":{"type":"object","properties":{"accuracy":{"type":"integer","description":"accuracy score of the comment, an integer from 0 to 100. 90-100: the issue is definitely present with solid evidence (e.g. undefined variable, syntax error); 70-90: issue exists with sufficient evidence (e.g. logic error, null pointer, security issue); 50-70: issue is inferred from experience with insufficient evidence; 30-50: description does not match code, pure speculation, or style suggestion that does not affect correctness; 0-30: false positive, missing location or fix, issue does not actually exist, or suggested fix causes crash.","properties":{}},"base_commit_id":{"type":"string","description":"base commit id of the merge request.","properties":{}},"code_line_content":{"type":"string","description":"one of the most related code line content of the comment.","properties":{}},"confidence_score":{"type":"number","description":"Confidence score of the comment (0-1.0).","properties":{}},"end_line":{"type":"integer","description":"File position: end line, starting from 1, inclusive.","properties":{}},"file_path":{"type":"string","description":"File position: file path.","properties":{}},"improvement_example_code":{"type":"string","description":"The code to fix the issue, must be in the same language as the original. Use standard JSON string escaping. Do NOT double-escape or wrap with extra quotes.","properties":{}},"improvement_example_description":{"type":"string","description":"Description of the improvement example. Use user preferred locale to generate the description.","properties":{}},"issue_description":{"type":"string","description":"Description of the issue. Use user preferred locale to generate the description.","properties":{}},"locale":{"type":"string","description":"Locale of the comment, default is zh-CN.","properties":{}},"priority":{"type":"integer","description":"Priority of the comment","properties":{}},"side":{"type":"string","description":"File position: comment on the old side or new side of the merge request diff, default is new.","properties":{}},"source_commit_id":{"type":"string","description":"source commit id of the merge request.","properties":{}},"start_line":{"type":"integer","description":"File position: start line, starting from 1.","properties":{}}},"required":["issue_description","improvement_example_description","improvement_example_code","priority","locale","side","file_path","confidence_score","start_line","end_line","base_commit_id","source_commit_id"]}},"draft":{"type":"boolean","description":"optional, whether to create the comment as a draft (invisible to others), default is false","properties":{}},"locale":{"type":"string","description":"required, locale for all comments (zh-CN or en-US). Use user preferred locale to generate the comment.","properties":{}},"number":{"type":"integer","description":"required, the number of the merge request","properties":{}},"repo_name":{"type":"string","description":"required, codebase repo name, eg group/repo","properties":{}}},"required":["repo_name","number","comments","locale"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="codebase", tool_name="create_merge_request_comment", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)