"""
# `mcp:byted_fe_knowledge_get_general_knowledge`

Acquire ByteDance's internal unique frontend development knowledge to help develop more accurate ByteDance frontend code.

---

**Parameters Schema:**

{"type":"object","properties":{"lib":{"type":"string","description":"Knowledge library, such as edenx, mf, rspack, rsbuild, vmok, emo, modernjs, eden-proxy etc.","enum":["general","通用知识","edenx","@edenx/app-tools","@edenx/runtime","edenx.config.ts","mf","ModuleFederation","@module-federation/","rspack","@rspack/","@rspack/core","rspack.config.ts","rsbuild","@rsbuild/","@rsbuild/core","rsbuild.config.ts","eden proxy","@edenx/proxy","eden-proxy","vmok","@vmok/","@vmok/runtime","@vmok/webpack-plugin-v5","@vmok/kit","@edenx/plugin-vmok","emo","eden-monorepo","@edenx/eden-monorepo","eden.monorepo.json","garfish","@garfish/bridge-react","@garfish/bridge-vue-v2","modernjs","@modern-js/","@modern-js/runtime","@modern-js/app-tools"],"properties":{},"default":"general"},"query":{"type":"string","description":"Query content","properties":{}}},"required":["query"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="byted_fe_knowledge", tool_name="mcp:byted_fe_knowledge_get_general_knowledge", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)