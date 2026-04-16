<title>Aime Skill MCP 配置指南</title>
<url>https://bytedance.larkoffice.com/wiki/FJj7wHMAMiH2IekOWxYcezkMnmd</url>
<content>
<!-- BLOCK_1 | G4PedDbjzoANXaxrAiwcYE4Vnie -->
## Skill vs MCP<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | WlMXdCILmoGpCMxxcwqc5spVnGe -->
> <grid cols="2">
> <column width="64">
>   > > ![图片](img_JOXFbOupLocoXwxRkz2cZVhenMf.png)
>   > 
>   > 
> </column>
> <column width="35">
>   > > ![图片](img_XcwbbyVQoo5dqSxUDeLcW1t9nEE.png)
>   > 
>   > 
> </column>
> </grid>
<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | OaXadP5ExoaW4Sx7oQcc4UgOndf -->
相信很多同学在新功能的开发时，对选择 MCP 还是 Skill 都有些拿不准，这说明二者之间并不完全正交。官方也意识到了这个问题，在多处文档中都进行了相关阐述，总结起来官方想表达的意思为：
<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | Zqswd2iwwornRYxHz2pc6WrTntc -->
<callout icon="watermelon" bgc="2" bc="2">
MCP 用于连接、通过提供工具来获取数据；Skill 就是知识，用来教会模型如何使用工具，如何编排某件任务，二者是配合的关系。
</callout>
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | SCYtdQUPBo2ch5xcWfMcZkhenXc -->
但实际上远没有那么理想，会存在如下问题。
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | EyBMdC9yKoWAu3xoRyGcY55rn1e -->
1. **不够内聚和原子性**。按照官方说法，必须至少同时配置一个 MCP 和一个 Skill or 一条知识来完成。对于功能的提供者来讲并不友好，甚至某些场景下不合理　
<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | FpbCdvPTVoH4yAxT60LcFArFnWf -->
2. **能力冲突和混淆**。MCP 提供了一系列能力A,B,C。Skill 中编排了 A -> B -> C 。模型同时拥有MCP 的能力的前提下，它完全有权利和能力自行编排和选择路径，不一定严格遵守你的Skill编排方式，后果就是：Skill 不容易调试稳定，会出现随机性。本质上并不是 Skill 机制的问题，而是这两种机制的定位存在耦合和交差出现的必然现象。
<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | ZIkadPqWLo5a8rxr1pYcPyeZnJb -->
3. **过多的 MCP 工具占用上下文**。经常有同学问到 "怎么选择和屏蔽MCP中的Tool"，尤其作为Aime 这样接近通用类型的Agent，工具爆炸是很恐怖的。其实 mcp 也是通过描述教会模型如何使用函数，这件事随着模型能力的增强，不进行注册，在Skill中描述大概率也是可行的。
<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | Ai56dLTggopnxPxk5NHcCuA6nGd -->
综上，我们决定突破官方对Skill 的约束，支持 Skill 中配置 MCP 能力。当然 coding Agent领域存在Plugin的概念，但Coding Agent 领域本身就是细分领域，不在乎工具爆炸问题，Plugin 机制并没有解决以上的三个问题， 只是一种分发手段。
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | VUYedzfmaoVtZTx57N9cKShInAo -->
也许未来业界会走向 Skill = MCP + 知识  的道路也说不定，我们只希望针对 Aime 生态内部来如何协助开发者们更好的完成功能。PS：我们也不认为Skill 会取代 MCP，但二者也不一定是正交的关系，存在一定程度的重合。
<!-- END_BLOCK_10 -->



