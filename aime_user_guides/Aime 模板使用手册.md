<title>Aime 模板使用手册</title>
<url>https://bytedance.larkoffice.com/wiki/E0qhw517PiDPmhkgC99cAVwlnwb</url>
<content>
<!-- BLOCK_1 | doxcnDyuiA6wGZ6H8ZM9yekAkfd -->
最近更新：2026-01-12
<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | YcWtdaOBIovN9CxRSPCcVxO9nmf -->
<table header-row="true" col-widths="177,643">
    <tr>
        <td>更新时间</td>
        <td>更新说明</td>
    </tr>
    <tr>
        <td>2025.10.14</td>
        <td>- 新建文档，对模板创建、调试与 “操作指南” 进行说明，完善 FAQ 章节</td>
    </tr>
    <tr>
        <td>2025.11.13</td>
        <td>- 支持跨空间导入已有模板，新增跨空间导入模板的操作说明
- 基于模板发起的任务支持在任务详情页中添加 “操作指南”</td>
    </tr>
    <tr>
        <td>2026.01.12</td>
        <td>- 新增 “批量创建模板任务” 使用说明</td>
    </tr>
</table>
<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | doxcn2FHwDEmZdSfwuf1URAkFEf -->
# 关于模板<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | AqkwdLO3CoSoswxVYZXcY80Anmf -->
<callout icon="bulb" bgc="2" bc="2">
你可以将一次运行效果良好的任务抽象为模板：在后续使用时只需填写少量参数即可复用成果。模板既支持个人使用，也支持在项目空间内或跨空间分享，促进协作与知识沉淀。
</callout>
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | TWAJd54oLoHUpkxlxMHc16A1nih -->
1. **什么是模板？**
	1. Aime 模板帮助你把高频、重复的工作沉淀为可复用的模板，结合参数化填充与操作指南，让后续任务可以快速、稳定地复现预期效果，显著降低每次创建任务的成本。
	2. 典型场景包括周报/月报、数据分析、问题排查与复盘、内容制作、资料整合等。
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | U7tgdGJeRoN6epxTzMccfsZ3nNC -->
2. **模板有什么作用？**
	1. 将高频且重复的任务配置为模板，告别重复输入；同时，支持动态参数配置，可满足相似任务的个性化需求。实现一次配置多次使用
	2. 配置为模板后可调试优化模板与关联的模板经验，以提升任务运行的稳定性与可控性
	3. 支持跨空间的模板的分享使用，降低任务与任务经验的分享与使用成本，促进团队协作与知识沉淀
<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | IhuFdVHEzoa2j9xOZCTcs9denXe -->
## 关键信息与注意事项<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | NYKTdGQ2poC6fKx6koJcmbS4nJc -->
- **模板创建**：
	- 基于已完成的任务一键自动化创建
	- 在首页点击新建模板卡片，0-1 创建模板
<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | LqFodQbjFo3iQuxSChAcpz7In0c -->
- **参数化填充**：
	- 支持填写参数的填写说明、默认参数、是否必填、上传文件等配置项
	- 可通过 “智能提取参数”  ai 识别指令中的参数并生成表单
	- 指令中 { } 之间的内容将被自动识别并添加为参数，降低批量填写指令的参数配置成本
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | HfQDdxlelokwkGxYTzpcjOqqnFe -->
- **操作指南**：
	- 对于 **步骤固定、发散性低、稳定性需求高&nbsp;**的任务，可从历史运行的关联模板任务中总结可复用的步骤与要点，用于提升模板的稳定性与可释性。即历史版本中的 “执行规划” 字段
	- 模板更新核心字段（如：需求指令、参数核心信息）后，操作指南相应失效，需要重新添加或编辑；同理，亦不能基于历史版本的模板任务添加操作指南。需要基于新版模板至少发起一次任务并得到结果后，再添加或更新操作指南。
	- 当任务流程高度不稳定或期望模型发挥创造性时，过度依赖操作指南可能降低输出质量。此类模板建议仅保留清晰的需求指令与参数表单，谨慎启用操作指南。
<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | EI5gdV3tFodbgoxspMPcoSxknng -->
- **权限与可见性**：
	- 模板的可见范围可设置为 **个人**、**项目内公开**、**全局公开**。
	- 项目空间内公开的模板分享后仅空间内成员可访问；设置为公开或分享过的个人权限的模板可能会被他人使用，请确保内容适合分享
	- 如果涉及代码、密钥、文档等敏感信息，请谨慎创建或公开模板，并在参数说明中明确数据使用规范
	- 模板支持配置 MCP 与 agent 扩展，请保证连接可用，并尽量避免配置私人信息
