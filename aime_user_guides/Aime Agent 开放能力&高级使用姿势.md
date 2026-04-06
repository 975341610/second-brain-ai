<title>Aime Agent 开放能力&高级使用姿势</title>
<url>https://bytedance.larkoffice.com/wiki/Ri4zwejsqigZB6k6Krcca7BJnfd</url>
<content>
<!-- BLOCK_1 | A2psdVTxCoZaqpxcy6LcWnqAnCf -->
## 🤹‍♀️ Skills
<!-- END_BLOCK_1 -->
<!-- BLOCK_2 | GElMdKcPzoG4TzxsPOCcvD9FnBc -->
<callout icon="raising_hand" bgc="15" bc="7">
Skills 是什么？
简单来说，Skill 就是一个插件包：包含了执行特定任务需要的「指令（操作流程）」，「业务知识」，「脚本」和其他相关的资源文件的压缩包。Aime 在发现任务与 Skill 描述一致的时候，会主动读取 Skill 中相关的指令和脚本，根据其中的指示来完成任务。
https://platform.claude.com/docs/zh-CN/agents-and-tools/agent-skills/best-practices
</callout>

<!-- END_BLOCK_2 -->
<!-- BLOCK_3 | DmrTdVHo9of6jCx1LrZcjX7snxh -->
Aime 支持通过 Skills 注入自定义的知识和脚本，更稳定地执行业务操作。