<!-- BLOCK_11 | doxcn3ynWxWXlMNCy2YKWNSPsDe -->
本文档介绍如何在 Skill 中配置 MCP (Model ContextProtocol) 服务器，使 Skill 能够连接和调用外部 MCP 工具。
<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | doxcng2dfbm2W1bBLeHHQZQWRce -->
## 快速开始<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | doxcnPsTy34pG4FWG2ykuE5148d -->
### 创建配置文件<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | doxcn6kvWcnoufJF8KTolbOdvBe -->
在 Skill 根目录下创建 `.aime/mcp.json` 文件：
<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | doxcnXgLTp0o3GuGR5xONbECWLc -->
```json
{
  "mcpServers": {
    "lark_open_doc_search": {
      "description": "支持查询飞书开放平台的文档",
      "type": "sse",
      "url": "https://pkr0mz0q.mcp.bytedance.net/sse"
    }
  },
  "mcpToSkill": true
}
```
<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | doxcn04Fsvh07iscHvX0n7KmMwe -->
### 选择使用模式<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | doxcnEmzEaPbtyFOwKrIdisFpob -->
Skill MCP 提供两种使用模式：
<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | doxcnARbrXcXiG8BYPTKlcDcOae -->
<table header-row="true" col-widths="180,201,432">
    <tr>
        <td>模式</td>
        <td>配置</td>
        <td>适用场景</td>
    </tr>
    <tr>
        <td>**手动模式**（默认）</td>
        <td>`"mcpToSkill": false`</td>
        <td>你自己控制调用 MCP 工具的时机，更精准</td>
    </tr>
    <tr>
        <td>**自动模式**</td>
        <td>`"mcpToSkill": true`</td>
        <td>Aime 会把 skill 里面配置的 mcp 转成 references 文档，然后内部直接调用</td>
    </tr>
</table>
<!-- END_BLOCK_18 -->



<!-- BLOCK_19 | O3d7deqVso8eGrxwldtcjJIvnje -->
### 例子<!-- END_BLOCK_19 -->

<!-- BLOCK_20 | KWbGdtyGLolhwIxaTMTco07onud -->
#### 简单例子<!-- END_BLOCK_20 -->

<!-- BLOCK_21 | CdUgd9xOZozfYmxM5orcjjnPnve -->
https://aime.bytedance.net/share/0718403a-db23-4515-a676-32fb89c7b4eb
<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | NQx7dW8JooLqYVx4PFCcKZLqnhf -->
**test-skill.zip**
<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | EjCGdbs33orRQpx5YUOc4Jl0n7g -->
<grid cols="2">
<column width="40">
  ![图片](img_WnNXb2AcuoGkuFxvmhRcwNelnkd.png)
</column>
<column width="59">
  ![图片](img_Me7ebcxfAof1qRxVZv8ct81AnKh.png)
</column>
</grid>
<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | JBlVdJRUioHsKjxB7gfcVwaAnYe -->
![图片](img_Ifnxbo4Wro3L3lx9AKMcYsvznKg.png)
<!-- END_BLOCK_24 -->



<!-- BLOCK_25 | A3N7dul0goxlEKxWB3Pcvpg6nje -->
#### 复杂 mcp 快速转 skill<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | BpmEd9pc2ob2gDxMZ7ScwHOPn3b -->
**复杂 mcp**
<!-- END_BLOCK_26 -->

<!-- BLOCK_27 | QEGwdMm43o2PUJxc4jbcM5Lonod -->
- 复杂mcp定义：工具超过10个以上，依靠 tool 的 desc 描述模型世界知识不太好理解，都被称为复杂mcp
<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | LK10dUVA9okSujx6N1ocmLmtnMb -->
- 多个 mcp 同时服务一个任务也属于复杂 mcp 范畴 （工具列表很容易超）
<!-- END_BLOCK_28 -->



<!-- BLOCK_29 | DYlxdyvMSom1Ctx5L6LcnYiYnye -->
Aime 提供了复杂mcp自动转skill的方式，如下
<!-- END_BLOCK_29 -->



<!-- BLOCK_30 | EqR7dGn5ooRV8Ax4lhjcgp2Engk -->
**测试skill**
<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | SNZEdAsFXolbATx0RpVc1cusnCg -->
这里以字节云mcp 市场为例，进行多 mcp 复杂源最佳实践，以下仅仅是例子
<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | Unkyd328ooBZL7xK7jXceaAdnGc -->
- Bits 问答： https://cloud.bytedance.net/mcp/695cf87b824f72416c8defd2?x-resource-account=public&x-bc-region-id=bytedance
<!-- END_BLOCK_32 -->

<!-- BLOCK_33 | FLRqdDYSLo8I0Axd3FDcrkF6nLf -->
- 字节差旅mcp： https://cloud.bytedance.net/mcp/692febbd7055b57d09cfd470?x-resource-account=public&x-bc-region-id=bytedance
<!-- END_BLOCK_33 -->



