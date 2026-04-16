<title>Aime 工作流功能介绍</title>
<url>https://bytedance.larkoffice.com/wiki/BsMqwZwUdirlwFkTCj7cYjGVnDg</url>
<content>
<!-- BLOCK_1 | doxcndGFSfAzunOoFjRD8Aq0Bod -->
<callout icon="bulb" bgc="3" bc="3">
你还在手动串联各个研发环节吗？
赶紧来试试 Aime 全新推出的**工作流功能** 🚀，集**模板串联、自动化执行、多轮对话、参数传递**于一身，让你的研发流程更高效、更智能！
[Aime - 项目空间使用手册](https://bytedance.larkoffice.com/docx/HC01dKOC3ohxomxwbG0c3VRVn9g?from=self_signature)
[Aime 项目空间：赋能团队研发提效](https://bytedance.larkoffice.com/docx/QtAjdMbSEo8x7HxgCOmcUJjqn8e)
任何问题反馈可联系：@(xuezhongliang@bytedance.com)@(wuyunfei.vip@bytedance.com)
</callout>
<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | doxcn7hTCyZ9NwiBSx4IEBPLhSf -->
# 功能介绍<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | doxcnYaHUzDYbUznBWNnCRCJlOe -->
Aime 工作流功能旨在将不同的 AI 环节进行串联，配置成自动化任务，满足用户在实际研发过程中的各种场景需求。无论是需求分析、技术方案生成，还是代码开发、测试部署，都可以通过工作流实现全流程自动化。
<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | doxcnZUC0RVtUjIs31aRu2B8JAc -->
工作流功能的核心价值在于：
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | doxcnpDnIA5GU3GbhKMydLBY2pb -->
- **模板串联**：将原来的单点功能（模板任务）串联形成不同场景下的 SOP，提升场景可用性
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | doxcnGA0AyyiACGZ4bWUaIg1hZf -->
- **灵活编排**：支持定时任务触发器、Codebase 触发器、Aime 模板任务、Bits 自由流水线等多种节点类型
<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | doxcnVBdRWKJchHlge6NAZUeAxc -->
- **智能执行**：单个节点支持多轮对话（上下文共享），支持多版本（上下文隔离）
<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | doxcnmyGK2cf3ZBBtR9kvmnu3Nb -->
- **参数传递**：跨节点实现上下文总结 + 产物传递（文件、图片、Code、链接）
<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | doxcnIaszVopqRNRMaidz6L2p9f -->
- **效果调优**：支持从任意节点重跑，直到达到满意的效果，再开始后续任务
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | GSMGdiwz5oPWjUxLqm7cJo2gnTc -->
![图片](img_A4okbWYYSoyQsWxpEc2cqNjanGc.png)
<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | doxcnpWtMlztYOZLIpJLvjzr6cd -->
# 使用方式<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | doxcnEGTxhdbAYuFjDIWbrkWMof -->
## 功能须知<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | doxcnT60Fq0SL9eMAI1PSBk4V5d -->
<callout icon="saluting_face" bgc="2" bc="2">
1. 工作流功能目前仅支持在**项目空间**内使用，且**已全量开放**。如若没有项目空间，可联系@(heyilin.eve@bytedance.com)申请。当天申请的项目空间可以下一个工作日查看 Aime 发的消息提醒。
</callout>
<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | doxcnisd1lfB0gqgTpxNk3Dggbc -->
## 使用流程<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | Z3ULd6DsGoJeBnxOOilc0B7RnNT -->
工作流任务，需要基于工作流模版发起。
<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | doxcnpvbzCwmChsYUOUVHYGaqWb -->
### 创建工作流模版<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | doxcn7sBWuYux4AkXGxif3gp3Ad -->
#### 进入 Aime 项目空间，点击首页的「新建工作流」按钮<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | OsMNdaNN1oO5WyxwPybcA67snhc -->
![图片](img_AScubjvmIoHQLIx7H4kcZdJ1npd.png)
<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | doxcnyamjapD8kQH7rfzgHD38we -->
#### 进入工作流配置页面，拖拽需要的任务节点到画布中<!-- END_BLOCK_19 -->

<!-- BLOCK_20 | BAihd4p6Pof9F1xoJ0tcJXNznXd -->
目前节点类型支持 Codebase 触发器、定时任务触发器和 Aime 模版任务。
<!-- END_BLOCK_20 -->

<!-- BLOCK_21 | VbrqdvUkmo66Njxq0lAcSOdanDf -->
![图片](img_IdCcbb6bGoPiNtxT4yucBAiJn7c.png)
<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | PjbddziKzo9HZqxuKLBcdeGhnef -->
#### 定义节点的输入参数、输出参数<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | OETqdzJV8oyfqWxHJx2ccjn5nDe -->
节点配置说明：
前置节点的输出参数，都可以被后续节点的输入参数引用。
<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | XbpPdLlqsoLT66xhpcCc60KJnIg -->
- 输入参数，支持 2 种类型:
默认参数（固定值）与引用参数（引用前置节点的输出参数)。
<!-- END_BLOCK_24 -->

<!-- BLOCK_25 | FzsjdL0jjow2psx1Q54cTjDxnLe -->
- 输出参数，支持 5 种类型: 
文本：由模型根据当前任务的上下文进行总结，用户填写的`参数描述`将作为模型总结的重要依据。
代码、链接（飞书链接、网页链接等）、图片、文件（markdown、txt 文件等）：从当前任务生成的产物中进行筛选，`参数描述`将作为模型选择的重要依据。
<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | NFaidKcJ0o7IRLxifnYcasPVn8c -->
- 节点执行人：以指定用户的身份运行当前节点的任务。
<!-- END_BLOCK_26 -->

<!-- BLOCK_27 | BfFydiButo8Riax0EqlcyPGMnNk -->
- 通知方式：当节点运行需要人工确认或任务完成后，消息通知的对象。
<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | JlAKdRw4soDbO8xy7dLc3XWInUd -->
- 交互配置：节点执行完成后，是否需要人工确认执行任务的结果、任务的产物。**需要多轮对话、不断调优的场景**可以开启`执行完需要人工确认`；否则，当前节点执行完毕后，会自动开始运行下一节点。
<!-- END_BLOCK_28 -->

<!-- BLOCK_29 | ZFYTdx9Xlo4PRIxZyL5ccWzinFc -->
![图片](img_PPqFbwuh4oBSAdxz9kicuVd0nvh.png)
<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | GY2Kdnyx8oBDHvxKUo2cmAhJnqc -->
#### 保存、发布工作流模版<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | R4NvdB9v1oNmnKxLaj5cK66mnPg -->
建议修改模版的默认名称，提高辨识度。`保存`、`发布`工作流模版后，就可以基于该模版发起任务。
<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | F1Wtd2TTPoBt2ExaAKhc78bmnBc -->
模版可见范围：
<!-- END_BLOCK_32 -->

<!-- BLOCK_33 | E9fbdEo0foRLs0xUy1UcO5ahnVc -->
- 空间内可见：项目空间内所有人都可以基于该模版发起任务，且工作流任务默认空间内公开。
<!-- END_BLOCK_33 -->

<!-- BLOCK_34 | FUusdZZe0oN7lLxwAK7cNEMnnsc -->
- 仅个人可见：仅模版创建者可基于该模版发起任务，且工作流任务默认仅个人可见。
<!-- END_BLOCK_34 -->

<!-- BLOCK_35 | V7sidut9OohRxNxb5l6cX3J2nDg -->
![图片](img_RaJObLY2KoiQfJxrNNEcX2InnVc.png)
<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | doxcnW6qmZYC4CX2WqTE76WiuEb -->
### 发起工作流任务<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | doxcn8XSKc7RdsnioJfddZu4rvd -->
#### 模版编辑页面，发布模版后可以`立即运行`<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | Fxt2dro63oD8z7xg7gAcVutgntb -->
![图片](img_JWG0bOzKQoaAYpxl4ricekMbnEd.png)
<!-- END_BLOCK_38 -->

<!-- BLOCK_39 | doxcnrrPt9CM6XSuNcLVX9qW4Zf -->
#### 项目空间首页，基于已有的模版发起任务<!-- END_BLOCK_39 -->

<!-- BLOCK_40 | B8OcddEPBordVDxQ0OIcKCexnQe -->
![图片](img_Ggd3bBd1iovPGmxhFCXcX2upnfh.png)
<!-- END_BLOCK_40 -->

<!-- BLOCK_41 | SA3AdLVHqofN3MxkitqcwZA5noi -->
### 操作工作流任务<!-- END_BLOCK_41 -->

<!-- BLOCK_42 | TIpxd6iMwomvPfxPAI2c25E0nvb -->
#### 人工确认与多轮对话<!-- END_BLOCK_42 -->

<!-- BLOCK_43 | SgindwIMXoGKnnxzZ9hcqNMTnKc -->
如果需要调整当前的产物，可以继续对话，直到符合预期再点击`确认`按钮进入下一节点。
<!-- END_BLOCK_43 -->

<!-- BLOCK_44 | AIu9dAqAQojQadxKDmfcXG7Mnyg -->
![图片](img_QDbXbD7OzogJARxXzKecw6uQn5f.png)
<!-- END_BLOCK_44 -->

<!-- BLOCK_45 | H3YxdXgFEo9omVxfn2Bcd4f0nDh -->
#### 从指定节点开始重新运行<!-- END_BLOCK_45 -->

<!-- BLOCK_46 | UFmjdcwkZoWF0Ox5gAXcbSTBnSe -->
如果在工作流运行的过程中，发现前置节点的产物需要调整，可以从指定节点重新运行。支持 2 种方式：
<!-- END_BLOCK_46 -->

<!-- BLOCK_47 | Tn4SdKuGvoZ0Bbx1syQceX72ncb -->
- 保留前置节点的任务上下文
<!-- END_BLOCK_47 -->

<!-- BLOCK_48 | X1LVd14mFoKlWVxEdEYcRXrhnlc -->
可以在历史节点中继续对话，修改历史产物。在完成修改后，点击`完成`按钮，将基于修正后的产物重跑后续节点。
<!-- END_BLOCK_48 -->

<!-- BLOCK_49 | Vzu8dFxckovlwRx8G17ciIC3nmg -->
![图片](img_GxR3bHbZJoxgeuxOIRmcNOgwnzh.png)
<!-- END_BLOCK_49 -->

<!-- BLOCK_50 | UVLPds4GuoCcj5x8koIc0mvtnD2 -->
- 舍弃前置节点的任务上下文，完全重新开始
<!-- END_BLOCK_50 -->

<!-- BLOCK_51 | WCWldFa7CoAdwAx2zEZcPQzdnHv -->
将从指定的节点创建新版本，开启全新的任务流程。未重跑的节点产物，可以继续被引用。
<!-- END_BLOCK_51 -->

<!-- BLOCK_52 | TlfddYL2aoM5Afxviogcd9pBnvf -->
![图片](img_MCBZbVeJIoko2sxcY8qc76wKnVh.png)
<!-- END_BLOCK_52 -->

<!-- BLOCK_53 | CZRNdkuzJod4o5xX5nVc7iSTnDb -->
只有节点的最新版本，才允许继续交互。
<!-- END_BLOCK_53 -->

<!-- BLOCK_54 | Hl2Vd3meqoABY3xD6JmcPFF2nfQ -->
![图片](img_PoE0bwZvporzN5x4t1bcE9aynsc.png)
<!-- END_BLOCK_54 -->

<!-- BLOCK_55 | YQIRdOQWloQ39wxyFMWcUvXNnVc -->
#### 取消运行中的任务<!-- END_BLOCK_55 -->

<!-- BLOCK_56 | Vcpnda8kfoiSwFxsQV5cXZaPnIr -->
![图片](img_VfJbb5zbAof5YNxh9bFc6JM6nmb.png)
<!-- END_BLOCK_56 -->

<!-- BLOCK_57 | doxcnmuCG5m051fMpfFrlhbZLLf -->
### 管理历史任务<!-- END_BLOCK_57 -->

<!-- BLOCK_58 | doxcnCSxnTiyedycTHIWM6ygM2e -->
#### 在「我的任务」页面，可以管理、查看个人的近期工作流任务<!-- END_BLOCK_58 -->

<!-- BLOCK_59 | IcCvdnHxrozwzQxTUQtcC8JynZd -->
![图片](img_QgjebStXjo0lgNxULyJcgHehnEc.png)
<!-- END_BLOCK_59 -->

<!-- BLOCK_60 | doxcncMTaHr62O5AGsuOmk1ldne -->
#### 在「历史任务」页面，可以管理、查看个人与空间内公开的工作流任务<!-- END_BLOCK_60 -->

<!-- BLOCK_61 | Qia2d3sf5oiWEIxulUOcCOBAnPg -->
![图片](img_IYnRbbWmqo6jGYxtuEhcwTA0nNd.png)
<!-- END_BLOCK_61 -->

<!-- BLOCK_62 | doxcnWtPXEbQWXNPue1eBGxbQyd -->
# 线上典型使用姿势参考<!-- END_BLOCK_62 -->

<!-- BLOCK_63 | doxcnRrykqef7jBEPOqJtbRyNYc -->
<table col-widths="250,250,250,250">
    <tr>
        <td>场景</td>
        <td>细分场景</td>
        <td>案例介绍</td>
        <td>能力介绍</td>
    </tr>
    <tr>
        <td>**研发流程自动化**</td>
        <td>**需求到代码全链路**</td>
        <td>- **案例1:** 工作流串联 [需求](https://aime.bytedance.net/chat/474cb356-2f72-4771-9567-cb3aed740d9f?workflowRunId=59f1fc93-55cd-4b3a-ac31-0c2e6143c690)[分析-技术方案-代码开发](https://aime.bytedance.net/chat/c1a4c814-5f83-410b-bc61-84340c37390b?workflowRunId=60b856bf-abcf-4e4e-8acf-9dfc2f7055e6)</td>
        <td>- **模板串联**：将需求分析、技术方案生成、代码开发等环节自动串联
- **参数传递**：前一环节的产物自动传递给下一环节</td>
    </tr>
    <tr>
        <td>**代码质量保障**</td>
        <td>**CodeReview 自动化**</td>
        <td>- **案例2:** [Codebase 触发器-CodeReview & 修复](https://aime.bytedance.net/chat/2bd8f975-be08-46f9-a3ae-2dedda4a5a2f?workflowRunId=d7924cc6-0311-4361-b2dd-b6ca7db1c75d)</td>
        <td>- **事件触发**：代码提交后自动触发 CodeReview
- **智能修复**：自动识别代码问题并提供修复建议</td>
    </tr>
    <tr>
        <td>**多轮交互优化**</td>
        <td>**复杂任务处理**</td>
        <td>- **案例3:** [多轮对话](https://aime.bytedance.net/chat/c1a4c814-5f83-410b-bc61-84340c37390b?workflowRunId=60b856bf-abcf-4e4e-8acf-9dfc2f7055e6)</td>
        <td>- **上下文共享**：单个节点支持多轮对话
- **效果调优**：支持从任意节点重跑</td>
    </tr>
</table>
<!-- END_BLOCK_63 -->

<!-- BLOCK_64 | doxcnSGSydGXbIGo5NGAzm4E5qc -->
# 常见问题<!-- END_BLOCK_64 -->

<!-- BLOCK_65 | doxcnrQQjVAYm06Yve8Oxz6zQXe -->
## Q1：工作流支持哪些节点类型？<!-- END_BLOCK_65 -->

<!-- BLOCK_66 | doxcn3I5VdaO93uYHdlEbsvgRUg -->
**A：**目前支持定时任务触发器、Codebase 触发器、Aime 模板任务、Bits 自由流水线等多种节点类型，可以根据实际场景编排合适的工作流程。
<!-- END_BLOCK_66 -->

<!-- BLOCK_67 | doxcn09hC8T1J2jS6e299inRsHh -->
## Q2：如何在工作流中传递参数？<!-- END_BLOCK_67 -->

<!-- BLOCK_68 | doxcnehbo8v8sCRxuGIHIonawSe -->
**A：**工作流会自动实现跨节点的参数传递，包括上下文总结和产物传递（文件、图片、Code、链接等）。用户在配置节点时，可以通过参数引用传递需要的参数；运行中也可以切换到 `默认参数` 类型，就能手动设置值。
<!-- END_BLOCK_68 -->

<!-- BLOCK_69 | TPpsdeQ2coBgWkxbFjOcZFKnnIg -->
![图片](img_WKuOb93euowmspxZ0qec9Jafnse.png)
<!-- END_BLOCK_69 -->

<!-- BLOCK_70 | doxcnos2NdUSV0XNdXWrLtQbMXc -->
## Q3：工作流执行失败了怎么办？<!-- END_BLOCK_70 -->

<!-- BLOCK_71 | doxcnql7VdwavpNUkAuCrDZMVqg -->
**A：**工作流执行失败后，可以在「运行工单」页面查看详细的错误信息。支持从失败节点开始重跑，方便用户排查问题和优化流程。
<!-- END_BLOCK_71 -->

<!-- BLOCK_72 | doxcnvCcS8IfgBmafbZt28fOO3b -->
## Q4：工作流功能是否支持自定义扩展？<!-- END_BLOCK_72 -->

<!-- BLOCK_73 | doxcnCKoQvseCGDYp6GylQIWORc -->
**A：**是的，工作流功能后续将提供标准的集成方案和框架，适配业务个性化诉求。后续规划中，还将支持业务 Agent 的接入与能力扩展。
<!-- END_BLOCK_73 -->

<!-- BLOCK_74 | doxcn46hO2pWTFgJUOUhtUlkCph -->
# 问题反馈渠道<!-- END_BLOCK_74 -->

<!-- BLOCK_75 | FVXdd7jVfo0KoQxqeYac8iBfnRd -->
可登记到文档：[Aime - 工作流功能 DogFooding 问题反馈](https://bytedance.larkoffice.com/wiki/D4ULwmorqiqcIYkC1ySc7PXZnuO?renamingWikiNode=false)
<!-- END_BLOCK_75 -->

<!-- BLOCK_76 | doxcnlFVxJRL6kNkq4HaYKcwrwb -->
- 工作流模版配置问题联系 @(wuyunfei.vip@bytedance.com)
<!-- END_BLOCK_76 -->

<!-- BLOCK_77 | doxcnjPXGRwqLsxhXWKNpGn4jbe -->
- 工作流任务执行问题联系 @(xuezhongliang@bytedance.com)
<!-- END_BLOCK_77 -->

<!-- BLOCK_78 | doxcnmuHSZEgkXgDjMQn1IQJeyd -->
- 产品诉求及其他联系 @(zhujingyan.43@bytedance.com)@(litengfei@bytedance.com)
<!-- END_BLOCK_78 -->




</content>
