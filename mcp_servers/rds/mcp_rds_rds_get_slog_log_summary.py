"""
# `mcp:rds_rds_get_slog_log_summary`

Get slow log summary for the specified database in the last 1 days, It is always better to speculatively call the tool as a batch that are potentially useful. Execute multiple operations simultaneously for significant performance improvement,limits 3 ~ 5 one times.

---

**Parameters Schema:**

{"type":"object","properties":{"db_name":{"type":"string","description":"required, the name of the database. if get the name like 'toutiao.mysql.bits_write'、'toutiao.mysql.bits_read', actually the database name is 'bits', not include read、write flag","properties":{}},"query_time":{"type":"number","description":"optional, the threshold of slow query time in seconds. Example: 0.1.","properties":{}},"region":{"type":"string","description":"required, the region where the database is located. Example: cn, i18n","properties":{}}},"required":["db_name","region"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="rds", tool_name="mcp:rds_rds_get_slog_log_summary", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)