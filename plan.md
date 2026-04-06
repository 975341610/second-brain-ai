# 修复计划：草稿转正异常与子页面删除问题

## 问题 1：草稿转正导致旧笔记显示异常
**根本原因**：在 `useAppStore.ts` 的 `saveNote` 中，当草稿（负 ID）保存成功获取真实 ID 后，虽然更新了选中 ID，但没有更新 `notes` 数组中其他笔记（即该草稿的子笔记）的 `parent_id`。导致侧边栏递归渲染时找不到对应的父节点，子笔记在树中消失。

**修复方案**：
- 修改 `saveNote`，在 ID 替换逻辑中增加对 `notes` 数组的扫描，更新所有以旧草稿 ID 为父 ID 的笔记。

## 问题 2：笔记子页面无法删除
**根本原因**：
1. **草稿删除失败**：如果子页面是新建尚未保存的草稿（负 ID），前端 `deleteNote` 会向后端发送 `DELETE` 请求。由于数据库中不存在该 ID，后端返回 404，前端抛出错误，导致本地状态未更新，笔记依然显示。
2. **缺乏级联删除**：后端 `soft_delete_note` 仅处理当前节点，未处理其子节点，导致删除父笔记后，子笔记状态不一致。

**修复方案**：
- **前端**：在 `deleteNote` 和 `bulkDeleteNotes` 中增加 ID 判断。若为负数 ID，直接从本地状态移除，跳过网络请求。
- **后端**：在 `soft_delete_note` 中实现递归逻辑，软删除所有后代笔记。

## 实施步骤
1. 修改 `clean_repo/frontend/src/store/useAppStore.ts` 中的 `saveNote`, `deleteNote`, `bulkDeleteNotes`。
2. 修改 `clean_repo/backend/services/repositories.py` 中的 `soft_delete_note`。
3. 编写并运行测试用例验证修复效果。
4. 提交代码并 push 到分支。