<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | M9bsdsXMMoeO5vxqBC9c5vS0nyp -->
# 快速上手<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | YSpVdhpDRojIVgxmfyycRffunsz -->
> 创建、编辑并调试模板，解锁玩转模板小技巧
> 
<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | BuAsdEFGHoYjRXxP0ticuoLCnjg -->
<callout icon="star" bgc="5" bc="5">
最佳实践：首次使用新模板时，先在小范围任务里试跑并核对结果，再推广到团队使用；遇到效果波动，优先检查参数填写是否完整与指令是否过度变更。
</callout>
<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | GKEMdn6k8odf7Bx3zqWcnZoRnFg -->
## 配置与操作步骤<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | YTRNdiYSJobB6uxu8TccmU69nef -->
### 步骤一：选择创建方式<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | OTz9dz33IoeYnsxDrCvc6WCfnUg -->
<grid cols="2">
<column width="50">
  **<路径一>  基于任务创建模板**
  适合已完成一次高质量任务并希望快速沉淀为模板的场景。系统会自动总结模板名称、参数等字段供参考。
  **适用场景：**任务效果已验证，希望快速创建、直接复用。
  **添加路径：**在任务对话框上方，单击 **创建模板**。在模板弹窗中检查并修改全量参数、关联拓展与基础信息。
  ![图片](img_RNZCbINqhoIYgYxMBYtcJErznFm.png)
</column>
<column width="50">
  **<路径二>  直接新建模板**
  在首页点击 **新建模板&nbsp;**卡片，手动填写需求指令与参数表单，可保留完整的指令，更灵活、可控地搭建模板。
  **适用场景：**已明确需求与参数设计，不依赖于已完成的任务，灵活可控。
  **添加路径**：在首页点击 **创建模板&nbsp;**卡片。在模板弹窗中输入清晰、具体的需求指令、参数与基本信息。
  ![图片](img_UNx4by0maoaYrKxADSfcqvljnJ9.png)
</column>
</grid>
<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | Ack9dOGKzoypYexMAg3cjvSNn0d -->
### 步骤二：模板填写与编辑<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | doxcnYuQ9nJe67ORwB78bX093Pd -->
模板表单包含 **需求指令与参数** 及 **基本信息** 两部分
<!-- END_BLOCK_19 -->

<!-- BLOCK_20 | CFgmdXZqnoX54zxHQJ0cOzRenXe -->
![图片](img_DLDCbTlVBofzvExY14OcQr25n2d.png)
<!-- END_BLOCK_20 -->

<!-- BLOCK_21 | HC39dQ9j1owO0gxvSkAcm0IrnGd -->
<grid cols="2">
<column width="49">
  ![图片](img_DnbwbsVFJoFkeKxq7jecxs1incM.png)
</column>
<column width="50">
  ![图片](img_XR7TbTUJVoiw1fxHQRgcBAwDnse.png)
</column>
</grid>
<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | Op2KdqzoooEORSxeEiscFTTEnug -->
1. 需求指令与参数
	1. 输入完整清晰的需求指令（即 user query）后可手动划词或 AI 智能提取参数
	2. 输入指令后，点击 “智能提取参数”，AI 将根据指令中的语义信息自动识别参数，降低操作成本；其中，指令中 { } 内的内容将自动被识别为参数
	3. 所有操作均可通过 “ctrl+z” 或 “command+z” 撤销回退
<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | PSRQdX3xpozVDhxQA66c7Ambn7d -->
<grid cols="2">
<column width="49">
  ![图片](img_E1RmbEZFBo6hjHxLtkvcKCnPnzf.png)
</column>
<column width="50">
  ![图片](img_G5yvbAIxPoEibPxLfsocWobQnqd.png)
</column>
</grid>
<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | C90qdjidWo7eA8xNu8XcmVQsnkd -->
1. 参数支持配置多种字段，包含：
	1. 是否配置为必填参数（全量参数默认配置为非必填，请自行配置）
	2. 添加默认值：使用者可在不修改参数值的情况下使用您配置的默认值
	3. 上传文件：开启后，参数内容可支持上传文件
