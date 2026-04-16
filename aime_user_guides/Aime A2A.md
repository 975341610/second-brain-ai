<title>Aime A2A</title>
<url>https://bytedance.larkoffice.com/wiki/LBSiwgQJGiHWx0k9guycFt05nge</url>
<content>
# 关于 Aime
## Aime 的定位
Aime 是专为字节同学打造的 AI Agent 工作平台，面向工作场景，集成了字节内部常用工具，帮助大家高效完成各类繁琐重复的任务，包括但不限于：写代码、分析数据、做调研、写文档等。

> 详细介绍：[Aime — 开启字节同学的异步办公新体验](https://bytedance.larkoffice.com/wiki/XxvZwyuyUiTlDEkrEHacSMJKnFe)
> 

## 联系方式
<table header-row="true" col-widths="200,100">
    <tr>
        <td></td>
        <td>PM</td>
    </tr>
    <tr>
        <td>A2A</td>
        <td>@(zhujingyan.43@bytedance.com)</td>
    </tr>
</table>

# CodeReview
## 使用流程
<table header-row="true" col-widths="52,392,376">
    <tr>
        <td colspan="3">对单次 MR 使用 Aime 做 CodeReview</td>
    </tr>
    <tr>
        <td>1</td>
        <td>邀请 Aime 作为评审人
> 添加后 Aime 就会开始进行 CodeReview
> 
> Aime 任务使用的是添加 Aime 的用户的权限。
> 
> CodeReview 会消耗用户的 Aime 次数。
> </td>
        <td>![图片](img_HhyHbp2xGoUvNlxNa50ceIM3nbf.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>在检查中可以看到一个 Aime CodeReview，然后在详情中可以看到对应的 Aime 任务链接。
> 新的 MR Version 不会创建新的任务。
> </td>
        <td>![图片](img_I5TTbM4l8ovNOZxbBAIc4SCVnWb.png)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>点击 Re-run 之后会创建一个新的 CodeReview</td>
        <td>![图片](img_WhvDbTGYEoHwwgxhfXYcgJX2nRf.png)</td>
    </tr>
    <tr>
        <td>4</td>
        <td>CodeReview 运行完毕之后会将结果添加到代码中</td>
        <td>![图片](img_PRMwbFeqhopY3wxucO7c5Omvnsf.png)</td>
    </tr>
    <tr>
        <td colspan="3">**每次 MR 都使用 Aime 做CodeReview**</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1. 选择设置 - Code AI features
2. 选择 Aime 作为默认的评审人</td>
        <td>![图片](img_VcRbbGY74oXPghxzVNzcSPK6nQe.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>后续会默认将 Aime 添加为评审人。</td>
        <td>![图片](img_HZchbckNQojYCixn45CcftnbnHf.png)</td>
    </tr>
    <tr>
        <td colspan="3">**自定义 CodeReview 规则**</td>
    </tr>
    <tr>
        <td>1</td>
        <td>在业务仓库的 [AGENTS.md](http://AGENTS.md) 里面增加业务规则的说明，或者直接引库内/外部的文档链接。
> [Aime 项目记忆（AGENTS.md）使用指南](https://bytedance.larkoffice.com/docx/VetbdMSMpoXMRMxiQuDcie7inth)
> 
> 注意: 自动发起的任务，由于不依赖用户登陆 Aime，因此可能存在 Lark Token 过期的问题，所以如果有 Lark 文档可能读不到，建议都保存在仓库里面
> </td>
        <td></td>
    </tr>
</table>

# DevMind
## 历史案例
<table header-row="true" col-widths="200,244,376">
    <tr>
        <td>部门</td>
        <td>回放链接</td>
        <td>用户之声</td>
    </tr>
    <tr>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
</table>

## 使用流程
<table header-row="true" col-widths="52,392,376">
    <tr>
        <td colspan="3">使用Aime分析DevMind的洞察报告</td>
    </tr>
    <tr>
        <td>1</td>
        <td>打开DevMind任一自己有权限的“洞察报告”</td>
        <td>![图片](img_Pqm4blFDlo53u2xK8uycL06enhh.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>通过右上角“数据洞察助手”打开数据分析任务抽屉</td>
        <td>![图片](img_R9EubwfIdoabMFxjywecAiDrnKh.png)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>透过抽屉入口或通过特定指标卡片入口发起数据洞察任务</td>
        <td>![图片](img_MJH9bFfPVosehCx5TzPc6FtxnKd.png)</td>
    </tr>
    <tr>
        <td>4</td>
        <td>下发任务过程可以精准指定1-N个待分析指标，可以复用历史任务和收藏任务</td>
        <td>![图片](img_XJJpb7fY5okhMqx8lJtch5bYnvg.png)</td>
    </tr>
    <tr>
        <td>5</td>
        <td>查看Aime分析返回的洞察结论</td>
        <td>![图片](img_D3PubdNDboqPgkx4hMFcqkvpnTg.png)</td>
    </tr>
    <tr>
        <td colspan="3">**使用Aime在DevMind创建可视化图表**</td>
    </tr>
    <tr>
        <td>1</td>
        <td>打开DevMind-可视化分析页面，在输入框用自然语言输入可视化图表创建需求</td>
        <td>![图片](img_FeFXbK8wWooz0RxpbTMcKYX9nTf.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>- 通过模板跳转到Aime任务页面，在Aime返回结果中可获得DevMind可视化图表效果预览和链接
- 点击链接进入，查看由Aime产生的可视化图表</td>
        <td>![图片](img_OXWYbQHj4o0PGSxVhabczfy4naf.png)
![图片](img_AZSSbu3Evo6Oekxlvfic1Rzbncc.png)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>通过自然语言指令，向Aime下发需求并智能编辑图表</td>
        <td>![图片](img_GVwbbgIvAo8ruwxIDFScBhUEnth.png)</td>
    </tr>
</table>




</content>
