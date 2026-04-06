<title>如何用 Aime 写飞书文档 One-Pager</title>
<url>https://bytedance.larkoffice.com/wiki/Q1R7wd3T2iBp8kkJVqKcXgRlntW</url>
<content>
<!-- BLOCK_1 | doxcni8eQyfStlrAffZprSIDi5f -->
最近更新：2026-02-07
<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | Op9ad2u2doN25ixJ6WRcGlB4nfg -->
<callout icon="green_book" bgc="4" bc="4">
**Aime** 将为你和你的团队带来**<font color="green">报告写作体验。</font>**
</callout>
<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | NG7Mdi9vloy4nwxYXAzcBaWnn9c -->
> 官网地址：**https://aime.bytedance.net/**
> 
<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | Kr6pdm06zoDpHrxsDNdcCSS4nbc -->
# 什么类型的文档 Aime 更擅长<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | PfymdCGMlofvpixSdGkcvr2nnvb -->
<table header-row="true" col-widths="179,641">
    <tr>
        <td>文档创作场景</td>
        <td>Aime的独特优势解释</td>
    </tr>
    <tr>
        <td>**企业内部数据报告**</td>
        <td>深度集成字节内部数据平台（如风神、Meego、DevMind），可直接读取仪表盘数据、下载图表截图，实现数据自动导入，无需手动处理。</td>
    </tr>
    <tr>
        <td>**周期性业务报告**</td>
        <td>内置飞书模板系统，支持【正文】【表格】【图表】等占位符，保证报告格式始终规范统一。其他 Agent 多依赖自然语言描述，输出格式易变，难以标准化</td>
    </tr>
    <tr>
        <td>**代码仓库分析文档**</td>
        <td>和 Bits 平台深度集成，可自动生成代码合入报告及技术设计文档，适合技术团队的代码分析需求。