<!-- END_BLOCK_24 -->

<!-- BLOCK_25 | MwQ3dMUpfoUczPxfV0hcvgkynxf -->
![图片](img_GVEkbZKcsorFGrxwuC9cBQ4Xnfg.png)
<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | IrSIdWLQyoTL65xi4g1c8guvnqh -->
1. 点击“下一步”，进入“基本信息”编辑页
	1. AI 已根据需求指令自动识别起草名称、职能、类型与模板简介，请根据实际情况编辑
	2. 模板可见权限将默认设置为 “仅个人可见”，在调试优化效果后，可将模板配置为公开（注意保护个人信息与隐私数据）
<!-- END_BLOCK_26 -->

<!-- BLOCK_27 | Q0mTdlaQooFtM3x5zHYcKiVknub -->
2. 编辑弹窗左下角的 “拓展” 可点击展开，展开后支持在抽屉内灵活增删模板所需的 agent 或 MCP
<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | Og8CdaPkYod0DaxYdjUc515rnnc -->
3. 完成全部信息编写后，点击 “保存”则模板创建完成
<!-- END_BLOCK_28 -->

<!-- BLOCK_29 | KCemdQ2rtoDhtwxuIlmc0DHcnsd -->
4. 后续使用过程中可打开点击该模板卡片，查看或进入编辑
<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | JfNAdV7wcoBPHGxL56Kcj8eWnEc -->
### 步骤三：使用模板发起任务<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | Ob6WdQMSJoFlaJxiE6scRdaPnWh -->
Aime 支持发起单个模板任务或在闲时批量发起模板任务
<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | MRh6dCcLooJrdrxmPtqccY6Ynsg -->
#### 发起单个模板任务<!-- END_BLOCK_32 -->

<!-- BLOCK_33 | HeK3d7wP6onieSxWbYvc0AKunff -->
1. 在模板列表或首页推荐中，选择合适的模板并打开使用弹窗。
<!-- END_BLOCK_33 -->

<!-- BLOCK_34 | Cu2ud7bLLoLaNRxxFRmc3w1jngg -->
2. 依次填写参数信息，或核对已预填的默认参数。
<!-- END_BLOCK_34 -->

<!-- BLOCK_35 | ZXdEdMOSYoddjKxeGtpc1HzlnLf -->
3. 单击发送，基于模板发起任务
<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | VLHvd00aRoG1Fhxy5jhcVQSGnGh -->
<grid cols="2">
<column width="46">
  ![图片](img_HDRAbvn14ommmbxJsLccxHSnnIh.png)
</column>
<column width="53">
  ![图片](img_TputbY3xkoDZH0x6zDjcS6hynNc.png)
</column>
</grid>
<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | PgrNdoFxsolOdwxgAzCcuvD9nod -->
1. 任务完成后可以通过飞书 bot 通知，或至平台历史记录中点击查看任务详情；基于模板发起的任务可在详情页输入框上方快速定位到发起任务的源模板
<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | SwBEde5rLoeDMYxX9Hycngg2nGd -->
#### 批量发起模板任务<!-- END_BLOCK_38 -->

<!-- BLOCK_39 | S0Yzd7K4zogVKfxkfHhc8qMKnTg -->
> 利用批量任务功能，在系统资源相对空闲的时段，基于同一模板和多组不同的参数一次性创建并执行大量任务。适用于需要重复运行但时效性要求不高的场景，如批量生成报告、数据处理、内容续写等。
> 
<!-- END_BLOCK_39 -->

<!-- BLOCK_40 | BGPYdIHCuoMMxrxLyEncAe7Hnaf -->
1. 批量任务会在系统“闲时”自动执行，以确保计算资源得到高效利用。不同地区“闲时”定义如下：
	- 中国大陆 (cn) 用户：工作日 `24:00` 至次日 `08:00`，以及所有法定节假日全天。
	- 国际 (i18n) 用户：每日 `24:00` 至次日 `08:00`。
<!-- END_BLOCK_40 -->