<!-- BLOCK_34 | RQEvdfOIIouxknxLZWJcgNiZn3f -->
创建 skill，目录如下
<!-- END_BLOCK_34 -->

<!-- BLOCK_35 | MJbxdFpoeoQW8dxiX2pcbhOmnWb -->
```markdown
├── .aime
│   └── mcp.json
└── SKILL.md
```
<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | Kh5dd7gI1oAP6Px1vBdcbcQrn7f -->
mcp.json
<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | Mml2d9BExozxcvxmLITcy7abnRe -->
```json
{
  "mcpServers": {
     "bytedance-mcp-bitsai_quoraid": {
       "description": "基于用户提问，从字节云文档中心、飞书文档、Oncall 工单、ByteTech、代码仓库、日志、应用中心资产、Meego 需求、研发流程数据等各类知识源检索内容，支持联网搜索从搜索引擎查询问题，并给出回答。",
      "type": "sse",
      "url": "https://j2p1h6jb.mcp.bytedance.net/sse"
    },
     "bytedance-mcp-data_service_travel": {
       "description": "字节企业服务领域，提供了与企业服务-差旅相关的各项工具，支持查询出差申请列表和详情、差旅酒店、火车、飞机订单的列表和详情等功能",
      "type": "sse",
      "url": "https://bz6wsb3g.mcp.bytedance.net/sse"
    }
  },
  "mcpToSkill": true
}
```
<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | DtEwdDHVOolHHox35p3cLlfgnBc -->
SKILL.md
<!-- END_BLOCK_38 -->

<!-- BLOCK_39 | HrAZdlEAdohhAbxjFSicO9EAn8c -->
```yaml
---
name: bytedance-knowledge-travel
description: 字节跳动企业服务开发技能，支持从字节云文档中心、飞书文档、Oncall工单、ByteTech、代码仓库、日志、应用中心资产、Meego需求、研发流程数据等知识源检索内容，支持联网搜索；同时提供企业服务-差旅相关工具，可查询出差申请、差旅酒店/火车/飞机订单等信息。
---

使用提供的工具完成任务：
根据用户需求，必须优先调用提供的工具获取信息并提供帮助
```
<!-- END_BLOCK_39 -->



<!-- BLOCK_40 | LxKkdELKUoyJDlxVq1Fcya8fndg -->
**测试效果**
<!-- END_BLOCK_40 -->

<!-- BLOCK_41 | WgFZdhSk1oq2soxHTe5cdVGznxd -->
https://aime.bytedance.net/share/348078d5-0fff-4364-be7e-3737727f8b49
<!-- END_BLOCK_41 -->

<!-- BLOCK_42 | Mq2AdkDe9oGVX2xqgHscsnEdnWh -->
自动生成mcp的skill reference 文档，如下
<!-- END_BLOCK_42 -->

<!-- BLOCK_43 | YBEgdeYk2o4jKFxDSrvcFtrOn9k -->
![图片](img_UPQObBzSdouq7pxlrpCcC149nag.png)
<!-- END_BLOCK_43 -->

<!-- BLOCK_44 | OhTedbkzQojDy1xDfnUc8SaonSd -->
![图片](img_D4OJbB82XobkRdx67xQcjoJEnIf.png)
<!-- END_BLOCK_44 -->



<!-- BLOCK_45 | doxcnPtZH7J2NKx2HUEBsdRfTVf -->
## 目录结构<!-- END_BLOCK_45 -->

<!-- BLOCK_46 | doxcntawaTzI6iOo54zYwpTyqec -->
```
your-skill/
├── .aime/
│   ├── mcp.json              # MCP 配置文件
│   └── setup/
│       └── setup.sh          # 可选的初始化脚本
├── references/
│   └── MCP_TOOLS.md          # 自动模式时，自动生成的工具文档
├── scripts/
│   └── call_mcp_tool.py      # 自动模式时，自动生成的调用脚本
├── SKILL.md
└── ...
```
<!-- END_BLOCK_46 -->



<!-- BLOCK_47 | doxcnq0r3Bxlv6pM1RhBP8xDUAb -->
## 使用模式详解<!-- END_BLOCK_47 -->

