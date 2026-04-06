"""
# `mcp:lark_workspace_batch_doc_summary`

通过提供的任务与文档URL列表，批量总结文档的内容，本工具仅会阅读document_url_list内的文档，执行过程中不具备执行其他工具的能力，不建议使用此AI工具直接输出结构化数据例如json或者执行参数化提取任务，本工具的特点是在大量文档中尽量不丢失上下文关联性的前提下，专注在文本内容总结与分析上
强烈建议在task中明确提出章节和内容需求，一个最佳实践如下，你可以直接使用：
'请阅读所有文件，重点提取属于张三（zhangsan.001）的工作内容，注意所谓属于是指明确有张三（zhangsan.001）在文档中出现的内容，同时，注意文档中的总结部分和综述部分，可能也包含了没有明确@提及张三（zhangsan.001）的内容，但是也包含了对应的数据、大盘、图表、计划、文案等内容的
目标：识别并梳理全年“周报/进展”序列为主干，保持时间连贯性，抽取核心方向、关键动作与结果。

请按照以下结构进行深度提炼和汇总：

1.  **全年总览 (Year at a Glance)**
    *   一句话总结今年的核心聚焦。
    *   列出3-5个最关键的年度成就/里程碑。

2.  **工作详情 (Quarterly Breakdown)**
	*   **核心项目进展**：具体做了什么，进度如何。
	*   **关键数据**：列出所有可量化的指标（如：准确率提升X%，QPS降低Y，覆盖Z个场景）。
	*   **交付物**：上线了什么功能，输出了什么文档。

3.  **专题分析 (Thematic Analysis)**
    *   **A项目**：总结从早期到后期的演进脉络。
    *   **B项目**：专门总结该专项的背景、动作和结果。
    *   **协作与支持**：列出跨团队（如：与QA、前端、算法等）的协作事项。

4.  **问题与复盘 (Challenges & Reflections)**
    *   遇到的主要技术难点或项目阻碍。
    *   采取的解决策略及沉淀的方法论。

**要求**：
- 识别并梳理所有文档内容中张三的工作内容为主干，保持时间连贯性，抽取核心方向、关键动作与结果。
- 在总结中保留来源链接（Markdown 格式），同时标注周报中由张三（zhangsan.001）直接或间接地提及的关联文档（例如标题含“方案/复盘/设计/总结/评审”等），用于后续 TOP10 选择。
- 不夸大角色：对于“参与”绝不写成“主导”，不归属无关文档，用户未直接或间接地提及的文档，不认为用户做了对应工作，也不认为文档与用户有关
- 输出中请附带每个文档的标题和链接以便制作 doc_list.md 与优先级列表
- 重要的指标、文档、图表、引用，都不要轻易忽略'


---

**Parameters Schema:**

{"type":"object","properties":{"document_url_list":{"type":"array","description":"required, lark document url list, example: https://bytedance.larkoffice.com/docx/xxx, https://bytedance.larkoffice.com/wiki/xxx, 不要只传入一个wiki目录，本工具不具备自动遍历子目录的能力，一次性最多分析20篇文档，超过请分批处理","properties":{},"items":{"type":"string","properties":{}}},"file_name":{"type":"string","description":"optional, 文件名(只接受markdown)，用于在生成的总结中标识文档来源，例如：summary_{task_brief}.md","properties":{}},"summary_task":{"type":"string","description":"required, 任务描述，详细描述任务内容（整个思维链和SOP），分析文档和变更记录与这个任务描述的相关性，没有字数和语法限制，例如：你是一个AI助手，你的任务是从文档中总结出我今年的工作内容，生成一份年度总结报告；注意如果你需要获取特定人员所属内容，需要在任务中明确指出用户ID和名字，例如'总结tangjing.fisher@bytedance.com今年的工作内容'","properties":{}},"user_id":{"type":"string","description":"optional, 需要被查询变更记录的用户ID，格式为：zhangsan.001，如果传入，则会搜索该用户的变更记录用作文档内容的补充","properties":{}}},"required":["user_id"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="lark_workspace", tool_name="mcp:lark_workspace_batch_doc_summary", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)