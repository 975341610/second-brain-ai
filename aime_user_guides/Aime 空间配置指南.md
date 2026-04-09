<title>Aime 空间配置指南</title>
<url>https://bytedance.larkoffice.com/wiki/R8YIw8XXLixg3okhYfpcSv4Zn3g</url>
<content>
<!-- BLOCK_1 | Serqdg67KoMuXGx5PKKcW6oFn8g -->
<callout icon="bulb" bgc="2" bc="2">
空间配置是释放 Aime 团队协作与空间任务执行潜力的关键。通过精准配置空间 “资源”与“技能”，你可以将分散的内部平台、代码仓库、文档库与任务规范整合为 Aime 可理解、可调用的信息，从而显著提升业务场景下执行任务的准确性、稳定性与效率。
推荐阅读：[Aime Skill 功能使用指南](https://bytedance.larkoffice.com/docx/UaxTdbzVnoyxGYxtlLecQPhlnNb)
</callout>
<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | IEi8dWN3JovkNrxFMhLcEdhMnFd -->
## 关键信息与注意事项<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | I6cKd1J4aoaAFCxlNC7c4r4pnab -->
- **概念边界**：
	- **资源**：分为信息源与平台两大类，Aime 通过连接这些资源进行跨平台异构信息的深度检索、分析和联动。
		- 信息源：指代码仓库、TCE 服务、测试用例、文档库等事实性“信息源” （注：个人空间暂时仅支持配置文档库资源，后续将逐步支持开发配置其他类型资源）
		- 平台：指 Meego、Bits 等可双向触发功能联动的“平台”
	- **技能**：指用户自定义的“指导规则”，是任务执行时具有最高优先级的行为准则。它告诉 Aime“应该怎么做”，更侧重于流程、规范和约束。
<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | Xx7wdkllHoUcVrx6ObUcYfvPn8g -->
- **同步与安全**：
	- **更新机制**：文档库资源将根据文档修改情况自动定时更新，也支持手动更新。引用的云文档内容变更后，也建议手动触发更新，以保证信息同步。
	- **权限风险**：文档库中的文档导入后会授权给 Aime 离线处理，导入后空间内所有成员可消费文档内容，可能存在数据越权的风险。请在导入前评估文档内容的敏感性，谨慎操作。
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | EwLddFGGJoGc4MxEYjncsKf1nIv -->
- **权限与可见性**：
	- **资源配置**：空间管理员与成员均可配置和导入各类资源。但请注意，部分资源（如代码仓库、TCE 服务）在创建 Aime 任务消费时，Aime 会校验当前操作者的个人权限以提供服务。
	- **技能配置**：空间管理员可以创建“空间公开”的技能，默认对所有空间成员启用；普通成员只能创建“个人可见”的技能。用户可自行选择是否要启用或停用某条技能。
<!-- END_BLOCK_5 -->



<!-- BLOCK_6 | T8VqdGTDroQt73xzdggc917TntI -->
## 快速上手<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | H3KudV43ToxbDyxuubBcUmuanme -->
> 本章节将引导你完成空间配置的核心流程。
> 
<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | AZkPddHsPor8KmxHgrpcVv3xnDd -->
### 步骤一：进入配置页面<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | JaQidNzw7o9ZP6xutm1czD9tnkb -->
在 Aime 首页，选择你的目标空间，并单击空间名称右侧的 **配置** 按钮，即可进入空间的基础信息配置页面。仅管理员可操作，普通成员仅可查看空间的基本信息。
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | DrPldyawvos5pjx2SYTc0j6gnhg -->
![图片](img_A4GmbUzNOon08BxJZivcD9elnCN.png)
<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | WniFdrtSdo3pp3xfhOFchKqIncg -->
### 步骤二：资源配置<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | BqEhdTH7Qo54pxxmchgc4cyYnug -->
> 资源是希望 Aime 在执行任务时能够访问和理解的外部信息源。合理的资源配置是提升任务质量的基础。
> 
<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | CTmMdDtHyoBZtWxDSKPccjfXnre -->
![图片](img_O7Wbb2wkOoQh0CxVst0cphXUnid.png)
<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | U8FpdNPnjoZswfx9PoocuHwpnKd -->
点击左侧导航栏中的 **资源配置** 。根据你的团队需求，连接项目相关的代码仓库、TCE 服务、Meego 空间、测试用例库和文档库。（注：个人空间暂时仅支持配置文档库与风神资源，后续将逐步支持开发配置其他类型资源）
<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | PI41dVMd6oPbSvx5uufcx5gXnvf -->
<table header-row="true" col-widths="100,169,250,250,250">
    <tr>
        <td>**资源类型**</td>
        <td>资源名称</td>
        <td>字段说明与操作</td>
        <td>配置权限要求</td>
        <td>常见问题与最佳实践</td>
    </tr>
    <tr>
        <td rowspan="6">**信息源**</td>
        <td>**文档库**</td>
        <td>支持上传或链接飞书文档以及 Wiki 知识库
Aime 会将其作为背景信息，在任务执行的过程中基于文档信息切片触发检索。</td>
        <td>录入人需要具备文档的访问权限。
上传的文档会转存并切片，空间内所有成员均可检索，存在越权风险，请谨慎评估。</td>
        <td>**最佳实践**：
- 在指令中通过“根据知识库/文档 xxx”来主动触发，以提升命中准确性
- 避免导入大量低质量、过期的文档，这会干扰检索结果。
- 文档库支持自动更新，但重要变更后建议**手动更新**以保证时效性。</td>
    </tr>
    <tr>
        <td>**代码仓库**</td>
        <td>填入 Git 仓库地址。
Aime 将能够理解代码结构、分析代码功能，并用于代码生成、修复、影响面分析等多种研发场景。</td>
        <td>录入人需要具备该代码仓库的 `clone` 权限。</td>
        <td>**最佳实践**：优先添加团队核心业务相关的代码仓库。对于大型单体仓库，确保 Aime 能够访问你关心的主要模块。</td>
    </tr>
    <tr>
        <td>**TCE 服务**</td>
        <td>填入服务的 PSM 名称。
Aime 可以获取服务的接口定义、调用关系、SCM 信息和线上调用链，用于 LogID 排障、接口稳定性分析等。</td>
        <td>录入人需要具备该 TCE 服务的**可读**权限。</td>
        <td>**常见问题**：如果服务信息不全，请检查你的 TCE 权限是否正确。</td>
    </tr>
    <tr>
        <td>**Meego**</td>
        <td>粘贴 Meego 空间或特定工作项的 URL 进行关联。
Aime 可以理解需求、缺陷等信息，并与研发任务联动。</td>
        <td>录入人需要具备对应 Meego 空间的**访问权限**并完成授权。</td>
        <td>**最佳实践**：将整个团队的 Meego 主空间进行关联，而非零散的工作项，以保证信息覆盖的全面性。</td>
    </tr>
    <tr>
        <td>**测试用例**</td>
        <td>填入 Bits 测试用例库的空间地址。
Aime 可以学习现有的测试用例，从而在面对新需求时生成更贴切、更完备的测试用例。</td>
        <td>录入人需要具备该 Bits 空间的**阅读**权限。</td>
        <td>**最佳实践**：导入覆盖核心业务流程的测试用例库，有助于 AI 更好地理解业务逻辑。</td>
    </tr>
    <tr>
        <td>**风神**</td>
        <td>**支持导入风神仪表盘或可视化查询的 URL。**
Aime 会每日前置更新数据，用于在数据问答场景中快速响应。</td>
        <td>录入人需具备对应仪表盘/查询的**访问权限**并完成登录授权。
- 暂不支持录入未保存的可视化查询
会根据导入人权限从风神<font background_color="light_blue">提前下载</font>看板图表数据。</td>
        <td>**最佳实践**：优先导入日常高频使用的、固定的数据看板，以便 Aime 分析和加速，进行每日异常分析，相关性分析等。</td>
    </tr>
    <tr>
        <td>**平台配置**</td>
        <td>**Meego**</td>
        <td>复制 Meego 项目链接以关联 Meego，通过 Meego 平台 Aime 官方插件获取全部需求和缺陷流转信息。在 Aime 配置不同节点的绑定模板后可通过绑定的模版一键发起任务。</td>
        <td>录入人需要具备 Meego 空间的访问权限。</td>
        <td>**最佳实践：**
- 在需求设计节点配置关联 Aime PRD 设计/review 模板，帮助查漏补缺、提供建议
- 技术开发节点，结合代码仓库和历史技术方案，生成符合团队技术栈和开发规范的前端技术方案，包含架构设计、技术选型、实现细节等</td>
    </tr>
</table>
<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | GBp2diIH8orC8dxUlObc0Sb2nic -->
<grid cols="2">
<column width="46">
  ![图片](img_ADbAbZiEAoJIdYxzXV5cbvdhnDc.png)
</column>
<column width="53">
  ![图片](img_IjSMbiGYYokIsXxE8XVc60cunPh.png)
</column>
</grid>
<!-- END_BLOCK_16 -->



<!-- BLOCK_17 | Ok7ZdVPWjoEuBqxrnBycQBCZnsh -->
### 步骤三：技能配置<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | Ke9ldobq5oFz5OxOoAyclMaqnyc -->
> “Skill 技能”是你为 Aime 设定的、具有**最高优先级**的指导规则。它与“文档库”资源的核心区别在于：
> 
> - 文档库（被动检索）：如同一个庞大的图书馆，Aime 会将文档内容切片处理后，在需要时根据任务语义去“搜索”相关信息作为参考。它回答的是“是什么”的问题。
> 
> - 用户自定义技能（主动遵循）：<font background_color="medium_gray">如同下达给 Aime 的“军规”，只要满足触发条件，Aime 就必须“遵循”其内容执行任务</font>。它回答的是“应该怎么做”的问题。
> 
> **<font background_color="light_red">功能使用与最佳实践指南：</font>**[Aime Skill 功能使用指南（0318上线）](https://bytedance.larkoffice.com/docx/UaxTdbzVnoyxGYxtlLecQPhlnNb)
> 
<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | UeeIdeZZJoKXJCxrZRGcqOddnpe -->
<grid cols="2">
<column width="28">
  ![图片](img_IzdXbXfXNoGtYbxh5TYcznoSnSc.png)
</column>
<column width="71">
  侧边栏切换到 **技能配置**。在这里，你可以将团队的工作流程、业务规范、特殊指令等沉淀为结构化的技能。
  通过配置技能，你可以约束和引导 Aime 的行为，使其更符合团队规范。
</column>
</grid>
<!-- END_BLOCK_19 -->

<!-- BLOCK_20 | YcsGdDP85o88u4xnhWIcz7m1nQe -->
<table header-row="true" col-widths="104,282,584">
    <tr>
        <td>配置项</td>
        <td>字段说明与操作</td>
        <td>最佳实践或说明</td>
    </tr>
    <tr>
        <td>**名称**</td>
        <td>上传 SKILL.md 时将根据 zip 字段解析，请前往 zip 中修改</td>
        <td>- 字符数上限 50
- **示例**：“代码提交规范”、“业务知识”、“全局任务通用规则”……
<grid cols="2">
<column width="50">
  - Goodcase：
  	- 代码评审要点清单-Android
  	- 长文分块-规范类
</column>
<column width="50">
  - Badcase：
  	- 代码评审要点清单
  	- 长文处理
</column>
</grid></td>
    </tr>
    <tr>
        <td>**指令**</td>
        <td>填写规则的具体描述。支持上传附件（[skill.zip](https://bytedance.larkoffice.com/wiki/BSVVwNRRdi6TDSkTHJNcUDiznbe)）或引用飞书云文档。
**这是技能的核心，需要清晰、准确。**
<grid cols="2">
<column width="70">
  注：飞书云文档 & Git 导入类型将自动检测文档更新的情况保持同步更新，若有即时更新的需求，请点击 “… - 更新” 
</column>
<column width="30">
  ![图片](img_ZLihbuHMmoVOnmxYGVrc5j4Rnac.png)
</column>
</grid></td>
        <td>- 内容的表述需要清晰、明确
- 飞书云文档后续将停止维护，建议通过 skill.md 主流方式录入维护 skill
	- 无研发基础的同学可以尝试 @aime-skill-creator 或与 [Aime 个人助理](https://aime.bytedance.net/assistant) 直接对话，用自然语言完整描述需求，让 Aime 帮你完成技能创建、编辑与管理维护～
![图片](img_R6XTb7NSco0oBLx4KzbcHASUnKh.png)</td>
    </tr>
    <tr>
        <td>**描述**
description</td>
        <td>定义这条技能在何种情况下被触发，具备什么样的能力，供模型参考。
上传 SKILL.md 时将自动解析填写，建议在 SKILL.md 中前置完善并明确</td>
        <td>**手动编写示例**：
- `当任务是“代码审查”或“Code Review”时` (关键词触发)
- `当任务涉及到修改数据库表结构时` (场景描述触发)
**最佳实践**：`use_when` 的描述应尽可能精准，避免过于宽泛导致不相关的任务也命中规则。
<grid cols="2">
<column width="62">
  - Goodcase：
  	- 当需要查询抖音 Meego 需求的排期节点或估分信息时；输入包含需求ID或链接
  	- 当编写周报并需要自动生成结构化提纲（包含目标、进展、风险）时；适用个人或团队周报
</column>
<column width="37">
  - Badcase：
  	- 需要查询排期
  	- 写周报
</column>
</grid></td>
    </tr>
    <tr>
        <td>**可见范围**
（仅项目空间内有区分）</td>
        <td>- **空间公开**：对项目空间内所有成员可见并生效。（仅管理员可创建）
- **个人可见**：仅对创建者本人可见并生效</td>
        <td>- 团队通用的规范（如研发流程、部署手册）适合设为“空间公开”
- 个人工作习惯或临时调试性指令则建议设为“个人可见”</td>
    </tr>
    <tr>
        <td>**启停**</td>
        <td>- **启/停**：所有用户都可以对选择启用或弃用空间内配置的技能，以调节任务效果</td>
        <td>- 空间公开的技能将默认设置对全员启用，用户可自行判断是否停用/启用
- 对于暂时用不到或已过期的技能，应及时停用或删除，避免对任务产生干扰</td>
    </tr>
    <tr>
        <td>**技能检测**</td>
        <td>- **检测机制**：保存时会进行安全、冲突、重复、过期检测</td>
        <td>导入失败时，系统会明确提示失败原因，请根据提示调整后重新提交。</td>
    </tr>
</table>
<!-- END_BLOCK_20 -->



<!-- BLOCK_21 | ATOmdRuMloNtEFxluXHcAzjtnMb -->
## 常见问题 (FAQ)<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | HuVrdQtttozQVlx1Pp2cwKmjnJh -->
**Q:&nbsp;技能规则在什么时候被检测？我如何知道是否生效？**
<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | TKgYdVPzco8XwQxGW4yc6QVknKe -->
**A:** 技能的冲突、重复等检测主要发生在**创建和编辑保存时**。如果检测失败，你会在页面上收到明确的失败原因提示。任务执行时，Aime 会根据 `use_when` 场景自动匹配并应用相关规则。你可以在任务结果详情页的 Aime 执行过程中，查看“本次命中的技能/规则”信息，确认规则是否已按预期生效。
<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | VB5PdcMDLotLQCxWBSucuILunyg -->
![图片](img_CGTQbPO2WoPdD9x0uZFczHX8nVb.png)
<!-- END_BLOCK_24 -->



<!-- BLOCK_25 | XqmwdQ1XdoTcokxBd2DcW8UAnrh -->
**Q: 我更新了文档库里的飞书文档，Aime 会立刻知道吗？**
<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | R1dmd5ERgoOvJIxpU1LcCC1Inyq -->
**A:** 不会立刻知道。文档库的同步有一定延迟（默认检测文档的更新情况每日自动更新以保持同步）。如果你的文档内容有重要更新，并希望立即在 Aime 任务中生效，建议进入 **资源配置** -> **文档库 /&nbsp;技能配置**，找到对应的文档，并点击 **手动更新** 按钮。
<!-- END_BLOCK_26 -->



<!-- BLOCK_27 | VPr0ddqs3ovHtmxqIBZcD1ROnVc -->
**Q：在有多条具有层级结构的技能期望录入的场景下我应该如何录入技能？**
<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | CMccduPd5ojhMfxHMfhcdN7Knmh -->
A：目前有两种方式可以按需尝试。
方案一：可以使用飞书文档作为主目录索引来承载具有层级的多条技能。详情 & 示例可参考：[Aime 知识：使用飞书文档分层管理知识](https://bytedance.larkoffice.com/wiki/GgNlw49KmiJ7uCkcDnWcY79OnSf)
方案二：通过 skill.zip 形式上传结构化的技能文件信息，详细可参考：[Aime Skill 指南](https://bytedance.larkoffice.com/wiki/BSVVwNRRdi6TDSkTHJNcUDiznbe)
<!-- END_BLOCK_28 -->



<!-- BLOCK_29 | C9fcdJa3howYbYxrahccvnzmnJf -->
**Q: 为什么我和同事在同一个项目空间，使用同一个任务指令，但 Aime 检索到的代码或文档内容不同？**
<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | GQfud8aSooRUMexpSCMcIv6MnXg -->
**A:** 这是因为 Aime 在访问部分资源（如代码仓库、TCE 服务、链接形式的飞书文档）时，会模拟**当前操作者**的身份进行访问，并遵守其个人权限。如果你的同事没有某个代码仓库的 `clone` 权限，那么即使该仓库已在资源中配置，他在执行任务时也无法读取其中的内容。
<!-- END_BLOCK_30 -->



<!-- BLOCK_31 | ZcITdyiDDoaTSixRKzacNNfgnGh -->
**Q: 文档库和技能配置里的“引用云文档”有什么区别？**
<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | OTZDdJJ0Wowg62xpxMGcSuLHnwf -->
**A:** **文档库**是**被动检索**的背景信息源，Aime 会根据任务语义去“搜索”相关内容，适合存放大量、分散的参考资料（如团队 Wiki）。而**技能配置**中的“引用云文档”是**主动应用**的指导规则，具有最高优先级，只要触发条件满足，Aime 就会“遵循”其内容，适合存放必须严格遵守的规范和流程（如“发布流程手册”）。
<!-- END_BLOCK_32 -->



<!-- BLOCK_33 | M9wfdvXkfovFMDxHvMycsfi6n0f -->
**Q: 多条技能很相似时如何处理？**
<!-- END_BLOCK_33 -->

<!-- BLOCK_34 | EJ7kdGMAloKwTPxKAGQcTaGfnKf -->
**A:** 录入时明确每条技能的使用时机， 尽量不要重合，不要模糊表述。可依据“使用时机边界、受众/范围、输入输出差异”进行拆分与去重；同时，考虑到技能的数量限制，建议可将跨场景公共步骤抽为一条“基础技能”供复用
<!-- END_BLOCK_34 -->



<!-- BLOCK_35 | FWtAd4LICoByl3xGuvBcW9pznad -->
## 附录<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | L12JdzNcHoT1pGxM5wQcJYvYnuf -->
### 资源配置字段总览<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | LheCd5ztvodwTAxJ6GBcWq8VnRA -->
<table header-row="true" col-widths="102,239,479">
    <tr>
        <td>资源类型</td>
        <td>主要配置字段</td>
        <td>格式要求/示例</td>
    </tr>
    <tr>
        <td>代码仓库</td>
        <td>Git 仓库地址</td>
        <td>`https://git.bytedance.net/group/repo.git`</td>
    </tr>
    <tr>
        <td>TCE 服务</td>
        <td>PSM (Product, Service, Module)</td>
        <td>`P.S.M.example-service`</td>
    </tr>
    <tr>
        <td>Meego</td>
        <td>Meego 空间或工作项 URL</td>
        <td>`https://meego.larkoffice.com/space/home/xxx`</td>
    </tr>
    <tr>
        <td>测试用例</td>
        <td>Bits 测试用例库空间地址</td>
        <td>`https://bits.bytedance.net/space/12345`</td>
    </tr>
    <tr>
        <td>文档库</td>
        <td>飞书文档/表格/Wiki 链接或文件上传</td>
        <td>`https://bytedance.larkoffice.com/wiki/xxxxxxxx`</td>
    </tr>
</table>
<!-- END_BLOCK_37 -->



<!-- BLOCK_38 | X6okdzkfYo4c4bxsPVCcCmFgnud -->
## 问题反馈<!-- END_BLOCK_38 -->

<!-- BLOCK_39 | XRYHdQSNuoG4Ifx0QukcuzphnCd -->
如果你在配置或使用空间/空间自定义技能的过程中遇到任何问题，或有宝贵的优化建议，欢迎通过以下方式联系我们：
<!-- END_BLOCK_39 -->

<!-- BLOCK_40 | Wk98dKCENo06Yuxxe5Jc2Htonlb -->
<grid cols="2">
<column width="40">
</column>
<column width="60">
  - **联系我们**：你也可以直接联系空间管理员或@(lanjunjian@bytedance.com)@(dingdegao@bytedance.com)@(wangyiyun.0423@bytedance.com)
</column>
</grid>
<!-- END_BLOCK_40 -->




</content>