<!-- BLOCK_48 | T0didtbrPoPR3Kx0eAgcOz3Cnuc -->
- **手动模式（"mcpToSkill": false）**：
	- MCP 不直接暴露给模型，而是藏在一个统一的工具 `skill_mcp_{skill_name}` 后面，由你在 Skill 或外部代码里显式调用具体 MCP 工具，调用顺序、次数、参数都由你控制
	- 完全懒加载：没调用就不会初始化 MCP，有助于控制长尾工具对整体性能和稳定性的影响。
	- 当工具数量多、参数复杂时，全靠你手写和维护说明，易漏、易不一致。
<!-- END_BLOCK_48 -->

<!-- BLOCK_49 | UiBEdypkgoMHamxUBM7ca6L7np9 -->
- **自动模式（"mcpToSkill": true）**：
	- 平台根据 `.aime/mcp.json` 里的 MCP 配置，自动生成一份工具说明文档 `references/MCP_TOOLS.md` 和调用脚本 `scripts/call_mcp_tool.py`，Agent 先“读文档”再按文档说明去调用脚本来使用 MCP 工具，Agent 对工具的选择和调用会更自主
	- 因为要生成文档和脚本，会在 Skill 激活时对 MCP 做统一扫描；如果 MCP 工具极多，初始化时会有一次性成本，但好处是后续调用有完整文档可查，还能结合 `enabledTools` 做白名单过滤。
<!-- END_BLOCK_49 -->



<!-- BLOCK_50 | doxcnj1HP0EKhZXLrM1qZOLouMc -->
### 手动模型（默认）<!-- END_BLOCK_50 -->

<!-- BLOCK_51 | doxcnEmrA0VkvkHba0Urjb2oiee -->
自己调用 MCP 工具，工具名格式：`skill_mcp_{skill_name}`
<!-- END_BLOCK_51 -->

<!-- BLOCK_52 | doxcn2D1rj3olWLg303dNjwpxGg -->
**工作流程原理：**
<!-- END_BLOCK_52 -->

<!-- BLOCK_53 | doxcnhTDij7s4zWI4C3WJTjbG3c -->
![board_IZuQwYRN0hrvN1bb9NxcEMp5nge](board_IZuQwYRN0hrvN1bb9NxcEMp5nge.drawio)
<!-- END_BLOCK_53 -->

<!-- BLOCK_54 | doxcnHvCGN0rK3olEhESHJpQXnf -->
**特点：**
<!-- END_BLOCK_54 -->

<!-- BLOCK_55 | doxcnwDGw1oii6YKtuwVrc7Pqrh -->
- 懒加载：首次调用时才连接 MCP 服务器
<!-- END_BLOCK_55 -->

<!-- BLOCK_56 | doxcnhZO7byQpgltx3MpEUHUPee -->
- 完全自己控制自己的 mcp 行为
<!-- END_BLOCK_56 -->

<!-- BLOCK_57 | Tc1tdTLHcowEz0xprjAcF0o4nsw -->
使用方式例子
<!-- END_BLOCK_57 -->

<!-- BLOCK_58 | F42qdzLaFobLIBxneGTcYKsfnsh -->
```python
#!/usr/bin/env python3
import os
import sys
import json

from byted_aime_sdk import call_aime_tool

# call_aime_tool(toolset, tool_name, params)
# 第一个参数：固定 skill_mcp_   你的 skill name
# 第二个参数：工具名称（如 "online_search"）
# 第三个参数：工具参数
result = call_aime_tool("skill_mcp_${skill_name}", "online_search", {
    "query": "Python best practices"
})
print(json.dumps(result, ensure_ascii=False, indent=2))
```
<!-- END_BLOCK_58 -->



<!-- BLOCK_59 | doxcn6EuiLS5TUi1JijiLdDkksf -->
### 自动模式（mcpToSkill doc）<!-- END_BLOCK_59 -->

<!-- BLOCK_60 | doxcnc1jesymvcMOTd5itzi2pab -->
Agent 通过阅读文档和执行脚本来使用 MCP 工具。
<!-- END_BLOCK_60 -->

<!-- BLOCK_61 | doxcn5llGUyRmRs1l7apGecShGc -->
**配置：**
<!-- END_BLOCK_61 -->

<!-- BLOCK_62 | doxcn3FUfQk7OKINkjmEMvylmbg -->
```json
{
  "mcpServers": { ... },
  "mcpToSkill": true
}
```
<!-- END_BLOCK_62 -->