[Aime X Bits One-Pager](https://bytedance.larkoffice.com/wiki/TIL7wIhVjiqt3MkPbrIcMDw4nig)</td>
    </tr>
    <tr>
        <td>**多任务并行处理**</td>
        <td>支持异步任务和定时任务，可自动生成并推送报告至飞书群组，充分利用工作碎片时间。</td>
    </tr>
    <tr>
        <td>**复杂数据可视化**</td>
        <td>支持多模态图表（如 PlantUML 时序图、类图、交互式 HTML 图表），并可集成飞书画板，满足多样化可视化需求。其他 Agent 通常仅能生成静态图片</td>
    </tr>
    <tr>
        <td>**企业知识库检索与标准化输出**</td>
        <td>可检索企业内部文档、术语表、指标口径，确保内容专业且准确。飞书评论系统还能注入数据源和写作规范，实现精细化格式和逻辑控制</td>
    </tr>
</table>
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | QUsAdxAm6oMqwux0lS5cI9uSnkh -->
# 提升文档初稿稳定性<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | Ky00dQ8o0oVjb2xCjYYc2BTjnbf -->
## 使用场景<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | Hc7idezdPobSVExw277cwEn8nVh -->
在日常工作中，日报周报月报是非常常见的需求。
<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | WaIddqER4oqrvUxHvbGchtUTnYa -->
然而，仅依靠自然语言描述，往往难以细致表达报告生成的具体细节，也容易导致模型自由发挥，生成的结果也不太可控。
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | ISOTd23yOoPYh3xh9LAc4bR5nPf -->
为此，我们专门设计了一套报告模板写作规范，**<font color="red">面向有固定格式和内容要求</font>**的飞书文档生成任务。
<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | EUawd5He2oLDiTxhiuvcPP13nZf -->
按照这套规范编写模板，Aime 生成的报告内容能够更加稳定、规范。
<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | SFgOdnIbSo1Hm4x0LBicHqTWnjg -->
## 使用流程<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | doxcn4VNNqduq30O7M2NhpHApnc -->
<table col-widths="52,746">
    <tr>
        <td colspan="2">进入 飞书</td>
    </tr>
    <tr>
        <td>1</td>
        <td>创建一个新的飞书文档，并搭建好报告的基本框架。将需要AI自动生成内容的部分用【】或高亮块标记出来。</td>
    </tr>
    <tr>
        <td>2</td>
        <td>在文档的全文评论区内：
1. 【3.1 添加数据源】
2. 【3.2 添加整个报告的写作规范】</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1. 【3.3 添加占位符】
2. 【3.4 通过评论添加逻辑】</td>
    </tr>
    <tr>
        <td colspan="2">打开 Aime </td>
    </tr>
    <tr>
        <td>4</td>
        <td>将飞书模板的链接粘贴到输入框内，并附上简要的任务说明，发起任务即可。</td>
    </tr>
</table>
<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | UEDXdmdiNoHRypxHzdHcdFFHnnh -->
## 报告模板怎么写<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | NcVHd7UzmoxNPNxSiFQcyhMKnMh -->
### 添加数据源<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | doxcnu4BycNNUrJBQv0cKhPFYwd -->
<table col-widths="92,352,376,100">
    <tr>
        <td></td>
        <td>风神</td>
        <td>Meego</td>
        <td>Devmind</td>
    </tr>
    <tr>
        <td>数据输入</td>
        <td>- 仪表盘链接（sheet维度，如果要读取多个sheet的数据，需要提供多个链接）
- 可视化查询链接</td>
        <td>- Meego视图链接
- Meego度量看板链接
- Meego需求链接
- 基于日期和空间筛选的需求/缺陷列表</td>
        <td>- 洞察报告</td>
    </tr>
    <tr>
        <td>数据输出</td>
        <td>对于仪表盘中每个图表，能够实现如下输出：
- 基于图表下载的原始数据
- 图表的截图</td>
        <td>- Meego视图里的所有工作项
- Meego度量页面的所有图表的原始数据
- Meego空间的需求列表
暂不支持：
- 排期、甘特图等数据
- 视图中快捷筛选的数据</td>
        <td>- 洞察报告中图表对应的数据，和所选维度的下钻数据
- 洞察报告中的表格数据</td>
    </tr>
    <tr>
        <td>模版全文评论注入</td>
        <td>@aime - 数据源：
- 风神链接：https://data.bytedance.net/aeolus/pages/dashboard/882434?appId=1002611&sheetId=1667980
- 数据的时间范围：从24年Q2到25年Q2，以季度为单位</td>
        <td>@aime - 数据源：
- Meego视图：{{meego视图链接}}
- Meego度量看板：{{度量看板链接}} 需要用浏览器打开
- Meego空间Tiktok中，2025年Q1的所有需求/缺陷</td>
        <td>@aime - 数据源：
- Devmind报告：https://bits.bytedance.net/data/biz/report/7506170295528310821?fr=msg&q=%28%27nodeA7080880437744896007DgranularityCwDcycleCstandardDrange%21%5B%27B2%2000%3A00%3A00DB8%2023%3A59%3A59%27%5D%2AA%27%2AFilter%21%5B%5D.A%27.TypeC%27.NameCDreportA7514617121276430377%27%29%2A~~domainMeasureObj.~~**metricAIdCB2025-06-0C%21%27D%27~%01DCBA.%2A**</td>
    </tr>
    <tr>
        <td>Query注入</td>
        <td>```bash
读取风神面板：风神链接：https://data.bytedance.net/aeolus/pages/dashboard/882434?appId=1002611&sheetId=1667980的数据  
根据这个飞书模板：`https://bytedance.larkoffice.com/docx/WDhDdDOroo3hMbxdloycRqfjn5f`，遵守格式和要求，生成对应的度量报告  
  
注意：  
- 文档中引用的其他文档，也需要读取并分析  
- 模版文档中所有风神截图，必须用风神网站下载的截图，禁止自己画图  
- 最终生成的文档格式必须严格遵守模版文档
```</td>
        <td>```bash
基于飞书模板：https://bytedance.larkoffice.com/docx/Far5dIO52oN0hHxsNkjcotNcnjb  
分析下面「meego数据」链接里的需求信息，不使用浏览器方式，通过meego工具查询和计算，整理出一篇效能报告（含数据图表和归因分析），并在我个人的飞书文档空间生成最终的报告文档。  
- 「megoo数据」：https://meego.larkoffice.com/flowco/storyView/QscL2jJHR?viewMode=table  
- 「下钻归因逻辑表」：https://bytedance.larkoffice.com/sheets/R8K0stx0zhlTu6tAjW9cbtqxnZe
```</td>
        <td>```bash
# 目标  
使用Devmind工具解读指定报告的数据，生成一份周报，时间范围为{{2025.06.02}}到{{2025.06.06}}。  
周报的格式和内容参考该飞书模板：https://bytedance.larkoffice.com/docx/Qs6vdxyOyo1Di3xzkkGcZz3Tnbg，严格按照模版的格式和要求来生成  
# 补充信息  
devmind报告链接：https://bits.bytedance.net/data/biz/report/7506170295528310821?fr=msg&q=%28%27nodeA7080880437744896007DgranularityCwDcycleCstandardDrange%21%5B%27B2%2000%3A00%3A00DB8%2023%3A59%3A59%27%5D%2AA%27%2AFilter%21%5B%5D.A%27.TypeC%27.NameCDreportA7514617121276430377%27%29%2A~domainMeasureObj.~_metricAIdCB2025-06-0C%21%27D%27~%01DCBA.%2A_  
# 注意  
1. 飞书文档不要使用浏览器打开  
2. 最终生成的文档格式必须严格遵守模版文档
```</td>
    </tr>
    <tr>
        <td>如何准备一个好的数据源</td>
        <td>- 尽量保证需要的数据集中在1-2个sheet中，太多的sheet会导致任务耗时增加
- 仪表盘上的维度名称，和模版文档中保持一致
	- Good Case：风神中和文档中均为“二级业务线”、“三级业务线”
	- Bad Case：风神中“二级业务线”、“三级业务线”，文档中叫“团队”、“方向”
- 仪表盘中图表名清晰，且无重名：重名或不清晰的名称会导致生成的报告质量下降
- 如果有过滤器，需要在仪表盘中提供所需过滤选项对应的所有图表</td>
        <td>- 视图中的需求数量适中：太多的需求会导致任务耗时增加
- 需求中的字段含义清晰
- 如果需要对需求的某些字段进行计算
	- 能够提供公式，且无需关联其他工作项：在文档中写明计算公式，由Aime计算
	- 需要业务知识，或需要关联其他工作项的复杂计算：使用Meego的计算字段直接给出</td>
        <td>- 在洞察报告中，提供需要分析的所有数据和下钻维度：如下图中，如果需要计算其他维度，需要在图表的维度中添加其他维度</td>
    </tr>
</table>
<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | BlSrdseIaoGe9bx4dtschHCnnJQ -->
### 添加整个报告的写作规范<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | Hnvwd9YXqo6NDYxTF8mcL5sonAe -->
<table header-row="true" col-widths="140,680">
    <tr>
        <td>场景</td>
        <td>全文评论</td>
    </tr>
    <tr>
        <td>突出一些信息</td>
        <td>@aime - 按以下规则处理数据：
- 关键指标（如百分比、小时数等）需用 **粗体** 突出。</td>
    </tr>
    <tr>
        <td>限制数字格式</td>
        <td>@aime - 按以下规则处理数据：
- 所有非整数的数字，展示时默认保留小数点后两位；若为0.00，则继续展示到第一个有效数字。</td>
    </tr>
    <tr>
        <td>图表需要可交互</td>
        <td>@aime - 按以下规则进行数据可视化：
- 所有图表生成，必须使用 html 可交互的方式</td>
    </tr>
</table>
<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | HD7nd8Geio1UeAxPg0Qcsa5gnqb -->
### 添加占位符<!-- END_BLOCK_19 -->

<!-- BLOCK_20 | DsPJdusp8onIRjxyH3ncdILjnAc -->
> 这里仅仅展示了最常用的占位符，用户也可以自定义占位符。
> 
<!-- END_BLOCK_20 -->

<!-- BLOCK_21 | OIaodGQnlovmkIxjauZcDVmJnlg -->
<table header-row="true" col-widths="140,680">
    <tr>
        <td>占位符</td>
        <td>通常的场景</td>
    </tr>
    <tr>
        <td>【正文】</td>
        <td>项目背景、业务需求、方案说明、数据分析结论、经验总结等详细描述性内容</td>
    </tr>
    <tr>
        <td>【列表】</td>
        <td>工作任务清单、项目进度、功能点梳理、优化建议、操作步骤、用户需求等条目式内容</td>
    </tr>
    <tr>
        <td>【图例】/【图表】</td>
        <td>产品截图、流程图、趋势图、分布图、饼图、柱状图、组织架构图等可视化展示</td>
    </tr>
    <tr>
        <td>【表格】</td>
        <td>数据对比、指标汇总、进度跟踪、人员分工、预算明细、计划排期等结构化数据</td>
    </tr>
    <tr>
        <td>【引用】</td>
        <td>政策条款、行业标准、权威观点、外部链接、参考文献、历史记录等引用性内容</td>
    </tr>
    <tr>
        <td>【代码】</td>
        <td>编程代码、脚本命令、SQL语句、接口示例、配置文件、自动化脚本等技术实现内容</td>
    </tr>
    <tr>
        <td>【公式】</td>
        <td>计算公式、指标算法、财务模型、逻辑表达式、数学推导等公式类内容</td>
    </tr>
    <tr>
        <td>【交互式图表】</td>
        <td>可交互趋势图、仪表盘、地图、数据看板等实时数据监控和可视化分析</td>
    </tr>
</table>
<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | IpoHdMojHoLqIGxpHLWc6fvEn5g -->
### 评论占位符，添加逻辑<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | MQdqdAWYco8YbXxHgHGc7dSTnQd -->
<table header-row="true" col-widths="140,680">
    <tr>
        <td>占位符</td>
        <td>示例评论</td>
    </tr>
    <tr>
        <td rowspan="2">【正文】</td>
        <td>@aime 主要分析结论从各小节的趋势分析、下钻分析和关联分析里提炼导致指标波动的最主要的因素。</td>
    </tr>
    <tr>
        <td>@aime 分析逻辑严格遵循下面的文档：UT分析参考：⭐️UT指标分析策略-PnSP 工作量分析参考：⭐️产品+技术+算法+数仓需求总工作量指标分析策略 -PnSP。每个指标按趋势分析、下钻分析、关联分析顺序给出。</td>
    </tr>
    <tr>
        <td>【列表】</td>
        <td>@aime 分析下面的表格，根据`数据所在表`列中的表名称，获取数据填表，最终结果中删除这一列。只填写25Q2列的数据，其他列的数据必须和原表保持一致，禁止擅自修改，最终以表格的形式嵌入文档。</td>
    </tr>
    <tr>
        <td rowspan="2">【图例】/【图表】</td>
        <td>@aime 图表展示方法：“首次提交定容需求数”和“实际需求定容数”用纵向柱状图展示，用主坐标抽。柱状图显示顺序是：“实际需求定容数”、“首次提交定容需求数”；“需求总定容率”用折线图展示，格式用百分比，保留一位小数，用次坐标抽，范围是50%-130%。</td>
    </tr>
    <tr>
        <td>@aime 绘制指标“研发流程平均变更前置时间”的趋势图。</td>
    </tr>
    <tr>
        <td rowspan="2">【表格】</td>
        <td>@aime 最终报告中的表格必须和原表保持一致。只填写25Q2列的数据，其他列的数据必须和原表保持一致，禁止擅自修改，最终以表格的形式嵌入文档。</td>
    </tr>
    <tr>
        <td>@aime 每个图表的计算都基于最原始的数据开始计算：每个图表的数据排除计算方法只在当前图表中生效，计算下一个图表的数据时重新按完整数据开始计算。</td>
    </tr>
    <tr>
        <td>【引用】</td>
        <td>@aime 分析devmind里面存在的指标，给出解释和理由。</td>
    </tr>
    <tr>
        <td>【代码】</td>
        <td>@aime 如有自动化脚本或SQL查询，请在此处补充，并简要说明用途。</td>
    </tr>
    <tr>
        <td>【公式】</td>
        <td>@aime 需求总定容率是一个百分比，等于“实际需求定容数”/“首次提交定容需求数”的比例。</td>
    </tr>
    <tr>
        <td>【交互式图表】</td>
        <td>@aime 绘制指标“研发流程平均变更前置时间”的趋势图。</td>
    </tr>
    <tr>
        <td>颜色</td>
        <td>@aime xxx部分如果大于阈值需要展示成<font color="red">红色</font></td>
    </tr>
</table>
<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | R63SdiqT9omXpfxw4E5chsFZnwb -->
## 最佳实践<!-- END_BLOCK_24 -->

<!-- BLOCK_25 | AHHfdkqynoBDksxqBU1c1kl5nte -->
<table header-row="true" col-widths="140,145,100,100,335">
    <tr>
        <td>数据源</td>
        <td>文档模版</td>
        <td>案例</td>
        <td>生成文档</td>
        <td>案例要点</td>
    </tr>
    <tr>
        <td>风神</td>
        <td>最终模版：[XX业务度量管理报告模板 脱敏版](https://bytedance.larkoffice.com/docx/PKjidaWigoZ6XVxOa5ycvdf4nQh)
初始模版：</td>
        <td>![图片](img_Ru9Ubc7j4ohA0AxOzuOcRsoEnCe.png)</td>
        <td>[XX业务度量管理报告-25Q2 脱敏版](https://bytedance.larkoffice.com/docx/UghfdjM4GoN2y9xa24RcMmthnmg?source_type=message&from=message)</td>
        <td>- 不同业务报告中，共有的分析逻辑，可以使用文档引用的方式，减少模版编写成本
![图片](img_BmkQbOWADoBHd8xJfuVcWKQrnZg.png)</td>
    </tr>
    <tr>
        <td>Devmind</td>
        <td>[Bits流水线周报模版（ForAime）](https://bytedance.larkoffice.com/docx/Qs6vdxyOyo1Di3xzkkGcZz3Tnbg)</td>
        <td></td>
        <td></td>
        <td>- Devmind指标的维度下钻
![图片](img_MkLubWAheo40goxvQVOcTCL9nSh.png)
- 基于分析结果，生成动态Html图表
![图片](img_WFxibOPIyoBYwCx07xycjhmln3S.png)</td>
    </tr>
    <tr>
        <td>DevMind </td>
        <td>[【生活服务】Aime x 团队交付能力分析实践](https://bytedance.larkoffice.com/wiki/TOl5wI3yjiJzH7k9F7ZclBl2noh?from=from_copylink)</td>
        <td></td>
        <td></td>
        <td>生活服务团队运用Aime结合DevMind平台对团队交付能力进行深入分析。通过Aime的智能分析，团队能够全面评估开发团队的交付效率、质量水平和资源利用情况。</td>
    </tr>
    <tr>
        <td>Meego</td>
        <td>[豆包研发效能月报模版（1）](https://bytedance.larkoffice.com/docx/JsLedKp26oPoLfx5VjAcknagnRf)</td>
        <td></td>
        <td></td>
        <td>- 支持</td>
    </tr>
    <tr>
        <td>国内业务</td>
        <td>[【国内业务】Aime × 度量归因分析探索](https://bytedance.larkoffice.com/wiki/TtebwlHp7iPwlRku4JscxZYEnFb?from=from_copylink)</td>
        <td></td>
        <td></td>
        <td>国内业务团队利用Aime进行度量归因分析的深度探索，Aime帮助团队从海量的业务数据中识别影响效能的关键因素，并建立因果关系模型。</td>
    </tr>
</table>
<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | MhhCdoAUGoSENKxXVffcTIFynWe -->
# 对文档初稿局部修改【新功能🔥】<!-- END_BLOCK_26 -->

<!-- BLOCK_27 | DvlWdZFmcoeyShxg7bGcyTSonXQ -->
## 使用场景<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | RolUda9SeoOTOlxpkFhcT25Fnih -->
针对 Aime 生成的文档还需要二次修改的情况，用户可以直接在 Aime 上编辑；也可以划词评论，让 Aime 按照反馈更新文档。所有更新都会自动保存历史版本，方便用户随时查看和回溯。
<!-- END_BLOCK_28 -->

<!-- BLOCK_29 | IXvXdOL2RoRSo3xj37IcpWvdnag -->
## 效果演示和说明<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | KzrndSCtBoELkCxUjw3cJfsRnUd -->
### 评论的使用方式<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | XA9tdsoeRo46d6xJ9ZrcyjDinpc -->
<table header-row="true" col-widths="129,541,150">
    <tr>
        <td>步骤</td>
        <td>解释</td>
        <td>图</td>
    </tr>
    <tr>
        <td>划词评论</td>
        <td>你可以对最新一轮的产品编辑，通过划词，然后添加评论的方式去要求 Aime 干一些事情，通过这种方式添加的评论会被默认选择上</td>
        <td>![图片](img_IIcQb9FzpoYbWWxmpAtcDKm9nye.png)</td>
    </tr>
    <tr>
        <td>手动选择评论</td>
        <td>Aime 创建完文档的初稿以后，可以将这个初稿分享给其他人，让其他人评论，当其他人评论好之后，你可以打开 Aime，手动选择这些评论。</td>
        <td>![图片](img_K6H6bQwFRozCTHxkVbhccgdVndf.png)</td>
    </tr>
    <tr>
        <td>查看历史记录</td>
        <td>文档生成完成或者修改完成之后可以点击右上角的历史记录，查看Aime和你都分别修改了哪些内容。</td>
        <td>![图片](img_Qph5blHqnomIoExpDRAcOe77nrg.png)</td>
    </tr>
</table>
<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | BCmddi6PXoCeaAxA6vYccy1Gnyg -->
### 一些使用场景<!-- END_BLOCK_32 -->

<!-- BLOCK_33 | RQ9ndIbdKo89L0xlJtics74AnFf -->
<table header-row="true" col-widths="129,541,150">
    <tr>
        <td>使用场景</td>
        <td>解释</td>
        <td>图</td>
    </tr>
    <tr>
        <td>图片修复</td>
        <td>Aime 在生成飞书文档的时候会生成一些图片，这些图片有可能出现各类异常，通过 评论进行修复。</td>
        <td>![图片](img_F8dpbk230oo2Jfxbht9cyh5knTN.png)</td>
    </tr>
    <tr>
        <td>数据修复</td>
        <td>Aime 在生成飞书文档的时候会出现数据异常的情况，你可以新增一些提示，例如添加一些共识或者是提供新的数据源，借助评论进行修复。</td>
        <td>![图片](img_GaCzb0OKUoEYUoxRYpqcr39GnNH.png)</td>
    </tr>
    <tr>
        <td>精简语言</td>
        <td>Aime 有些时候会特别的发散，当你希望 Aime对于某一部分能够简洁一点的时候，可以评论一下。</td>
        <td>![图片](img_VVEqb95DVob8SFxeAAPcvUX6nWq.png)</td>
    </tr>
    <tr>
        <td>深入分析</td>
        <td>Aime 有些时候分析的也会比较浅，这个时候你可以通过评论，让 Aime 能够更加深入的分析。</td>
        <td>![图片](img_H5Zeb5K5loCMZwxKf1rcmlrHnCg.png)</td>
    </tr>
    <tr>
        <td>解释逻辑</td>
        <td>当你不知道 Aime 是怎么得出某些结论的时候，你可以通过评论，让 Aime 能够解释他的逻辑。</td>
        <td>![图片](img_CQX0bGGeRoXhxvxI8IKc0v4TnJK.png)</td>
    </tr>
</table>
<!-- END_BLOCK_33 -->

<!-- BLOCK_34 | X1tFdXPvvoliYFxKtTxcxirInMd -->
## 效果回放<!-- END_BLOCK_34 -->

<!-- BLOCK_35 | Z81odzZwJo2VDgxUK7ncnB0Rn0b -->
<table header-row="true" col-widths="164,656">
    <tr>
        <td>场景</td>
        <td>回放链接</td>
    </tr>
    <tr>
        <td>数据是怎么算出来的</td>
        <td>https://aime.bytedance.net/share/295fdec9-c61f-4b2f-a717-da5a0c282e48</td>
    </tr>
    <tr>
        <td>错误内容进行修正</td>
        <td>https://aime.bytedance.net/share/131b5406-c7a8-4a9f-8129-1bbdfa0228c4</td>
    </tr>
    <tr>
        <td>生成图表和画布</td>
        <td>https://aime.bytedance.net/share/ebbad75d-b0a2-41b9-95df-5b2d39507780</td>
    </tr>
    <tr>
        <td>调研扩写</td>
        <td>https://aime.bytedance.net/share/c5f105b0-391a-4e81-8a19-db6d98bd061f</td>
    </tr>
</table>
<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | LLjwdev1Zowlf0xkIh7cPZrinIf -->
# 其他经验<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | InEMdF8lsoTpTRxo2Rpcn87InHf -->
[编写Aime度量报告模板最佳实践](https://bytedance.larkoffice.com/wiki/IHfrw1PVHiViowkgP9Ncj43bnXc)
<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | P5jKdjeZcoYNxCxzc1pcsM9wncf -->
[如何和aime一起调试数据分析/飞书模板](https://bytedance.larkoffice.com/docx/TcvYdooZboyWorxPkXOcSm9mn4f)
<!-- END_BLOCK_38 -->


</content>