<!-- BLOCK_41 | WtXSdrtMdoaPUGxVyBFcr6HGnBe -->
2. 为保证平台的公平性和稳定性，批量任务设有以下配额和限制：
	<table header-row="true" col-widths="130,665">
    <tr>
        <td>**限制项**</td>
        <td>**说明**</td>
    </tr>
    <tr>
        <td>单次提交上限</td>
        <td>一次批量任务最多支持提交 **<font color="orange">500</font>**<font color="orange"> 条</font>任务。</td>
    </tr>
    <tr>
        <td>每日额度上限</td>
        <td>创建批量任务时，每批任务需要设置一个“每日占用的任务额度上限”，它代表 **这批任务<font color="orange">每天</font>最多消耗的任务总数**
- 该额度从<font color="orange">每日总任务配额（目前单日最多 50 则）</font>中扣除，在提交时进行校验。如果设置的额度超过了你当天剩余的可用任务数，系统将提示错误并阻止提交。
- 截断逻辑：如果在闲时执行期间，你的每日总任务配额耗尽，系统会自动暂停执行，并将剩余的子任务移至下一个闲时周期继续处理。</td>
    </tr>
</table>
	1. 使用步骤
		1. 在模板使用弹窗中，切换到“批量执行”标签页，获取批量任务飞书模板
		2. 获取并填写参数集飞书云文档
			- 单击“获取云文档链接”按钮，系统会根据模板的参数结构，自动生成一份名为“`/模板名称/ - 批量执行任务参数集模板`”的飞书表格。
			- 打开该飞书表格后，**创建副本**（点击表格右上角菜单 -> 创建副本），然后在副本中根据说明填写你需要执行的每一条任务的参数。
			- 注意：必填参数列不能为空，否则该行任务将被自动跳过。
		3. 设置上传参数集并设置每日限额
			- 上传参数集：将你在上一步中填写好参数的飞书表格副本链接，粘贴到参数集输入框中。
			- 设置每日额度上限：在“本批任务每日额度上限”输入框中，设定这批任务在一天内最多可消耗的任务数量。此额度会从你的每日总任务配额中扣除，请谨慎配置。
		4. 提交任务与校验
			- 单击“提交”按钮；系统会弹窗提示本次任务预计占用的额度信息与今日剩余可用任务额度。确认无误后，单击确认提交。
				- 在参数集云文档中，如果某一行的必填参数为空，该行对应的子任务将被系统**自动跳过**，不会执行。
			- 系统将校验你设置的“每日额度上限”是否超过了你当天剩余的可用任务总额度。如果超出，将报错并拦截提交，你需要调低额度后重试。
			- 提交成功后，任务将进入“等待运行”状态。
		5. 查看进度与结果
		![图片](img_FYjtbLWrJohgFdxSMWucJPfwngd.png)
			- 任务提交后，系统会为你的参数集云文档生成一个只读的“快照”版本。你可以随时点击参数集输入框旁的链接查看提交时的具体参数，无需担心原始文档被修改导致记录丢失。
			- 任务开始执行后，你可以在源模板的 “批量执行” 标签页查看实时进度，如 `x/y 条任务已执行完成`。
			- 你也可以到“历史任务”页面，使用“任务类型 - 批量任务”筛选器来定位和查看所有已完成或正在运行的子任务。<font color="red">（批量任务管理配置页正在规划中，敬请期待）</font>
<!-- END_BLOCK_41 -->

<!-- BLOCK_42 | BSr4dFKGbotSAmx0q97cIyI9nMc -->
![图片](img_XPAQb76Z0ovRW4xrKNecZoG3nhd.png)
<!-- END_BLOCK_42 -->

<!-- BLOCK_43 | DnvidzxxCoTTcVxOn3scpCfXnZd -->
1. 模板任务的结果详情页将会展示关联的模板标签，点击可查看或进入编辑；亦可点击下拉选择“新建模板”
<!-- END_BLOCK_43 -->

<!-- BLOCK_44 | S4oqdX0cVoKVCfxwu0RcqaKhnLh -->
#### 模板 link 发起<!-- END_BLOCK_44 -->

<!-- BLOCK_45 | B1Y7dbwhsomUdWxk1BjceCgRnNb -->
详情参考：
<!-- END_BLOCK_45 -->




<!-- BLOCK_46 | Yh5vdmfO2o1Qlgx80Etci3QlnBf -->
## 配置模板的 “操作指南”<!-- END_BLOCK_46 -->

<!-- BLOCK_47 | SCotdaDT8ortYpxcuu5cxdgwnSe -->
1. 什么是 “操作指南”
	1. “操作指南” 即原 “执行规划” 字段。**基于历史任务总结提炼得到**，预先规定了要执行哪些步骤，每一步的工具、目标、应该怎么做。
	2. 适用场景：**适合执行步骤清晰明确、相对固定且稳定性要求高的任务**，比如数据处理；效果最好，灵活度差