<!-- BLOCK_63 | doxcnQMMU8zkDWmB9c6MOHzotTc -->
**工作流程原理：**
<!-- END_BLOCK_63 -->

<!-- BLOCK_64 | doxcnvdoA8xPJzgEcufUd0CAjfg -->
![board_SF8ZwatKThIrTNbchDicgPd2nHb](board_SF8ZwatKThIrTNbchDicgPd2nHb.drawio)
<!-- END_BLOCK_64 -->

<!-- BLOCK_65 | doxcn0jF3ty4GkCsPwRawNQAzGc -->
**生成的文件：**
<!-- END_BLOCK_65 -->

<!-- BLOCK_66 | doxcnGEhRbd56nJJVRDDnrK1aob -->
1. **references/MCP_TOOLS.md** - 工具文档
	- 所有工具的名称和描述
	- 参数说明（名称、类型、是否必填）
	- 调用方式说明
<!-- END_BLOCK_66 -->

<!-- BLOCK_67 | doxcniVvMtwD5YBoBcKVglGI6eg -->
2. **scripts/call_mcp_tool.py** - 调用脚本
	- 命令行调用方式
	- SDK 导入示例
<!-- END_BLOCK_67 -->

<!-- BLOCK_68 | doxcnb6fsHlVFWIFTmIslxhU0wh -->
**调用方式：**
<!-- END_BLOCK_68 -->

<!-- BLOCK_69 | doxcnM7T5xJhMG1LdaxGR2Ie7fh -->
```bash
# 方式一：命令行
python scripts/call_mcp_tool.py <tool_name> '{"param": "value"}'

# 方式二：SDK， xxx为 skill name
from aime_client import call_aime_tool
result = call_aime_tool("skill_mcp_xxx", "tool_name", {"param": "value"})
```
<!-- END_BLOCK_69 -->

<!-- BLOCK_70 | doxcnuGstsZ2CGTFGAe0BfKumMe -->
**适用场景：**
<!-- END_BLOCK_70 -->

<!-- BLOCK_71 | doxcnBZvtbBjvMh1v4V1v7iL1Gb -->
- 工具数量多，需要详细文档
<!-- END_BLOCK_71 -->

<!-- BLOCK_72 | doxcnI40P7bdFlM5lWTkgXBlxTf -->
- 参数复杂，需要参考说明
<!-- END_BLOCK_72 -->

<!-- BLOCK_73 | doxcnIszm24U5EfSnRUWK3ni7ud -->
- 希望 Agent 有更多控制权
<!-- END_BLOCK_73 -->



<!-- BLOCK_74 | doxcnzgUxLQe5IKfI7CkiTvfhhd -->
## 与平台 MCP 的关系<!-- END_BLOCK_74 -->

<!-- BLOCK_75 | doxcnJJO3fdGYVc7ETTqBUxBaXc -->
Skill MCP 是独立于平台全局 MCP 的：
<!-- END_BLOCK_75 -->

<!-- BLOCK_76 | doxcnVlx178fQo6J2c6XkPNrd9g -->
<table header-row="true" col-widths="120,238,360">
    <tr>
        <td>特性</td>
        <td>Skill MCP</td>
        <td>平台 MCP</td>
    </tr>
    <tr>
        <td>作用域</td>
        <td>仅当前 Skill，不直接注册到模型的funcation call</td>
        <td>全局</td>
    </tr>
    <tr>
        <td>生命周期</td>
        <td>随 Skill 激活</td>
        <td>持续可用</td>
    </tr>
    <tr>
        <td>配置位置</td>
        <td>`.aime/mcp.json`</td>
        <td>平台配置</td>
    </tr>
</table>
<!-- END_BLOCK_76 -->

<!-- BLOCK_77 | doxcn7NNWup5amHgZZVZ8l6SpZd -->
## 配置详解<!-- END_BLOCK_77 -->

