import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/DEVELOPMENT_LOG.md', 'r', encoding='utf-8') as f:
    content = f.read()

new_log = """## [2026-04-14] - Nova 前端交互细节与体验修复 (拖拽手柄、黑线残留、拼写检查)

### 1. 拖拽手柄与 Block 菜单冲突彻底解决 (Notion 方案)
- **精准识别操作**: 在 `NovaBlockEditor.tsx` 中引入了 `dragInteractionRef` 跟踪鼠标按下状态。
- **阈值判定**: 通过计算移动距离（> 3px）和按压时长（> 200ms），准确区分“点击”和“拖拽”操作，彻底解决了拖拽时误触发挥出块级菜单的严重体验问题。

### 2. Drop Cursor (黑线) 残留清理
- **强制回收**: 在编辑器层级的 `onDragEnd`、`onDrop` 以及 Drag Handle 插件内部的 `onElementDragEnd` 事件中，增加对 DOM 中遗留 `.ProseMirror-dropcursor` 元素的深度清理，确保拖拽结束后界面不残留黑线。

### 3. AI 拼写检查体验闭环
- **底层 Transaction 拦截**: 在 `AISpellcheck.ts` 插件中实现了处理 `removeError` 动作的 Meta 事务逻辑。
- **状态同步更新**: 当用户在菜单中采纳修正建议后，能够彻底消除底层的 Decoration (红色波浪线) 和 `storage.errors` 中的记录，实现真正的“一键修复并净化”。

### 4. TypeScript 严谨编译修复
- **依赖清理与补充**: 移除了 `SpellcheckSuggestionCard.tsx` 中未使用的 `AnimatePresence` 导入。
- **无感构建**: 修复了新增 Ref 带来的上下文引用丢失问题，确保 `npm run build` 和 `npm run dev` 能够无缝且无报错地通过。

---

"""

content = content.replace("## [2026-04-14] - Nova 前端 UI 交互细节深度修复 (标题折叠、Slash 菜单与拖拽手柄)", new_log + "## [2026-04-14] - Nova 前端 UI 交互细节深度修复 (标题折叠、Slash 菜单与拖拽手柄)")

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/DEVELOPMENT_LOG.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("DEVELOPMENT_LOG.md updated successfully!")