<!-- END_BLOCK_47 -->

<!-- BLOCK_48 | QGghdcIOWoct80xM0QJcgF7nnwb -->
2. 添加渠道
	1. 基于任务创建的模板，若创建时未进行任何对于核心参数信息的修改，则将自动基于原始任务生成 “操作指南”
![图片](img_Tvc7bnjn1ogevrxbWFxcj1oknWe.png)
	1. 在根据模板创建的模板任务结果详情页，也能通过点击输入框上方的关联模板标签来打开关联模板（**当且仅当任务是依据最新版本的模板创建时，才可以根据当前任务生成并添加/更新 “操作指南” 字段）**
<!-- END_BLOCK_48 -->

<!-- BLOCK_49 | PIaTdyvT0oDkdvxIza5ckPhKn8d -->
3. 注意事项
	1. 若你修改了 需求指令、参数核心信息或拓展工具（模板更新），现有操作指南会失效。可基于新版模板发起一次任务，得到满意的结果后，可在任务详情页添加/更新操作指南。
	2. 并**非在所有场景下配置添加 “操作指南” 都是更好的调试选择**。当使用时期望更充分地发挥模型自身的创造力或者场景本身灵活度较高（如：问题排查），可将 “操作指南” 字段置空，交由 Aime 自行探索
<!-- END_BLOCK_49 -->

<!-- BLOCK_50 | BLAidEhMsoMMAqxwymwcTSnVnpc -->
## 跨空间导入已有模板<!-- END_BLOCK_50 -->

<!-- BLOCK_51 | VMMNd3JB4o1PAxxv1FtcEAS2niW -->
模板跨空间导入功能实现了让模板在不同空间之间流转。你可以轻松地将任意空间中的优秀模板导入到当前空间使用。
<!-- END_BLOCK_51 -->

<!-- BLOCK_52 | IINhddrOOoQhE4xW0nhcEijKnIb -->
> - **普通用户**：只能导入自己创建的模板。
> 
> - **空间管理员**：除了自己创建的模板，还可以导入源空间内所有设置为“项目内公开”的模板。
> 
<!-- END_BLOCK_52 -->

<!-- BLOCK_53 | XnbhdJ8TGoeJqaxFifvcgkkNnKf -->
![图片](img_GqE9bv0VUon8fsxWhmccDTYLntg.png)
<!-- END_BLOCK_53 -->

<!-- BLOCK_54 | TEUId6zmbozerAxxLYNcKpoNnue -->
1. 点击首页 “创建模板” 卡片中的 “导入” 按钮，打开导入模板功能抽屉
<!-- END_BLOCK_54 -->

<!-- BLOCK_55 | K70kdKl7LoUe6OxIfmOcSQuSnBf -->
![图片](img_P5jkb7Y6aovpDgxxgDHcYcRwnih.png)
<!-- END_BLOCK_55 -->

<!-- BLOCK_56 | JdiadsVtIoD99Wx0zcNcnMnhn5g -->
1. 打开模板导入抽屉后
	- **选择来源空间**：在页面顶部的下拉菜单中，选择你希望从哪个空间导入模板。列表会展示全量你拥有权限的所有空间。
	- **筛选与搜索**：支持通过模板名称进行模糊搜索，或使用筛选器快速定位模板。（模板列表展示的字段信息支持自定义配置）
	- **批量选择与导入**：
		- 在列表中勾选你想要导入的模板。单次最多支持批量导入 **50** 个。
		- 已导入的模板也可以被再次勾选，实现模板的更新或覆盖。
	- **设置导入后的属性**：
		- **公开范围配置：**在页面底部，你可以统一设置这批导入模板在当前空间的 **公开范围**（例如，统一设为“项目内公开”），模版的可见范围将默认继承模板现有的可见范围
		- **“操作指南”配置**：为确保模板在新环境下的效果（不同空间的知识库、工具配置可能存在差异），迁移时将默认选择清除模板的“参考经验”，也可在导入时手动选择同步。迁移后，建议，基于新空间的环境重新运行任务，再生成新的、适配当前空间的操作指南。
<!-- END_BLOCK_56 -->

