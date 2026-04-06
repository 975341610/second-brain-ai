"""
# `mcp:devmind_query_chart_url`

Query the charts url based on the returned dimensions, metrics, and data model.

---

**Parameters Schema:**

{"type":"object","properties":{"analysis_dimension":{"type":"string","description":"The analysis dimension for generating visual analytical charts extracted from the user's input prompt, include time dimension","properties":{}},"analysis_metric":{"type":"string","description":"The analysis metric for generating visual analytical charts extracted from the user's input prompt","properties":{}},"chart_url_request":{"type":"object","description":"The request body for querying chart data,It could be different requests resulting from combinations of various dimensions, metrics, or filter values.","properties":{"chart_type":{"type":"string","description":"sheet, line, bar, bar_stack, line_stack, percent_bar_stack, pie, double_axis, card, radar, bar_row","properties":{}},"dimension_condition_list":{"type":"array","properties":{},"items":{"type":"object","properties":{"begin_time":{"type":"string","description":"if there is a time dimension and the granularity_id is 14 (i.e., biweekly), then this value is mandatory, if the user does not specify to fill in with the system's current time. format: YYYY-MM-DD","properties":{}},"dimension_id":{"type":"string","properties":{}},"granularity_id":{"type":"integer","description":"filter time granularity when used with time dimension, Day (id = 1)  Week (id = 2) Month (id = 3) (which is the default Time Granularity if user doesn't specify) BiMonth (id = 4) Quater (id = 49)","properties":{}},"operator":{"type":"string","properties":{}},"value":{"type":"array","description":"filter value","properties":{},"items":{"type":"string","properties":{}}}},"required":["dimension_id"]}},"dimension_list":{"type":"array","properties":{},"items":{"type":"object","properties":{"begin_time":{"type":"string","description":"if there is a time dimension and the granularity_id is 14 (i.e., biweekly), then this value is mandatory, if the user does not specify to fill in with the system's current time. format: YYYY-MM-DD","properties":{}},"dimension_id":{"type":"string","properties":{}},"granularity_id":{"type":"integer","description":"filter time granularity when used with time dimension, Day (id = 1)  Week (id = 2) Month (id = 3) (which is the default Time Granularity if user doesn't specify) BiMonth (id = 4) Quater (id = 49)","properties":{}},"operator":{"type":"string","properties":{}},"value":{"type":"array","description":"filter value","properties":{},"items":{"type":"string","properties":{}}}},"required":["dimension_id"]}},"metric_list":{"type":"array","properties":{},"items":{"type":"object","properties":{"agg_type":{"type":"string","description":"If it is a metric type itself, this field is not needed; it is only required when the MetricType is dimension","properties":{}},"extra":{"type":"integer","description":"If the aggType is of the quantile type, this value represents the quantile value.","properties":{}},"metric_id":{"type":"string","properties":{}},"metric_type":{"type":"string","description":"Select from the recommended metrics or dimensions. The selection shall be exactly what is taken from the source, and can only be either \"dimension\" or \"metric\". The default value \"metric\" may be omitted.","properties":{}}},"required":["metric_id"]}},"model_id":{"type":"string","properties":{}}},"required":["model_id","metric_list","dimension_list","dimension_condition_list"]},"filter_condition":{"type":"string","description":"The filtering conditions for generating visual analytical charts extracted from the user's input prompt, include time condition dimension","properties":{}}},"required":["analysis_metric","analysis_dimension","filter_condition","chart_url_request"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="devmind", tool_name="mcp:devmind_query_chart_url", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)