<!-- BLOCK_78 | doxcnmjwTxW1FqUewMZTIpk1mec -->
```json
{
  "mcpServers": {
    "server-name": {
      "description": "服务器用途描述",
      "type": " sse | streamable-http | cloud-sdk",
      "command": "启动命令（stdio）",
      "args": ["参数列表"],
      "env": { "环境变量": "值" },
      "url": "服务器地址（sse/streamable-http）",
      "psm": "PSM 标识（cloud-sdk）",
      "header": { "请求头": "值" },
      "timeout": 300,
      "enabledTools": ["tool1", "tool2"]
    }
  },
  "mcpToSkill": false
}
```
<!-- END_BLOCK_78 -->

<!-- BLOCK_79 | LLP2dgxHGopRXCxVLlic5Mt4nWz -->
<table header-row="true" col-widths="120,80,60,554">
    <tr>
        <td>字段</td>
        <td>类型</td>
        <td>必填</td>
        <td>说明</td>
    </tr>
    <tr>
        <td>`mcpServers`</td>
        <td>object</td>
        <td>是</td>
        <td>MCP 服务器配置，key 为服务器名称</td>
    </tr>
    <tr>
        <td>`mcpToSkill`</td>
        <td>boolean</td>
        <td>否</td>
        <td>是否启用文档模式，默认 `false`</td>
    </tr>
</table>
<!-- END_BLOCK_79 -->

<!-- BLOCK_80 | EIkrdAqoooEZRwxEeWtcGUarnvh -->
<table header-row="true" col-widths="147,147,120,494">
    <tr>
        <td>字段</td>
        <td>类型</td>
        <td>必填</td>
        <td>说明</td>
    </tr>
    <tr>
        <td>`description`</td>
        <td>string</td>
        <td>推荐</td>
        <td>服务器用途描述</td>
    </tr>
    <tr>
        <td>`type`</td>
        <td>string</td>
        <td>否</td>
        <td>连接类型，可自动推断</td>
    </tr>
    <tr>
        <td>`command`</td>
        <td>string</td>
        <td>stdio 必填</td>
        <td>启动命令</td>
    </tr>
    <tr>
        <td>`args`</td>
        <td>string[]</td>
        <td>否</td>
        <td>命令参数</td>
    </tr>
    <tr>
        <td>`env`</td>
        <td>object</td>
        <td>否</td>
        <td>环境变量</td>
    </tr>
    <tr>
        <td>`url`</td>
        <td>string</td>
        <td>sse/http 必填</td>
        <td>服务器地址</td>
    </tr>
    <tr>
        <td>`psm`</td>
        <td>string</td>
        <td>cloud-sdk 必填</td>
        <td>字节云 PSM</td>
    </tr>
    <tr>
        <td>`header`</td>
        <td>object</td>
        <td>否</td>
        <td>HTTP 请求头</td>
    </tr>
    <tr>
        <td>`timeout`</td>
        <td>number</td>
        <td>否</td>
        <td>超时秒数，默认 1800</td>
    </tr>
</table>
<!-- END_BLOCK_80 -->

<!-- BLOCK_81 | doxcnwPJN6cFvlB738IUnYsMvif -->
`enabledTools`string[]否启用的工具列表（白名单）。为空时启用全部工具，配置后仅启用列表中的工具。适用于 MCP 服务器工具过多时精确控制，仅仅需要`mcpToSkill` 为 true时配置，否则不需要配置，本身就是懒加载
<!-- END_BLOCK_81 -->

<!-- BLOCK_82 | V4KjdcsQ9odc3jx6HhWcv1PxnHb -->
<callout icon="watermelon" bgc="2" bc="2">
注意：不支持 stdio 类型指定的本地 MCP
</callout>
<!-- END_BLOCK_82 -->

