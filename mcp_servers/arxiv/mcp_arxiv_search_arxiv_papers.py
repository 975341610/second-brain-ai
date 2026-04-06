"""
# `mcp:arxiv_search_arxiv_papers`

Search for papers on arXiv with advanced filtering

---

**Parameters Schema:**

{"type":"object","properties":{"categories":{"type":"array","description":"arXiv category filters. Use specific categories like 'cs.AI', 'math.GT', or 'physics.optics'. For a main subject area, use wildcards like 'cs.*' (all computer science), 'math.*' (all mathematics), 'physics.*' (all physics). To search all subjects, omit this parameter entirely rather than using '*'.","properties":{},"items":{"type":"string","properties":{}}},"date_from":{"type":"string","description":"Start date of the query in YYYYMMDD format (inclusive). Represents the beginning of a left-closed, right-open date range. For example, to query data on 20250108, set date_from to '20250108'.","properties":{},"format":"YYYYMMDD"},"date_to":{"type":"string","description":"End date of the query in YYYYMMDD format (exclusive). Must not be '*'. Represents the end of a left-closed, right-open date range. For example, to query data on 20250108, set date_to to '20250109'.","properties":{},"format":"YYYYMMDD"},"max_results":{"type":"integer","properties":{},"maximum":50},"page":{"type":"integer","description":"offset page for pagination, 1,2,3...","properties":{}},"query":{"type":"string","description":"Enter plain keywords without quotes or field qualifiers; use * if no keywords are provided.","properties":{}},"sort_by":{"type":"string","description":"Use Relevance for most scenarios unless there's a strong requirement to sort by date. Relevance provides the most useful results for typical queries.","enum":["Relevance","LastUpdatedDate","SubmittedDate"],"properties":{},"default":"Relevance"},"sort_order":{"type":"string","description":"only useful when sort_by is not Relevance","enum":["Ascending","Descending"],"properties":{},"default":"Descending"}},"required":["query"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="arxiv", tool_name="mcp:arxiv_search_arxiv_papers", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)