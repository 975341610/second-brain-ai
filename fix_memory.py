import os

with open('MEMORY.md', 'r', encoding='utf-8') as f:
    content = f.read()

rule_to_add = """
- **开发日志实时维护**: 必须在每次执行任务、发现 Bug、修改代码、推送 GitHub 后，实时更新根目录下的 `DEVELOPMENT_LOG.md`。任何需求和 Bug 必须先记录，**只有在老大明确确认解决后，才能在日志中标记为已完成/已解决**。日志需保持言简意赅，便于快速读取当前项目进度。
"""

if "开发日志实时维护" not in content:
    content = content.replace("# 工作流铁律 (Iron Rules)", "# 工作流铁律 (Iron Rules)" + rule_to_add)
    with open('MEMORY.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Memory updated.")