<!-- BLOCK_83 | LA7sdSrBNoOSBlx8GE7cbpPdnZL -->
<table header-row="true" col-widths="128,170,620">
    <tr>
        <td>连接类型</td>
        <td>说明</td>
        <td>例子</td>
    </tr>
    <tr>
        <td>~~stdio~~</td>
        <td>~~通过标准输入输出通信，适用于本地命令行工具。~~</td>
        <td>```json
~~{~~
~~&nbsp;&nbsp;"mcpServers": {~~
~~&nbsp;&nbsp;&nbsp;&nbsp;"filesystem": {~~
~~&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description": "文件系统操作",~~
~~&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"type": "stdio",~~
~~&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"command": "npx",~~
~~&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]~~
~~&nbsp;&nbsp;&nbsp;&nbsp;}~~
~~&nbsp;&nbsp;}~~
~~}~~
```</td>
    </tr>
    <tr>
        <td>sse</td>
        <td>通过 Server-Sent Events 通信，适用于远程服务。</td>
        <td>```json
{
  "mcpServers": {
    "remote-api": {
      "description": "远程 API 服务",
      "type": "sse",
      "url": "https://api.example.com/mcp/sse",
      "header": {
        "Authorization": "Bearer your-token"
      }
    }
  }
}
```</td>
    </tr>
    <tr>
        <td>streamable-http</td>
        <td>通过 HTTP Streaming 通信。</td>
        <td>```json
{
  "mcpServers": {
    "http-service": {
      "description": "HTTP 流式服务",
      "type": "streamable-http",
      "url": "https://api.example.com/mcp"
    }
  }
}
```</td>
    </tr>
    <tr>
        <td>cloud-sdk</td>
        <td>通过字节云 CloudSDK 连接，自动处理认证。</td>
        <td>```json
{
  "mcpServers": {
    "internal-service": {
      "description": "字节内部服务",
      "type": "cloud-sdk",
      "psm": "bytedance.mcp.your_service"
    }
  }
}
```</td>
    </tr>
    <tr>
        <td>不指定 `type` 时，系统按以下规则推断</td>
        <td>自动推断</td>
        <td>- `command`：stdio
- `psm`：cloud-sdk
- `url`：sse</td>
    </tr>
</table>
<!-- END_BLOCK_83 -->



<!-- BLOCK_84 | doxcn0IHvToLjgDN6P8oIBshBdc -->
## 工具过滤（enabledTools）<!-- END_BLOCK_84 -->

<!-- BLOCK_85 | doxcnglechdmyfxrgzT4Dv7Yrfc -->
当 MCP 服务器提供的工具数量过多时，可以使用 `enabledTools` 配置来精确控制启用哪些工具。
<!-- END_BLOCK_85 -->

<!-- BLOCK_86 | doxcnXnH8Dt78DpDYKOapNHUqdf -->
### 使用场景<!-- END_BLOCK_86 -->

<!-- BLOCK_87 | doxcnqoKQlVnwN77I0DjOwj7X7e -->
<callout icon="bulb" bgc="5" bc="1">
**适用于以下场景：**
- MCP 服务器工具数量超过 10 个，只需要使用其中部分
- 避免工具过多导致上下文膨胀
- 精确控制 Skill 的能力边界
仅仅需要 `mcpToSkill` 为 true 时配置，否则不需要配置，本身就是懒加载
</callout>
<!-- END_BLOCK_87 -->

<!-- BLOCK_88 | doxcnJqlpJAje9VRw6SdZH3MGcc -->
### 配置示例<!-- END_BLOCK_88 -->

<!-- BLOCK_89 | doxcnKVs16BAXEF7t3DNdEEa61e -->
```json
{
  "mcpServers": {
    "large-mcp-server": {
      "description": "包含很多工具的 MCP 服务器",
      "type": "sse",
      "url": "https://example.com/mcp/sse",
      "enabledTools": ["search", "query", "get_detail"]
    }
  },
  "mcpToSkill": true
}
```
<!-- END_BLOCK_89 -->

<!-- BLOCK_90 | doxcnApSP84pYjeAxdZiiKjQSwb -->
### 行为说明<!-- END_BLOCK_90 -->

<!-- BLOCK_91 | doxcnkfSCFMsq7od4LpuwbcVqhh -->
<table header-row="true" col-widths="350,350">
    <tr>
        <td>配置情况</td>
        <td>行为</td>
    </tr>
    <tr>
        <td>`enabledTools` 未配置或为空</td>
        <td>启用该服务器的**所有工具**</td>
    </tr>
    <tr>
        <td>`enabledTools` 配置了工具列表</td>
        <td>仅启用列表中指定的工具</td>
    </tr>
</table>
<!-- END_BLOCK_91 -->

<!-- BLOCK_92 | doxcnn9ofi758tOedXI1hfsP20f -->
<callout icon="gift" bgc="3" bc="1">
**注意**：`enabledTools` 中的工具名称必须与 MCP 服务器返回的工具名称完全匹配（区分大小写）
</callout>
<!-- END_BLOCK_92 -->




</content>
