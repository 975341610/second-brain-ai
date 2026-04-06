<title> Aime x Meego 全自动 AI 原生需求交付流程</title>
<url>https://bytedance.larkoffice.com/wiki/OK1zw57lNiNtbTksA5icDPVXnnf</url>
<content>
<!-- BLOCK_1 | doxcn0gu9NdsIQSYzzSfS9jR2xb -->
<callout icon="bulb" bgc="3" bc="3">
**一句话定位：**基于 Meego 自动化落地 Aime 研发全流程闭环，通过 Meego 平台自动化配置，自定义工作项流程，接入 Aime 插件发起研发活动任务、协同 Meego 交互。任何问题请联系@(hanxu.conch@bytedance.com)
[Aime 项目空间：赋能团队研发场景提效](https://bytedance.larkoffice.com/docx/QtAjdMbSEo8x7HxgCOmcUJjqn8e)
[Aime 工作流功能介绍](https://bytedance.larkoffice.com/wiki/BsMqwZwUdirlwFkTCj7cYjGVnDg)
</callout>
<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | OzIFdhAW6oPLC7x2rwhcVzCpnQf -->
<!-- 视频文件：Aime x Meego 全自动 AI 原生需求交付流程.mp4 (视频文件不支持下载，请在原文档中查看) -->

<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | doxcnf2LHW7nk6jjVc46m7egDjh -->
# 简介<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | doxcnrXZAbU7eETxW0JlWfQ1pqf -->
Aime 项目空间 Meego 自动化能力是一套基于 Meego 平台的流程自动化解决方案，旨在通过 Meego 原生事件和智能任务编排，实现 Aime 智能研发全流程的自动化闭环
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | doxcneWmipCCccrQb2jRtcRpCCc -->
- **灵活配置**：支持在 Meego 平台配置自动化流程，可根据业务场景灵活自定义事件流
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | doxcnXCOAGtvlVawXJStD00Mnig -->
- **原生集成**：支持完整的 Meego 原生事件和规则集，确保与 Meego 平台的深度融合
<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | doxcn3xHgrgrvHWj41rqqiU1jMf -->
- **智能协作**：接入 Aime 插件创建工作流任务/模板任务，完成相应研发工作并与 Meego 实现无缝交互
<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | doxcngoG5kGMrdK86nl18J9ngDf -->
## 核心价值<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | doxcnntx9RSLyaksH0g2C77Ipde -->
Meego 自动化能力为研发团队带来以下核心价值：
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | doxcnj57CzKQCJYkKrTyuWScfZc -->
- **提效降本**：通过自动化触发和执行研发任务，减少人工干预，提升研发效率，降低人力成本
<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | doxcn3mx4xrTq9JBgrysjzPb1Ve -->
- **流程标准化**：将研发流程标准化、规范化，确保每个环节都按照最佳实践执行，提高交付质量
<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | doxcndPDh5u6cLz1aDNoyzO5b6d -->
- **信息闭环**：实现研发信息在 Meego 和 Aime 之间的双向流通，确保信息不丢失、可追溯
<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | doxcnznvK42MIq9IStT0sWnDxRd -->
- **智能赋能**：结合 Aime 的 AI 能力，为研发流程提供智能解决方案，如生成技术文档、代码等
<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | doxcnOhAGnVShmNo9ALNRPNO8Yb -->
- **灵活适配**：支持根据不同业务场景自定义流程，满足多样化的研发需求
<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | doxcndc9jLGKzCCS8GfT8VX4esb -->
- **全链路覆盖**：从需求评审到开发、测试、部署，覆盖研发全链路的自动化管理
<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | RfTkdql2PoFUAOxlJZnca9jbnHd -->
# 前置准备<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | QuNrdeRjkoSN1axFzIwcdreCnbd -->
## 创建工作流模板<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | OTm5ds2WdosY2cxYyZHcTDGAnNg -->
> 「仅支持项目空间，个人空间不支持工作流」[Aime 工作流功能介绍](https://bytedance.larkoffice.com/wiki/BsMqwZwUdirlwFkTCj7cYjGVnDg)
> 
<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | D5YsdmThqotpSIx7yhrcpgpinQc -->
<!-- 视频文件：快速创建工作流.mp4 (视频文件不支持下载，请在原文档中查看) -->

<!-- END_BLOCK_19 -->

<!-- BLOCK_20 | K6g1drZwTogN3AxGWOicDD5znwd -->
## 绑定 Meego 空间<!-- END_BLOCK_20 -->

<!-- BLOCK_21 | I2E1dr5EboExybxkreUc4c1gn9g -->
> 需要是 Aime **空间管理员权限（仅在手动发起 Aime 任务时必要，如果只想接入自动化流程可跳过）**。可以点击**左上角空间设置**查看空间成员与权限
> 
<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | FxAOdcITpoB3vbxrgD4cLzmonUb -->
<!-- 视频文件：配置 Meego 平台.mp4 (视频文件不支持下载，请在原文档中查看) -->

<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | doxcnIcLs1P7hzspbMMWHi7bMRe -->
# 功能速览<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | RBzgdYCzwodXYDxNalScq8Lsnkc -->
## 自动修缺陷<!-- END_BLOCK_24 -->

<!-- BLOCK_25 | K2IhdUKtDoYx3IxdQ7Lcc32YnSf -->
> **<font color="green">场景：</font>**当 Meego 缺陷单创建后自动触发一个工作流任务。
> 
<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | XWD9dVepboxjw6xnngScUO3Onud -->
<!-- 视频文件：缺陷自动触发工作流.mp4 (视频文件不支持下载，请在原文档中查看) -->

<!-- END_BLOCK_26 -->

<!-- BLOCK_27 | CqwgdTf5uozHdexttL5csKLenLx -->
## 自动做需求<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | Sa4GdItb9oSkZqxjbAwccHtMne0 -->
> **<font color="green">场景：</font>**当 Meego 需求进入开发阶段后自动触发一个工作流任务。
> 
<!-- END_BLOCK_28 -->

<!-- BLOCK_29 | E0bcdMekMozvpCxCjGSc31rJnnE -->
<!-- 视频文件：需求自动写代码.mp4 (视频文件不支持下载，请在原文档中查看) -->

<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | EFWkdV7Xyo2ZtRxfV0Xc3hbDnpg -->
## AI 节点发起任务<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | KiHpdAi1mo6JCYxHtxKclucungd -->
> **<font color="green">场景：</font>**接入 Aime AI 节点，选择快捷指令一键发起各类任务，智能托管交付流程
> 
<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | QGUmdmziroVQMZxDEEhcNo0RnDh -->
<!-- 视频文件：屏幕录制2026-03-17 15.47.12.mov (视频文件不支持下载，请在原文档中查看) -->

<!-- END_BLOCK_32 -->

<!-- BLOCK_33 | KlXLdVUOao0JXwxuUMzcTf5sn4q -->
## 手动发起<!-- END_BLOCK_33 -->

<!-- BLOCK_34 | Z1nhdh1vCojgnFxJpoVccxUBnZf -->
> **<font color="green">场景：</font>**当在使用 Meego 的时候，在工作项详情页发起一个需求的 Aime 工作流（**需要在项目空间绑定 Meego**）。
> 
<!-- END_BLOCK_34 -->

<!-- BLOCK_35 | NPeud91MOokojZxDBWGcJn6snNb -->
<!-- 视频文件：手动发起工作流任务.mp4 (视频文件不支持下载，请在原文档中查看) -->

<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | VDEGdpUhFoX2tbxtksVciOJZn2d -->
## 触发模版<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | Vzwad6UeBonDXJxKOyQcfKhfnfd -->
<!-- 视频文件：meego 节点触发模板.mp4 (视频文件不支持下载，请在原文档中查看) -->

<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | doxcn0tWKGaeXAS5V05PM8408Hf -->
# 详细说明<!-- END_BLOCK_38 -->

<!-- BLOCK_39 | doxcnbqT0fd9KqppaPCIwuHTKyf -->
以下将以配置一个完整的需求工作项流程作为示例，详细说明 Meego 自动化能力的使用方法。
<!-- END_BLOCK_39 -->

<!-- BLOCK_40 | doxcnll8ddm8RsrGF7HyUtr5vHh -->
## 新建自动化规则<!-- END_BLOCK_40 -->

<!-- BLOCK_41 | PqWid78VBocMtkxepjDcInbwn3b -->
> 在 Meego 平台自动化 tab 新建规则。<font color="yellow">需要空间管理员权限</font>
> 
<!-- END_BLOCK_41 -->

<!-- BLOCK_42 | doxcnmm2792dDn8JuVDlieHWVZb -->
<grid cols="2">
<column width="50">
  ![图片](img_FJefbK38Foi3vkxMYs3c9Ib3ncc.png)
</column>
<column width="49">
  ![图片](img_SlbDbuPeuo4cjqxd6cEcBPwdnug.png)
</column>
</grid>
<!-- END_BLOCK_42 -->

<!-- BLOCK_43 | doxcnPOnTk5cg4b6lS1j9hXRyEg -->
## 配置触发器<!-- END_BLOCK_43 -->

<!-- BLOCK_44 | SfO1dlD5Yogadtxfu8ocKm7bnKd -->
> 设置触发条件，例如当需求评审节点状态流转到进行中时，触发事件
> 
<!-- END_BLOCK_44 -->

<!-- BLOCK_45 | doxcnA1Uxw4UmloXU9pqc0dbLae -->
![图片](img_LciVbx3wuobsOSxwLBPclgBRnmf.png)
<!-- END_BLOCK_45 -->

<!-- BLOCK_46 | doxcnycE70oZVsGqJxYLk6xdPDd -->
## **配置过滤条件**<!-- END_BLOCK_46 -->

<!-- BLOCK_47 | Z0w2dLc7OopXfpxovsJcsE3Un9f -->
> 设置事件过滤条件，例如业务线属于「xxx」且存在需求文档时继续流程
> 
<!-- END_BLOCK_47 -->

<!-- BLOCK_48 | doxcncW0WukpAzRmGnDPwvMQEuc -->
![图片](img_Au7mb2CMEo5XbuxG8xgcMCLTnFd.png)
<!-- END_BLOCK_48 -->

<!-- BLOCK_49 | INredhgD0o4nBHxrTdYcP4W1nUb -->
## 配置 Aime 插件操作<!-- END_BLOCK_49 -->

<!-- BLOCK_50 | OtxDdqWtIo2rLaxnEdPcZTSEncf -->
> 选择 Aime 插件，添加发起创建 Aime 模板任务操作；填写控制面、空间 ID、模板 ID/shared_id 、触发人身份等表单项
> 
<!-- END_BLOCK_50 -->

<!-- BLOCK_51 | UoyKd25ggoTffGxXXSbcFXbKnCf -->
<grid cols="2">
<column width="49">
  ![图片](img_Ffd3bXYaUooOAbxG8PWctbNPnsc.png)
</column>
<column width="49">
  ![图片](img_JKuwb6Xs5oiOc3x2KzUc09s3ngf.png)
</column>
</grid>
<!-- END_BLOCK_51 -->

<!-- BLOCK_52 | doxcn3bqzKtbmYzxy5qlDoOF3sd -->
## 任务结果通知<!-- END_BLOCK_52 -->

<!-- BLOCK_53 | RWvhdnsnYoSGHNxjtGwcvJhNnwg -->
> 当 Aime 任务执行完成会按表单配置把结果发送到飞书卡片
> 
<!-- END_BLOCK_53 -->

<!-- BLOCK_54 | doxcnko0BTUi7oieREHdxGUkATg -->
![图片](img_G2q1bNnVgoEwHWxMsoDcUhzLnHf.png)
<!-- END_BLOCK_54 -->

<!-- BLOCK_55 | doxcntikjYywSMSIgEtdMsde24d -->
## 获取空间 ID 和模板 shared ID<!-- END_BLOCK_55 -->

<!-- BLOCK_56 | Nie1dUNLGo1rxfxnkykcB7Uon9b -->
> 获取方式如下；<font color="yellow">注意请选择空间公开或全局公开模板，否则将无法发起任务</font>
> 
<!-- END_BLOCK_56 -->

<!-- BLOCK_57 | CEKDdMG9EoUyUDxfbrDcSpJKncf -->
<!-- 视频文件：屏幕录制2026-02-10 21.26.47.mov (视频文件不支持下载，请在原文档中查看) -->

<!-- END_BLOCK_57 -->

<!-- BLOCK_58 | doxcnEyIx7JFzadFpGHAZCfeU0d -->
## 支持分支流程<!-- END_BLOCK_58 -->

<!-- BLOCK_59 | Z6ObdVeyno3zpvx8dq5cgh4Znrb -->
> 支持添加分支，例如在需求节点进行时同时发起需求分析和编写测试用例两个任务
> 
<!-- END_BLOCK_59 -->

<!-- BLOCK_60 | doxcne252pt4lr3K5ijW6w43Vah -->
![图片](img_KFMLbLJteoGKlxxLUzCcSoZlnFb.png)
<!-- END_BLOCK_60 -->

<!-- BLOCK_61 | doxcnMAEa0QqPgCRqKWwOhDQuff -->
## 自动注入 Meego 链接<!-- END_BLOCK_61 -->

<!-- BLOCK_62 | GQsIdyv6LoR2L8xWVX1c3bQen6o -->
> 所有模板/工作流任务运行时会将 Meego 链接硬编码到提示词顶部，无需配置模板变量
> 
<!-- END_BLOCK_62 -->

<!-- BLOCK_63 | doxcnaJFOgVba4UfTjLNwvesgAg -->
![图片](img_UGhlbk4HDomCBSxm1ZRcDPdSnRf.png)
<!-- END_BLOCK_63 -->

<!-- BLOCK_64 | doxcnx4TI64FNP2gbLPgg7dM5ec -->
## 任务执行结果<!-- END_BLOCK_64 -->

<!-- BLOCK_65 | MODtdQ86ioucLOxKADEc1Hkvnub -->
> 任务执行成功后，会发送通知到需求群，并将生成文档写入对应字段（需要用户在任务模板中说明）
> 
<!-- END_BLOCK_65 -->

<!-- BLOCK_66 | JTxJdpqrTo0nZ7xIePJc0FOsn1b -->
<grid cols="2">
<column width="56">
  ![图片](img_Wc7DbQgl4onH4wxq7RjclYCTnmb.png)
</column>
<column width="42">
  ![图片](img_C14xbslRsosom6xiYL5cWgiqnih.png)
</column>
</grid>
<!-- END_BLOCK_66 -->

<!-- BLOCK_67 | doxcnJfONHVXieHvV2KWKzKvEOf -->
1. **问题排查**：当流程执行不符合预期时，请先进行自查。检查对应自动化规则的执行记录，是否有对应事件以及是否匹配了过滤条件。当报错属于插件时，请联系 Aime Oncall；否则请自行排查设置或发起 Meego Oncall。**请阅读 FAQ 中第 4、5 项**
<!-- END_BLOCK_67 -->

<!-- BLOCK_68 | doxcn3ZAgzfV1v1Wtw0kx3FJdOg -->
<grid cols="3">
<column width="32">
  ![图片](img_YxBubihYqoSbnQxJzqNcluthnOg.png)
</column>
<column width="32">
  ![图片](img_QvIrbsg34oNL7MxsjLkcDLKdn5b.png)
</column>
<column width="34">
  ![图片](img_KWSobBvhRo6Glwxswo8cjcPZn0e.png)
</column>
</grid>
<!-- END_BLOCK_68 -->

<!-- BLOCK_69 | doxcnWuHjgEB3CElGyAxGcwfYIb -->
# FAQ<!-- END_BLOCK_69 -->

<!-- BLOCK_70 | doxcnIlBB2VRCsLBMDLTVvejgMg -->
## 1. 和 Aime 空间 Meego 配置的关系<!-- END_BLOCK_70 -->

<!-- BLOCK_71 | doxcnz0mXjXQzCx4wVM4BO9PWFb -->
**A：**
<!-- END_BLOCK_71 -->

<!-- BLOCK_72 | doxcnlWjqMlnDG3lglnBiJyJRZc -->
- 二者能力上是正交的，即配置内容以及生成的任务互不干扰。
<!-- END_BLOCK_72 -->

<!-- BLOCK_73 | doxcnfnYztLoow1q6G0yP5JDRUg -->
- Aime 空间 Meego 配置后续**不再迭代（预期会逐步下线）**，为了获得更好的流程管理能力和交互体验，建议使用 Meego 自动化能力。
<!-- END_BLOCK_73 -->

<!-- BLOCK_74 | doxcnpuxwMkiRM1TBqZnkuPgjGc -->
- 启用 Meego 自动化能力建议关闭 Aime 空间配置
<!-- END_BLOCK_74 -->

<!-- BLOCK_75 | OZhHdLWw3oHTrCxrXWLckUE7nad -->
- **通过 Meego 插件手动发起 Aime 项目空间任务，需要在项目空间绑定 Meego**
<!-- END_BLOCK_75 -->

<!-- BLOCK_76 | CrysdaxL1otsNJxoc8OcrJrNnLd -->
<grid cols="2">
<column width="49">
  ![图片](img_K2xFb35vgoen7lxrDf8c2Xjrnqf.png)
</column>
<column width="49">
  ![图片](img_XpDhbcUXDolRaXxGtXccC39Knpd.png)
</column>
</grid>
<!-- END_BLOCK_76 -->

<!-- BLOCK_77 | doxcnS7PwSbq9J1MtcsAEjYUQud -->
## 2. 关于 Meego 自动化配置的详细介绍<!-- END_BLOCK_77 -->

<!-- BLOCK_78 | doxcnuBrhKfpZ9865fWRYnzRqOg -->
请参考 [Meego 官方文档](https://meego-hc.larkoffice.com/b/helpcenter/1ykiuvvj/61y8fqwv)
<!-- END_BLOCK_78 -->

<!-- BLOCK_79 | doxcnTQ3OAN38ONRpQ865y6XBPc -->
## 3. 目前支持的触发器类型<!-- END_BLOCK_79 -->

<!-- BLOCK_80 | doxcn4zGJX8wMzzdtLCdEOvIgxd -->
目前支持下图中的 7 类触发器，更多 Meego 原生事件类型支持高优迭代中
<!-- END_BLOCK_80 -->

<!-- BLOCK_81 | PCQedS7TJooDo3x2Ukdc0Xfmnff -->
![图片](img_EYWkbqMtFoo7wdxzgvRc6x1ynQd.png)
<!-- END_BLOCK_81 -->

<!-- BLOCK_82 | NY62dJIhVoIIRNxJQHRcPf6Xnhh -->
任务将以指定角色作为触发人发起
<!-- END_BLOCK_82 -->

<!-- BLOCK_83 | V0Y8dwI8AoC4LwxKdX4chfH9n7f -->
![图片](img_HfyCbqwsSoSiAdx8bpwc8LKlnQc.png)
<!-- END_BLOCK_83 -->

<!-- BLOCK_84 | doxcn0SdXNGlSWzallZ2pYRGwnh -->
## 4. 自动化执行记录为成功但未发起任务<!-- END_BLOCK_84 -->

<!-- BLOCK_85 | JaDtdgg7Fo2Dc4xITO1csC5Pnyg -->
![图片](img_VvWxbAZeToxA7zx7377cIDtznyb.png)
<!-- END_BLOCK_85 -->

<!-- BLOCK_86 | doxcnIfiqgznvfML6jlCwJqaHDg -->
**A：**请先自查，自查无误联系 Aime oncall 协助排查：
<!-- END_BLOCK_86 -->

<!-- BLOCK_87 | doxcnRxncJ9TLKWjLjUAXEMW6Uc -->
- **Aime&nbsp;插件表单配置入参是否正确**
<!-- END_BLOCK_87 -->

<!-- BLOCK_88 | doxcnbqUaRA56YzbYkXXQnR7XLh -->
- **用户是否有空间成员权限**
<!-- END_BLOCK_88 -->

<!-- BLOCK_89 | doxcnIBd6quCR10SRihB8cTxVIf -->
- **模板是否为空间公开**
<!-- END_BLOCK_89 -->

<!-- BLOCK_90 | doxcnFvMnxKJHCrQhEq8Hk5CSjb -->
- **模板不能有必填参数（如需注入变量，请通过修改模板 prompt 提取：如 PRD 取 meego 链接中的【xxx字段】，值将会在运行时注入）**
<!-- END_BLOCK_90 -->

<!-- BLOCK_91 | doxcn11B7qNyb7TBFyPSNqnsfJe -->
- **如果是工作流，模板第一个节点必须为模板类型（不能是触发器等类型）**
<!-- END_BLOCK_91 -->

<!-- BLOCK_92 | W5bZdK1b7obLqlxRlrvcejbwnTe -->
- **<font background_color="light_yellow">提 Oncall 请提供对应的自动化执行记录及 meego 工作项链接，方便快速解决问题</font>**
<!-- END_BLOCK_92 -->

<!-- BLOCK_93 | doxcnq7Ljpn6HGBNOxH9lMeDZgf -->
## 5. 自动化执行记录没有事件<!-- END_BLOCK_93 -->

<!-- BLOCK_94 | doxcnVP9IfoMcl8tGXltSCuvawg -->
**A：请关闭浏览器泳道插件，挂泳道操作不会有事件发起**
<!-- END_BLOCK_94 -->

<!-- BLOCK_95 | I9LPdPeyPoWPXOxLOnTc5GlMnQd -->
## 6. AI 节点使用说明<!-- END_BLOCK_95 -->

<!-- BLOCK_96 | H64YdSX1co2uPixeJrxcExwPn6d -->
请参考 [Meego 官方文档](https://meego-hc.larkoffice.com/b/helpcenter/1ykiuvvj/wmvff0ww)，管理员可配置模板接入 AI 节点或把已有工作项的普通节点转为 AI 节点
<!-- END_BLOCK_96 -->




</content>
