"""
# `mcp:rds_rds_run_sql`

Execute SQL in the specified database. The result will be saved to a CSV file and the file path will be returned.

---

**Parameters Schema:**

{"type":"object","properties":{"db_name":{"type":"string","description":"required, the name of the database.","properties":{}},"filepath":{"type":"string","description":"optional. the file path to save the result. if not provided, a random file name will be used.","properties":{}},"region":{"type":"string","description":"optional, the region where the database is located. Example: cn, i18n, boe. default is cn.","properties":{}},"sql":{"type":"string","description":"required, the sql content to execute.","properties":{}}},"required":["db_name","sql","region","filepath"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="rds", tool_name="mcp:rds_rds_run_sql", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)