<!-- BLOCK_57 | V2CId3ldOocOZ9x4sqocKcu7nEh -->
2. 导入模板后
	1. 导入操作相当于在当前空间创建了一个模板的副本。该副本的“创建者”会记录为执行导入操作的用户，而原始创建者信息可在迁移日志中追溯。
	2. 新导入模板的所有历史数据（如点赞量、使用量、版本记录）都会被清空，一切从零开始。
	3. 模板的导入状态仅分为“已导入”和“未导入”。导入成功或失败会通过即时状态卡片提示。考虑到模板存在多次调试后导入同一个模板的诉求，已导入的模板支持重复导入，请合理标记进行区分。
<!-- END_BLOCK_57 -->

<!-- BLOCK_58 | doxcn6IXftUyzCz3y3zuHfwhk3d -->
# 常见问题<!-- END_BLOCK_58 -->

<!-- BLOCK_59 | MIped4QC5oJQsZxMM8aceyO1nRf -->
##### Q：模板运行的效果和准确性不稳定，我该如何提升模板效果和稳定性？<!-- END_BLOCK_59 -->

<!-- BLOCK_60 | TIoRdUAXtoR46KxQSw3cQiaOn0d -->
A：对于 执行步骤清晰明确、相对固定且稳定性要求高的任务，比如数据处理场景，建议调试模板后，基于模板发起任务，并选择生成结果最好的一次点击添加 “操作指南” 字段，让模型在后续执行该模板任务时有更清晰的执行路径。与此同时，我们也在规划支持用户自定义编辑 “操作指南”并计划上架任务诊断工具，届时模板任务生成结果将更可控。
<!-- END_BLOCK_60 -->

<!-- BLOCK_61 | doxcnvl0qiAcg4hw1deHCC2pejg -->
##### Q：模板可以配置多个同名参数吗？<!-- END_BLOCK_61 -->

<!-- BLOCK_62 | doxcnjlC0vPg6EcXqd2GK4OOkue -->
A：不可以。模板使用者在使用模板时只能通过参数名称来判断需要填写的信息，为了保障模板的可读性与易用性，不支持在一个模板中配置多个同名参数。
<!-- END_BLOCK_62 -->

<!-- BLOCK_63 | J4ZvdTYBBo0bK9xuAZgcvR45n9c -->
##### Q：基于模板发起的任务出现任务偏离或者夹杂上一次任务的上下文的情况<!-- END_BLOCK_63 -->

<!-- BLOCK_64 | K1Jodj6bwo5cEZxBuYRcdff4n9g -->
A：如果发现类似情况，可能是因为：
- 自动生成的模版经验泛化性不足。如：代码类任务可能无法抽象出一个通用的流程，不同参数的流程差异很大无法参考
- 复制了别人的模版，而原模版和修改后的模版任务存在差异
<!-- END_BLOCK_64 -->

<!-- BLOCK_65 | Duhed1m2go8qhSxbMJ5cUlHunvh -->
可以尝试重新创建模版或者修改模版任务描述。
<!-- END_BLOCK_65 -->

<!-- BLOCK_66 | KB8iddgNXoiBNXxdHHNcLibrn4d -->
##### Q：变更模板信息后 “操作指南”失效怎么办？<!-- END_BLOCK_66 -->

<!-- BLOCK_67 | PDZPdrImCopH3RxGK3scNapmnjg -->
A：当你修改了 需求指令、参数核心信息 或 拓展工具 等关键信息，现有操作指南会失效。可基于新版模板发起一次任务，得到满意的结果后，可在任务详情页添加/更新操作指南。
<!-- END_BLOCK_67 -->

<!-- BLOCK_68 | SZDVdt2yeooCsLxUsIHcXxTanSd -->
##### Q：历史版本任务能直接更新“操作指南”吗？<!-- END_BLOCK_68 -->

<!-- BLOCK_69 | RTVTdIGmPoftNlx41jRcIviOnUK -->
A：不可以。“操作指南”的作用是在模型执行时给到历史优秀经验作为参考，以提升最终生成结果的稳定性；与模板的版本之间存在关联关系。若任务基于模板的历史版本创建，页面会提示需要基于最新版本的模板重新发起任务后，再更新操作指南。
<!-- END_BLOCK_69 -->

