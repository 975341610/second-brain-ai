
在 AI 大模型（LLM）的开发者生态中，存在一套被称为“灰产三件套”或“中转全家桶”的成熟技术流程。这套流程的核心目标是**将低成本的账号资源（如网页端 Session、免费额度、订阅套餐）转化为高稳定性、可商业化分发的标准 OpenAI API**。

以下是“注册机 + sub2api”这套流程的深度调研总结。

---

### 一、 核心逻辑：从“号”到“接口”的工业化链路

这套流程可以抽象为四个关键阶段，每个阶段各司其职：

<grid cols="2">  
<column width="50">  
<callout icon="bulb" bgc="5">  
**1. 账号生产（注册机）**  
注册机是流量的源头，负责通过自动化脚本批量创建 OpenAI、Claude 等平台的账号。它需要解决：  
- **批量自动化**：模拟用户行为，自动填写邮箱、验证码。  
- **风控对抗**：绕过 Sentinel 安全检测、验证 Cloudflare Turnstile。  
- **资源获取**：集成接码平台（SMS）和自动验证码识别（Capsolver）。  
</callout>  
</column>  
<column width="50">  
<callout icon="bulb" bgc="12">  
**2. 协议转换（sub2api / CPA）**  
原始账号通常只能通过网页端或特定客户端使用。转换层的任务是：  
- **Session 转 API**：将 Access Token 或网页 Session 映射为标准 API。  
- **订阅聚合**：将 ChatGPT Plus 或 Claude Pro 的配额提取出来。  
- **格式统一**：确保输出的 JSON 结构完全兼容 OpenAI 标准格式。  
</callout>  
</column>  
</grid>

<grid cols="2">  
<column width="50">  
<callout icon="bulb" bgc="3">  
**3. 聚合调度（NewAPI / GPT-load）**  
当手握成百上千个转换后的 API 后，需要一个“大脑”来管理：  
- **渠道聚合**：将多个 sub2api 实例或自建渠道汇聚到一个入口。  
- **负载均衡**：通过智能轮询算法，分摊请求压力。  
- **死号剔除**：自动检测失效账号并从号池中移除。  
</callout>  
</column>  
<column width="50">  
<callout icon="bulb" bgc="11">  
**4. 业务分发（NewAPI / OneAPI）**  
最终面向终端用户的环节：  
- **计费系统**：支持 Token 计费、倍率设置、多倍率配置。  
- **令牌权限**：为不同客户生成独立的 API Key。  
- **审计监控**：实时查看调用日志和报错率。  
</callout>  
</column>  
</grid>

---

### 二、 核心组件与协同模式

在实际操作中，这些组件通常以“全家桶”形式组合：

#### 1. 核心工具详解

<table header-row="true">  
<tr>  
<td>组件名称</td>  
<td>主要功能</td>  
<td>典型角色</td>  
</tr>  
<tr>  
<td>**NewAPI / OneAPI**</td>  
<td>大模型 API 网关，负责用户管理、计费、渠道聚合和分发。</td>  
<td>**管理中枢**</td>  
</tr>  
<tr>  
<td>**Sub2api (CRS2)**</td>  
<td>支持 Claude Code、Codex、Gemini 等订阅接入，实现“订阅转 API”。</td>  
<td>**转换引擎**</td>  
</tr>  
<tr>  
<td>**CPA (OpenClaw)**</td>  
<td>账号池维护工具，专门管理 Codex/ChatGPT 账号的 Session 续期与检测。</td>  
<td>**号池维护**</td>  
</tr>  
<tr>  
<td>**GPT-load**</td>  
<td>高性能密钥池轮询代理，主打高并发下的智能调度和故障恢复。</td>  
<td>**调度专家**</td>  
</tr>  
</table>

#### 2. 协同工作流示例
1. **注册机**生产出 1000 个带额度的 OpenAI 账号。
2. **CPA/Sub2api** 接入这些账号，提取出对应的 API 访问点。
3. **GPT-load** 将这 1000 个访问点做成一个轮询池，提升并发上限。
4. **NewAPI** 对接 GPT-load，设置 0.1 倍的低费率，对外售卖“廉价 API”。

---

### 三、 业务流程图示

![preview](workflow.mermaid)

---

### 四、 这种流程的主要应用场景

<callout icon="star" bgc="5">  
**1. 廉价 API 中转站**  
通过批量注册免费号或低价地区订阅，将 API 价格压低至官方的 1/10 甚至更低，形成巨大的价格差收益。  
</callout>

<callout icon="star" bgc="5">  
**2. 大规模自动化抓取与分析**  
企业级爬虫或数据分析任务需要极高的并发配额，官方 API 的 Rate Limit 往往无法满足，通过万级号池可以轻松突破限制。  
</callout>

<callout icon="star" bgc="5">  
**3. 跨境服务接入**  
针对无法直接支付或访问官方服务的地区，提供稳定的代理接入层。  
</callout>

---

### 五、 核心风险与对抗点

虽然流程高度自动化，但依然面临严峻的风险挑战：

1.  **大规模封号风险**：官方（OpenAI/Anthropic）会通过注册 IP 段、关联邮箱域名、异常调用模式（如纯 API 调用而无网页端轨迹）进行封杀。
2.  **风控逻辑迭代**：例如 OpenAI 的 **Sentinel** 系统和 Cloudflare 的 **Turnstile** 会不断升级，要求注册机具备更强的指纹模拟能力。
3.  **服务不稳定性**：中转链路越长，延迟（Latency）越高，一旦上游转换层（如 sub2api）失效，下游业务会瞬间瘫痪。
4.  **资金安全**：部分灰产使用“黑卡”支付订阅，会导致账号在短时间内被批量封禁，造成预付金损失。

---

### 六、 总结

“注册机 + sub2api”流程本质上是**将零散、低质的 AI 资源进行工业化重组的过程**。通过 NewAPI 的网关能力和 Sub2api 的协议转换能力，灰产从业者构建起了一个低成本、高灵活性的影子 API 帝国。对于普通开发者而言，了解这一流程有助于识别市场上 API 服务的来源，并评估其稳定性与合规风险。
