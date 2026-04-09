with open('nova_repo/DEVELOPMENT_LOG.md', 'r') as f:
    content = f.read()

new_log = """# Development Log

## v0.09 - 动态表情包系统与快捷面板唤起 [2026-04-09]

### 表情包面板完全体
- **彻底脱离 BubbleMenu**：重构了表情包面板的挂载结构，将其从容易被 Tiptap 拦截销毁的 `BubbleMenu` 中抽离，采用 `fixed` 全局居中挂载与 `z-[99999]` 高层级，解决了点击笑脸按钮面板瞬间闪退的 Bug。
- **预装动态 GIF**：在 `data/emoticons/` 目录下预装了 3 个动态 GIF 测试表情，面板秒开即用，直接支持点击插入。
- **极客唤醒快捷键**：拦截编辑器键盘事件，实现打字时敲击 `/e + 回车`，瞬间删除 `/e` 并唤起表情面板。

"""

content = content.replace("# Development Log\n", new_log)

with open('nova_repo/DEVELOPMENT_LOG.md', 'w') as f:
    f.write(content)