<!-- BLOCK_70 | VpfYdPKRZoBmz4x4FLJcPCmWnUd -->
##### Q：迁移模板的时候需要同步迁移模板关联的自定义 MCP 吗？<!-- END_BLOCK_70 -->

<!-- BLOCK_71 | H8KEdY6T6oXtJ8xXVUVcS0EXnXe -->
A：不需要。Aime 目前已支持跨空间调用 MCP。因此，导入模板时，其关联的 MCP 不会被一同迁移，但这不影响模板的正常使用。模板在新的空间运行时，依然会自动调用其原始的 MCP 配置。
<!-- END_BLOCK_71 -->

<!-- BLOCK_72 | DuTZdPirAozqknxQx1dcIibln2b -->
##### Q：我更新了模板的指令或参数，之前的批量参数表还能继续用吗？<!-- END_BLOCK_72 -->

<!-- BLOCK_73 | BPKtdeOr4oMCqGxFiB5c8LQln6c -->
A：不建议直接复用。模板更新后，需要重新生成并下载最新的参数集模板表格，再按照新的字段说明填写并提交，避免字段不一致导致解析失败或任务被跳过。
<!-- END_BLOCK_73 -->



<!-- BLOCK_74 | Qeewdr1GOoSyUkxESgxcLPyVnwc -->
# 附录<!-- END_BLOCK_74 -->

<!-- BLOCK_75 | CBtndSxhBozt1vxGirochacnnjc -->
1. 字段、概念与说明
<!-- END_BLOCK_75 -->

<!-- BLOCK_76 | RJOWdBGDzoQykFxlwffcDxMbnTe -->
<table header-row="true" col-widths="130,690">
    <tr>
        <td>字段 / 概念</td>
        <td>说明</td>
    </tr>
    <tr>
        <td>**参数名称**</td>
        <td>禁止为空，长度建议不超过 20 字符；自动过滤首尾空格。</td>
    </tr>
    <tr>
        <td>**填写说明**</td>
        <td>对应字段的输入指南，说明类型与格式规范，支持填写链接。</td>
    </tr>
    <tr>
        <td>**默认参数**</td>
        <td>每次使用时自动预填；使用者如有改动，下次回显其最近一次配置；支持链接与附件。</td>
    </tr>
    <tr>
        <td>**必填项**</td>
        <td>打开后该字段为必填；系统会在发送前进行校验并提示模板使用者缺失项。</td>
    </tr>
    <tr>
        <td>**上传文件**</td>
        <td>与当前任务类型兼容的附件上传开关。</td>
    </tr>
    <tr>
        <td>**工具与扩展**</td>
        <td>可按需添加/删除模板任务运行所需的其他工具连接与智能助手扩展。</td>
    </tr>
    <tr>
        <td>**公开范围**</td>
        <td>可设置为 个人、项目内公开、全局公开
建议优先选择与任务场景匹配的可见范围，并注意保护个人隐私数据</td>
    </tr>
    <tr>
        <td>**操作指南**</td>
        <td>原 “执行规划” 字段。**基于历史任务总结提炼得到**，规定了有哪些步骤，每一步的目标是什么、怎么做。
**适合步骤固定的任务**，比如数据处理；效果最好，灵活度差</td>
    </tr>
</table>
<!-- END_BLOCK_76 -->

<!-- BLOCK_77 | AY44dpVLvoGfdBxKJDScUD1InHc -->
1. 关联功能友情链接
	1. [Aime - 定时任务功能使用手册](https://bytedance.larkoffice.com/wiki/A9wswaghqiAAoxkWsb7cdISLnlb)
<!-- END_BLOCK_77 -->

<!-- BLOCK_78 | Z0Zbdpo7Gobi14xDigFcbFYDnwf -->
# 问题反馈<!-- END_BLOCK_78 -->

<!-- BLOCK_79 | ZJafdmGLqoXSTLxvoCTcLG0Qnzd -->
<grid cols="2">
<column width="50">
</column>
<column width="50">
  如果创建或使用模板过程中遇到问题（例如模板经验效果有问题或者不符合预期），请通过[问卷](https://bytedance.larkoffice.com/share/base/form/shrcnNAx1NpbBap6uGyActpSjch)、用户群 或联系@(caoyunxiang@bytedance.com)@(dingbo.2020@bytedance.com)@(wangyiyun.0423@bytedance.com)反馈，感谢您的支持！
</column>
</grid>
<!-- END_BLOCK_79 -->




</content>
