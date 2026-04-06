"""
# `mcp:yfinance_yahoo_finance`

Fetch Yahoo Finance data based on the given query parameters.. The tool will return structured financial data that can be used for analysis or decision-making.

---

**Parameters Schema:**

{"type":"object","properties":{"end_date":{"type":"string","description":"optional，End date for historical data in YYYY-MM-DD format, example：2025-06-18. If start_date and end_date are not provided, you can only get the latest information of the stock, but not the historical data.","properties":{}},"start_date":{"type":"string","description":"optional，Start date for historical data in YYYY-MM-DD format，example：2025-01-01. If start_date and end_date are not provided, you can only get the latest information of the stock, but not the historical data.","properties":{}},"tickers":{"type":"array","description":"required，Array of ticker symbols ，example：[\"AAPL\", \"GOOG\", \"MSFT\"]","properties":{},"items":{"type":"string","properties":{}}}},"required":["tickers"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="yfinance", tool_name="mcp:yfinance_yahoo_finance", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)