<!-- END_BLOCK_3 -->
<!-- BLOCK_4 | DsLzdXrSvojVugxGAuVcOI8wnCd -->
在侧边栏「知识配置」-「添加知识」-「上传 skill.zip」即可完成导入，完整指南见：[Aime Skill 指南](https://bytedance.larkoffice.com/wiki/BSVVwNRRdi6TDSkTHJNcUDiznbe)

<!-- END_BLOCK_4 -->
<!-- BLOCK_5 | LIa8djcHooQfm5x3gVncP7oVnrd -->
Aime Skill 支持注册额外的 MCP 工具，参考 [Skill MCP](https://bytedance.larkoffice.com/wiki/Ri4zwejsqigZB6k6Krcca7BJnfd#share-WOwXdB3dVoSMzjxDlGBcQu7nnwb) 小节。

<!-- END_BLOCK_5 -->
<!-- BLOCK_6 | SZ9MdFjgDoSfpMxO4QWcetoMnod -->
你可以在[这里](https://github.com/anthropics/skills)找到一些来自 Claude 的用法示例。<font color="red">谨慎加载未经验证（特别是</font>**<font color="red">外部开发者</font>**<font color="red">）的 Skill，可能会窃取代码、Token 等敏感信息</font>

<!-- END_BLOCK_6 -->
<!-- BLOCK_7 | BSCGd9lpdonzD2x2qNUcVorTnLh -->
<grid cols="2">
<column width="49">
  ![图片](img_TxOGblFJKoHnvlxebMac9eSvnUc.png)
</column>
<column width="50">
  ![图片](img_UYwTbCAb6ovGqHxVVEdcYtX8nGc.png)
</column>
</grid>

<!-- END_BLOCK_7 -->
<!-- BLOCK_8 | OLpXdYHENo3BcqxLgbYcJyYjnWf -->
<callout icon="bulb" bgc="3" bc="3">
**Pro Tip**
你可以在 Skill 中编写脚本利用 [Agent API](https://bytedance.larkoffice.com/wiki/Ri4zwejsqigZB6k6Krcca7BJnfd#share-HTpkd39NZo03XYxpzMAcmdmenfw) 调用添加的自定义 MCP 工具，实现更复杂的自动化流程
</callout>

<!-- END_BLOCK_8 -->
<!-- BLOCK_9 | ELLfdGSdro6PucxkKuRcBtacnne -->


<!-- END_BLOCK_9 -->
<!-- BLOCK_10 | FXbndo77PoyDa7x6PDfctjJpnde -->
## 🤖 AGENTS.md
<!-- END_BLOCK_10 -->
<!-- BLOCK_11 | GKzxdTbQroOcOjxzBW7c9hXAnUh -->
<callout icon="raising_hand" bgc="15" bc="7">
[AGENTS.md](https://agents.md/) 是什么？
AGENTS.md 是面向 Agent 的 README.md，合理使用 AGENTS.md 可以减少 Aime 每个任务都需要花时间了解仓库技术栈、目录结构的开销，并使编写的代码更符合仓库约定
</callout>

<!-- END_BLOCK_11 -->
<!-- BLOCK_12 | OJWKdroDIo0VruxVasRcQISqnfe -->
Aime 支持项目级的 AGENTS.md，在项目任意目录中添加 AGENTS.md 即可启用。

<!-- END_BLOCK_12 -->
<!-- BLOCK_13 | P7vwdJ5Pjo77rfx10alcdG0wnPb -->
建议包含仓库整体结构和技术栈、代码规范、开发/编译/测试流程等信息

<!-- END_BLOCK_13 -->
<!-- BLOCK_14 | NE2od5Fmooxdrqx5wuKcBQdtn5e -->
使用指南：[Aime 项目记忆（AGENTS.md）使用指南](https://bytedance.larkoffice.com/docx/VetbdMSMpoXMRMxiQuDcie7inth)

<!-- END_BLOCK_14 -->
<!-- BLOCK_15 | OifBd25WFo0PpKxHQhfc0axhnNh -->
> 如果你有多个仓库需要复用相同的知识，可以使用项目空间，项目空间下的所有任务共享知识库中配置的文档
> 
> [Aime - 项目空间使用手册](https://bytedance.larkoffice.com/wiki/Z6a6waWnQidvWPkxjL8cpzHhnFh)
> 

<!-- END_BLOCK_15 -->
<!-- BLOCK_16 | E8Qqd1ViRoWPvHxxu72cp0mnn3e -->


<!-- END_BLOCK_16 -->
<!-- BLOCK_17 | ZpI8dbdLaonnixxzzNscnzB4nNg -->
## ⚒️ MCP
<!-- END_BLOCK_17 -->
<!-- BLOCK_18 | SodOdeq5WoneOtxOdpcceHv5ndb -->
<callout icon="bulb" bgc="15" bc="7">
自定义 Aime 可以使用的工具，与第三方平台集成，扩展 Aime 的能力边界。
</callout>

<!-- END_BLOCK_18 -->
<!-- BLOCK_19 | CnNZdfgXOo5r6BxQ0PIcAYCNn2b -->
Aime 支持多种方式添加自定义 MCP 工具：

<!-- END_BLOCK_19 -->
<!-- BLOCK_20 | E7lNdISIDoFKAzx3v8tckCkTnec -->
### 任务 MCP
<!-- END_BLOCK_20 -->
<!-- BLOCK_21 | UeMYdRZI0osfsyxKm8NcZD1FnFb -->
在发起任务时，在「拓展」-「工具配置」中可以配置本次任务使用的 MCP 工具。

<!-- END_BLOCK_21 -->
<!-- BLOCK_22 | ELmqdb3KyoaN2exJUfQcowrPnhw -->
<grid cols="2">
<column width="31">
  ![图片](img_QiIFbVRzOo610Kxw3lkcv30anFh.png)
</column>
<column width="68">
  ![图片](img_UBiGbgDmQoQV1sx8hddc2kuLn5e.png)
</column>
</grid>

<!-- END_BLOCK_22 -->
<!-- BLOCK_23 | CEUjd2FcGoSIadxYfSJcXarCnkd -->
Aime 官方提供了一些内置的 MCP 服务，你也可以添加自定义 MCP 服务（仅支持远端 MCP 如 StreamableHTTP, SSE 和字节云 MCP SDK 接入）

<!-- END_BLOCK_23 -->
<!-- BLOCK_24 | O0tQd9JtqoIWwpxybPGcPaV5n3g -->
在字节云 MCP 市场可以找到内部其他开发者提供的 MCP（[CN](https://cloud.bytedance.net/mcp?x-resource-account=public&x-bc-region-id=bytedance) | [ROW](https://cloud.tiktok-row.net/mcp?x-resource-account=public&x-bc-region-id=bytedance)）

<!-- END_BLOCK_24 -->
<!-- BLOCK_25 | EhhYdUHsFoi68Ax3nCscQ3EInQe -->
> 字节云 MCP 市场上不是所有的 MCP 工具都支持 i18n 区域，如有需要可以联系开发者
> 

<!-- END_BLOCK_25 -->
<!-- BLOCK_26 | CMWFd6RGGog5gbxzADYc6HaTnqg -->
### Skill MCP
<!-- END_BLOCK_26 -->
<!-- BLOCK_27 | RhNldDDljocC9ExeErGcms98nmp -->
> 注意 ⚠️：功能尚未稳定，使用方式可能发生变化
> 

<!-- END_BLOCK_27 -->
<!-- BLOCK_28 | Ow7sdTS10oHfQdxLNUnc56uknfd -->
[Skill MCP 配置指南](https://bytedance.larkoffice.com/docx/BGYGdg7HMoLzVPxOE0XcxPYYnle)

<!-- END_BLOCK_28 -->
<!-- BLOCK_29 | XUOBdmLctoctGRxDgvMcGZcenbd -->
Skill MCP 支持通过 stdio 调用 MCP 工具，本地运行的 MCP 服务可以访问 aime 容器内的文件，实现 LSP MCP 等更高级的功能。

<!-- END_BLOCK_29 -->
<!-- BLOCK_30 | GMbDdGYCIoX7Taxuz3ocMe4qnne -->
### 内置 MCP 使用指南
<!-- END_BLOCK_30 -->
<!-- BLOCK_31 | LaHcd3MSzo0vBCx3u1jcpaCJncg -->
- Figma MCP：[Figma MCP 使用指南](https://bytedance.larkoffice.com/wiki/SMXlww9MyiAKvCk469ycRhP2nZd)

<!-- END_BLOCK_31 -->
<!-- BLOCK_32 | V6u8dm9zDobVhFxgEIUcWtNTnYb -->
- Deepwiki MCP：[DeepWiki MCP 使用指南](https://bytedance.larkoffice.com/wiki/EetgwYfWzi2FbZkTDTzc8wkwnMH)

<!-- END_BLOCK_32 -->
<!-- BLOCK_33 | RR4tdub3oozWV4xgUvscs1U3n4d -->
- Codebase MCP ：[Codebase MCP 使用指南](https://bytedance.larkoffice.com/wiki/LBeSwiSVviQmnQkFIcFcipMcniD)

<!-- END_BLOCK_33 -->
<!-- BLOCK_34 | UtwadtdidoX2HNx9fkhcnfBYn8f -->
### 开发自定义 MCP
<!-- END_BLOCK_34 -->
<!-- BLOCK_35 | QzdBd563KoRheJxaOOpcuUPAnWe -->
推荐通过字节云方式接入 MCP 服务[【Aime】字节云自定义MCP接入说明](https://bytedance.larkoffice.com/wiki/MXrBwKE2FiL0c8k9xe8cQgQfnue)

<!-- END_BLOCK_35 -->
<!-- BLOCK_36 | KuVMd4m2qojVsFxf3xjceCMFnTe -->
接入后，可以通过 [Aime 调试平台](https://aime.bytedance.net/debug) 获取 MCP 工具的输入、输出以及请求的 logid 来排查问题，使用手册：[Aime - 自定义MCP调试使用手册](https://bytedance.larkoffice.com/wiki/F0znwODSZiA4iJkLbmLcneovnue)

<!-- END_BLOCK_36 -->
<!-- BLOCK_37 | AcHAdCFuionjhbxCHJ3cR5I8n4g -->


<!-- END_BLOCK_37 -->
<!-- BLOCK_38 | De8EdVrcDomV65xAX9Jc4BsDnEb -->
## 🎨 Aime Open API
<!-- END_BLOCK_38 -->
<!-- BLOCK_39 | NXqldtvJtoHggIxt7DAc00eun9d -->
<callout icon="bulb" bgc="15" bc="7">
目前仍在实验中，需要申请～
</callout>

<!-- END_BLOCK_39 -->
<!-- BLOCK_40 | DiltdyXKOo7JBuxnQJaceaC1nSf -->
Aime 平台提供的接口，可以触发 Aime 任务、获取任务执行状态以及最终产物等

<!-- END_BLOCK_40 -->
<!-- BLOCK_41 | FsYXdImcIoeMYRxokvzcahH9n2f -->
- 以给定参数执行模板任务

<!-- END_BLOCK_41 -->
<!-- BLOCK_42 | Q9iRd8BscoGtcPxcCa3cLNJGnwd -->
- 通过 webhook 获取任务执行状态更新和产物

<!-- END_BLOCK_42 -->
<!-- BLOCK_43 | IFskdaAXior2gKxt346cnp6InGh -->
- 下载 Aime 任务的产物内容

<!-- END_BLOCK_43 -->
<!-- BLOCK_44 | AnF8d0JzeoFhZnxyREdc3pjxnDf -->
参考：[Aime OpenAPI 用户手册](https://bytedance.larkoffice.com/wiki/CmWowLiEdiwOOrkdMRocvnHknSf)

<!-- END_BLOCK_44 -->
<!-- BLOCK_45 | DEbtdzOh3oNxGVxJPdBc5amznNb -->


<!-- END_BLOCK_45 -->
<!-- BLOCK_46 | TVDJdzGOWorhIpxzz8CcE46bnfc -->
## 🔌 Aime Agent API
<!-- END_BLOCK_46 -->
<!-- BLOCK_47 | CrJSdp7AYoCA4HxtrVmcoTRynHg -->
<callout icon="bulb" bgc="15" bc="7">
<font color="yellow">不是 </font>[<font color="yellow">OpenAPI</font>](https://bytedance.larkoffice.com/wiki/CmWowLiEdiwOOrkdMRocvnHknSf)<font color="yellow">，不能用来触发 Aime 任务，仅限 Aime 执行环境内访问</font>
</callout>

<!-- END_BLOCK_47 -->
<!-- BLOCK_48 | AB3edTAwNo25dExhTaXcOeCkn4g -->
可在 Aime 执行的 bash 命令中通过 Agent API 调用由 Agent 提供的能力，实现自动化执行 Agent 内工具等操作。

<!-- END_BLOCK_48 -->
<!-- BLOCK_49 | T0pPdJJ3KoC92FxmxmXcTo7Unrh -->
- 列出 MCP Server 上的工具列表 / 执行 MCP 工具

<!-- END_BLOCK_49 -->
<!-- BLOCK_50 | ZBiRdUKxooX24dxhS03ck8exnif -->
- 更新 Aime 执行 bash 命令使用的环境变量

<!-- END_BLOCK_50 -->
<!-- BLOCK_51 | JuWNdg6Bzo7feVxusBrco4gXn2p -->
参考：[Aime Agent API](https://bytedance.larkoffice.com/wiki/SnSRwt31einNpykFw73c5pVmnEe)

<!-- END_BLOCK_51 -->
<!-- BLOCK_52 | Sv9TdLS6fouKFYxGsp7cczLenVd -->


<!-- END_BLOCK_52 -->
<!-- BLOCK_53 | QvCZdxN1Tor3gwxdXJ5cj88KnSf -->
## 🐳 自定义开发环境
<!-- END_BLOCK_53 -->
<!-- BLOCK_54 | UA65dHSr3oxIGQxLjincK4RYn9e -->
> [Aime - 开发环境配置](https://bytedance.larkoffice.com/docx/RYG6dAVDEoEQFfxgVemcTjGPnFg)
> 

<!-- END_BLOCK_54 -->
<!-- BLOCK_55 | C0hydrrQFopowcxcxJVctBzZnZb -->
Aime 的默认环境可能与你的仓库要求不符，导致 Aime 无法正常编译

<!-- END_BLOCK_55 -->
<!-- BLOCK_56 | Lsc8dfhWPontsFxWL8ZcygNjnie -->
你可以在侧边栏「环境设置」中添加自定义环境，创建任务时通过 @ 指定了对应仓库的情况下，会出现「环境」标识

<!-- END_BLOCK_56 -->
<!-- BLOCK_57 | LNDTd5cjHoX7BoxT4njc5g90nFd -->
![图片](img_BlCDbRRGhoDYFUx1Wn4cluvyn4c.png)

<!-- END_BLOCK_57 -->
<!-- BLOCK_58 | GLHPd0E2poc95ixj3IHcyaqEncb -->


<!-- END_BLOCK_58 -->
<!-- BLOCK_59 | B8SndgSy4oSwh7xK1PIcTMelnte -->
## 🗺️ 环境变量
<!-- END_BLOCK_59 -->
<!-- BLOCK_60 | G1Eyd6a98oSR3UxXWtzcslYwnEc -->
Aime 执行 bash 命令时会注入一些环境变量，可以用于鉴权、判断是否在 Aime 环境等。

<!-- END_BLOCK_60 -->
<!-- BLOCK_61 | KOYqdDPZIoXQVvx5j92cmn7Anth -->
<!-- 同步块开始（源文档: PsS5dXPzHoSKQpxKwgmcLhrbnuh，源块: RowQdHPsgsThCDbnxROcg295nyh）-->
<table col-widths="246,576">
    <tr>
        <td>**环境变量**</td>
        <td>**内容**</td>
    </tr>
    <tr>
        <td>`AIME_SESSION_ID`</td>
        <td>Aime 任务的 Session ID，即任务 url 中
`https://aime.bytedance.net/chat/``<font color="green" background_color="light_green">{id}</font>` 的部分</td>
    </tr>
    <tr>
        <td>`AIME_TEMPLATE_ID`</td>
        <td>Aime 任务的模板 ID，如果该任务由模板创建</td>
    </tr>
    <tr>
        <td>`AIME_SPACE_ID`</td>
        <td>Aime 任务的项目空间 ID，如果该任务在项目空间中创建</td>
    </tr>
    <tr>
        <td>`AIME_WORKSPACE_PATH`</td>
        <td>当前 Aime 任务的工作区根目录</td>
    </tr>
    <tr>
        <td>`AIME_AGENT_BASE_URL`</td>
        <td>Aime Agent API Base URL，详见 [[WIP] Aime Agent 开放能力&高级使用姿势](https://bytedance.larkoffice.com/wiki/Ri4zwejsqigZB6k6Krcca7BJnfd#share-UGeXdrPQYo7IHYx2ddfcRkDJn8f)</td>
    </tr>
    <tr>
        <td>`AIME_CURRENT_USER`</td>
        <td>当前 Aime 任务的发起人邮箱前缀</td>
    </tr>
    <tr>
        <td>`AIME_CURRENT_USER_EMAIL`</td>
        <td>当前 Aime 任务的发起人邮箱，邮箱后缀不一定是 @bytedance.com</td>
    </tr>
    <tr>
        <td>`<font color="orange">AIME_USER_CLOUD_JWT</font>`</td>
        <td>当前用户的字节云 JWT，可用于 TCE/SCM 等平台接口的认证
注意：
- 字节云 JWT 的有效期为 1 小时
- 字节云 JWT 的区域取决于触发 Aime 任务的区域
	- aime.bytedance.net: CN
	- aime.tiktok-row.net: TT-ROW</td>
    </tr>
    <tr>
        <td>`<font color="orange">AIME_USER_CODE_JWT</font>`</td>
        <td>当前用户的 Code User JWT，可用于调用 Codebase API [NextCode OpenAPI 接入指南](https://bytedance.larkoffice.com/wiki/PKoiwOfVniSnO6kEomWcett0nIc)</td>
    </tr>
    <tr>
        <td colspan="2">> 以下环境变量用于声明 terminal 的非交互性，防止启动的命令等待交互直到超时
> </td>
    </tr>
    <tr>
        <td>`DEBIAN_FRONTEND`</td>
        <td>`noninteractive`</td>
    </tr>
    <tr>
        <td>`TERM`</td>
        <td>`xterm`</td>
    </tr>
    <tr>
        <td>`CI`</td>
        <td>`true`</td>
    </tr>
    <tr>
        <td>`PAGER`</td>
        <td>`cat`</td>
    </tr>
    <tr>
        <td>`EDITOR`</td>
        <td>`/bin/true`</td>
    </tr>
    <tr>
        <td>`NO_COLOR`</td>
        <td>`1`</td>
    </tr>
    <tr>
        <td colspan="2">> 其他默认注入的环境变量
> </td>
    </tr>
    <tr>
        <td>`HTTP_PROXY`</td>
        <td>[仅 CN] 用于访问外网；需要访问 Aime Agent API 时需要在脚本中禁用掉</td>
    </tr>
    <tr>
        <td>`HTTPS_PROXY`</td>
        <td>[仅 CN] 用于访问外网；需要访问 Aime Agent API 时需要在脚本中禁用掉</td>
    </tr>
    <tr>
        <td>`BUILD_VERSION`</td>
        <td>`aime` 模拟 SCM 环境，防止部分内部 cli 工具触发扫码登陆</td>
    </tr>
    <tr>
        <td>`BUILD_TYPE`</td>
        <td>`aime` 模拟 SCM 环境，防止部分内部 cli 工具触发扫码登陆</td>
    </tr>
    <tr>
        <td>`BUILD_TOKEN`</td>
        <td>同 `AIME_USER_CLOUD_JWT`</td>
    </tr>
</table>
> 注：在 Remote SSH 或 Web IDE 中的 Terminal 不会注入
> 
> **Aime 在执行命令时会判断是否需要注入密钥类环境变量（标黄的环境变量），防止执行外部脚本/Skill 时误注入导致 token 泄漏**
> 
<!-- 同步块结束 -->

<!-- END_BLOCK_61 -->
<!-- BLOCK_62 | ZF3sdhkQDoNeAGxn9pbcX6CGnmf -->


<!-- END_BLOCK_62 -->
<!-- BLOCK_63 | KNSdddX9goilDgxyLm8cCdcDnJc -->
## 🚀 高级使用姿势
<!-- END_BLOCK_63 -->
<!-- BLOCK_64 | W5KqdPvfEoyq8oxboEwcb1fAn4d -->
### 调试 Aime 任务
<!-- END_BLOCK_64 -->
<!-- BLOCK_65 | E7lodGsmroBoToxsSNccBBM2ned -->
可以通过 [Aime 调试平台](https://aime.bytedance.net/debug) 来排查问题，使用手册：[Aime - 自定义MCP调试使用手册](https://bytedance.larkoffice.com/wiki/F0znwODSZiA4iJkLbmLcneovnue)

<!-- END_BLOCK_65 -->
<!-- BLOCK_66 | DQ7fdDUApodDuOxsf6ec8aeNnCb -->
目前仅支持查看创建的 sub agent 任务描述，MCP 工具的输入、输出以及请求的 logid，更多需求可以到下方 Feature Request 添加评论。

<!-- END_BLOCK_66 -->
<!-- BLOCK_67 | LghYdvHARo0VTkx4bsucVbshn5e -->
### 在 Aime 环境中使用自定义密钥
<!-- END_BLOCK_67 -->
<!-- BLOCK_68 | RncGdrQYRohlRExuQn1cAlegnJh -->
除了字节云/Code JWT 外，有时你可能需要让 Aime 通过其他密钥调用第三方服务。你可以添加自定义 Skill，在其中调用 Agent API 提供的**更新环境变量**接口并作为脚本提供给 Aime，这样 Aime 执行 Skill 中的脚本后再执行后续命令就会带上注入的 Token。

<!-- END_BLOCK_68 -->
<!-- BLOCK_69 | X5aHdxEQtortEmxHyRJczYqTnlh -->
如果你的密钥是动态获取的，例如不同用户有不同密钥内容，可以在 [FaaS](https://cloud.bytedance.net/faas?x-resource-account=public&x-bc-region-id=bytedance) 上封装一个接口，利用 Aime 注入的字节云 JWT 完成鉴权。

<!-- END_BLOCK_69 -->
<!-- BLOCK_70 | YuSVda21SoAIJJxL19ScUZSXnpf -->
### 调用其他平台 API / 回传产物和结果到自定义 API
<!-- END_BLOCK_70 -->
<!-- BLOCK_71 | Y6YAdmN7Xo6XM6xz35lczvSPnlb -->
想让 Aime 在任务完成后把特定格式的结果传回自己的系统方便后续处理？

<!-- END_BLOCK_71 -->
<!-- BLOCK_72 | TJSvdUJClo4uvWxwFhtcQEQ3nPg -->
- 你需要的产物数据

<!-- END_BLOCK_72 -->
<!-- BLOCK_73 | Hoihd1q8soH4iixyTdlcBqkanpd -->
- 生成的文件

<!-- END_BLOCK_73 -->
<!-- BLOCK_74 | ZifrdH99nob72nxhuM4cFPjrnCb -->
- 统计/埋点信息

<!-- END_BLOCK_74 -->
<!-- BLOCK_75 | QSgzdTsDMohKJwxKUq0cAo70nQc -->
把接口封装到 Skill 脚本中，并要求 Aime 在任务结束时调用 Skill 上传即可（后续会支持 Hooks）

<!-- END_BLOCK_75 -->
<!-- BLOCK_76 | ZXA0dYpaco4IUYxkGlzc98oHn9e -->
注意访问自定义 API 时需要遵循 Aime 任务区域和服务区域相同的规则（CN - CN/ I18N - I18N），不然可能会由于网络隔离无法正常调用。

<!-- END_BLOCK_76 -->
<!-- BLOCK_77 | YzindYCgUoIMYzx9ievcU1dHnPe -->
### 调用 MCP Tool 的时候携带自定义环境变量
<!-- END_BLOCK_77 -->
<!-- BLOCK_78 | WZytdMdPLozDjBxe4tbcTRz4nuf -->
MCP 协议工具的所有参数均需要模型在工具参数中传递

<!-- END_BLOCK_78 -->
<!-- BLOCK_79 | AWTRdztKwooGDDxaTDEcooGpn9g -->
- 如果参数由 Aime 输入，可以让 Aime 从环境变量中获取到值后再调用

<!-- END_BLOCK_79 -->
<!-- BLOCK_80 | BHkvdEYMooWqzxx32Itc17rCnDe -->
- 如果直接调用 Agent API，可以考虑封装到 Skill 供 Aime 直接使用

<!-- END_BLOCK_80 -->
<!-- BLOCK_81 | XG1WdY7z8oZOJhxTHH8cp4psnCg -->
### 统计模板执行情况、用量、耗时等信息
<!-- END_BLOCK_81 -->
<!-- BLOCK_82 | YwPEdTvX7o3vaMxq3PhcsQn3nif -->
目前暂未开放统计信息，可以在下方评论具体想要的数据

<!-- END_BLOCK_82 -->
<!-- BLOCK_83 | UrkNd0lyuoNMZpxlX9xcdGWTnNe -->
### 任务中包含批量处理大量类似内容，如何稳定效果
<!-- END_BLOCK_83 -->
<!-- BLOCK_84 | HKA0dYOIrosu86xIzuhcRvBynWh -->
建议在提示词中提示「每 X 个使用一个 subagent」来分批处理子任务，每个子任务之间会隔离上下文。

<!-- END_BLOCK_84 -->
<!-- BLOCK_85 | TVnFdec6voDEJsxTFsKc5Vz3n0c -->
X 视任务需要的上下文长度决定，同一个 subagent 连续执行超过 25 个子任务效果可能会开始下降（出现幻觉、提前结束等）

<!-- END_BLOCK_85 -->
<!-- BLOCK_86 | UBY4dfZS5oFPltxhrJpcZyJLnrf -->
### 结束时发送自定义飞书卡片
<!-- END_BLOCK_86 -->
<!-- BLOCK_87 | ChMMdjtB5oKWGSxIyMDcgUQTnpc -->
侧边栏【知识配置】中可以启用官方预置的 `feishu-card` 知识，创建任务的时候提供飞书卡片模板 json 即可

<!-- END_BLOCK_87 -->
<!-- BLOCK_88 | SQhUdzFzro1NwGxvvEKcGbxfnBd -->
群组 id 可以通过 https://open.larkoffice.com/api-explorer 选择一个需要群组 id 的 API（如「更新群信息」）获取

<!-- END_BLOCK_88 -->
<!-- BLOCK_89 | G5pxdf6mPooSWNxura3ceA3fnsf -->


<!-- END_BLOCK_89 -->
<!-- BLOCK_90 | IqAEd18BWodRqgxbZ8Ncod5hnid -->
## 🚧 Feature Request
<!-- END_BLOCK_90 -->
<!-- BLOCK_91 | GngHdbEwzoMxw0xThDxcQWThnng -->
点击**标为已读**参与投票 ⬇️ 

<!-- END_BLOCK_91 -->
<!-- BLOCK_92 | UNrwdZBnnoueDUxXcVxc5w1pnLb -->
或者**添加评论**对某个功能补充新的需求

<!-- END_BLOCK_92 -->
<!-- BLOCK_93 | NUJLdrTU6o1sEFxGSTQcnu58nZS -->
**Hooks**

<!-- END_BLOCK_93 -->
<!-- BLOCK_94 | VZqzd9MpQoav4zxhTTccG2lUnJM -->
任务执行开始/结束/其他时机，额外执行特定命令/脚本

<!-- END_BLOCK_94 -->
<!-- BLOCK_95 | V5d4do8xvoxKDixQGBocQlI2nvx -->
> 🚧 开发中！
> 

<!-- END_BLOCK_95 -->
<!-- BLOCK_96 | CJpQd9QFoo5HXRxMcg1cMeg4ntb -->

<!-- END_BLOCK_96 -->
<!-- BLOCK_97 | HMXUdqC15oc9lSxZIA7c0YZSn0c -->
**密钥管理**

<!-- END_BLOCK_97 -->
<!-- BLOCK_98 | SJDkdwy28oWlI4xWXL2cub4knee -->
在 Aime 平台上管理调用外部平台的 token，运行命令时按需注入

<!-- END_BLOCK_98 -->
<!-- BLOCK_99 | JdGHdI5pFoOJDlx76vMc2J3GnWb -->

<!-- END_BLOCK_99 -->
<!-- BLOCK_100 | OuFqdeS8BoQlIKxYjhDc1x6wnIg -->
**LLMs.txt**

<!-- END_BLOCK_100 -->
<!-- BLOCK_101 | WVROdKvbjoQ35Fxvi4HcULSFnrh -->
网站提供 `/llms.txt`，当用户请求中带有对应域名时将主动加载，引导 Aime 使用特定方式操作平台

<!-- END_BLOCK_101 -->
<!-- BLOCK_102 | DInsdsYAZor9AlxlJ0HcqyFmnuh -->

<!-- END_BLOCK_102 -->
<!-- BLOCK_103 | Uiw8dMgLFomXv4x7sPncvYZInRg -->
**统计信息**

<!-- END_BLOCK_103 -->
<!-- BLOCK_104 | EWvCdQvymoqlzhxjV7rcsXG9nvd -->
统计自定义工具调用成功率、耗时、Skill 脚本执行情况等信息

<!-- END_BLOCK_104 -->
<!-- BLOCK_105 | FTgddIiJNomKJ1xPltbcv9CenOe -->

<!-- END_BLOCK_105 -->
<!-- BLOCK_106 | NjCqdDeVgocZpnxxE1ucEnyGnAg -->
**任务调试**

<!-- END_BLOCK_106 -->
<!-- BLOCK_107 | P10jdPBOtoWIQmxZIIkc1DjEnTb -->
在调试平台开放更多中间过程的信息：模型思考过程，中间工具调用参数和结果，诊断工具等

<!-- END_BLOCK_107 -->
<!-- BLOCK_108 | NAbMdiDYgoX57JxgIgHcDMeUnCe -->

<!-- END_BLOCK_108 -->
<!-- BLOCK_109 | AmhxdImIho7IMJxwp3UcxLUOnlh -->
**自定义执行环境**

<!-- END_BLOCK_109 -->
<!-- BLOCK_110 | UsfsdWb26oNutxxT8VPckk0OnCf -->
自定义 Dockerfile，启动命令等，无需每次都重新安装依赖

<!-- END_BLOCK_110 -->
<!-- BLOCK_111 | Z7dddSYuOoIT2rxc4Ssc1H38ntf -->
自定义机器配置 CPU/内存/磁盘大小，开发大项目

<!-- END_BLOCK_111 -->
<!-- BLOCK_112 | Aimed1v9qooMrwxCUVTcB6YTnzn -->

<!-- END_BLOCK_112 -->
<!-- BLOCK_113 | Uig5dDiqeonhQMx29ylcPe8hn1d -->
**自定义 SubAgent**

<!-- END_BLOCK_113 -->
<!-- BLOCK_114 | A7wsdEX1roO21qxkhWBcMp9Tnee -->
创建固定 prompt、skill 等属性的 SubAgent

<!-- END_BLOCK_114 -->
<!-- BLOCK_115 | Z3SEdzf3To5pEdxhvzScqsnYnch -->

<!-- END_BLOCK_115 -->
<!-- BLOCK_116 | BMzvd8Hieo6NLuxeIh0cWd6HnCc -->
**自定义飞书卡片**

<!-- END_BLOCK_116 -->
<!-- BLOCK_117 | INtcdPdgbooVJnx37qucHOOGnoc -->
自定义任务需要接管、确认或结束后发送的飞书卡片模板，指定群聊

<!-- END_BLOCK_117 -->
<!-- BLOCK_118 | BTsDdmZBfoWD8Ix0wzjc9TB5nvb -->

<!-- END_BLOCK_118 -->
<!-- BLOCK_119 | UX5wdzbu7opRP7xqokVcM71mneg -->
**更多 Agent API**

<!-- END_BLOCK_119 -->
<!-- BLOCK_120 | MdzHdQzszoy4NzxWOjic0vqznKb -->
管理产物、调用 LLM、转移飞书文档权限...

<!-- END_BLOCK_120 -->
<!-- BLOCK_121 | LyLWdv7fuolqI6xuPkMcafUznsK -->

<!-- END_BLOCK_121 -->
<!-- BLOCK_122 | UQ8tdV8CYoSqg4xELGZcQttznGb -->
**其他**

<!-- END_BLOCK_122 -->
<!-- BLOCK_123 | Z0f5dLHb2oe98Fx4dJPcjr28nBh -->
在评论区留言许愿 🔮

<!-- END_BLOCK_123 -->
<!-- BLOCK_124 | RzyvdZWAGobEqSx3CbccHEhanah -->


<!-- END_BLOCK_124 -->

</content>
