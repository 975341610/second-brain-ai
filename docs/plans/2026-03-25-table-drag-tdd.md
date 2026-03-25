# Table Drag TDD (Vitest) Implementation Plan
> **For agent:** REQUIRED SUB-SKILL: Use Section 4 or Section 5 to implement this plan.
**Goal:** 在 `frontend` 建立 `npm run test`（Vitest + jsdom）并以 TDD 方式为表格拖拽与表格基础能力补齐单元/组件测试，同时修复拖拽逻辑与性能/卸载问题，确保全量测试通过。
**Architecture:** 测试以 Vitest + jsdom + Testing Library 为主；纯事务逻辑（moveRow）用 tiptap/prosemirror 事务在内存中构造文档并断言结构变化；基础表格功能（新增/删除行列）优先覆盖对应 helper/command 或最小组件交互。
**Tech Stack:** Vite + React + TypeScript + Vitest + jsdom + @testing-library/react

---

## Task 1: Git 分支准备
**Files:** 无

**Step 1:** 创建分支
```bash
cd second-brain-ai
git checkout -b fix/table-drag-tdd
```
**Expected:** `Switched to a new branch 'fix/table-drag-tdd'`

---

## Task 2: Vitest + jsdom 测试环境
**Files:**
- Modify: `frontend/package.json`
- Modify: `frontend/vite.config.ts`
- Create: `frontend/src/test/setup.ts`

**Step 1:** 增加脚本 `test`（非 watch）
**Step 2:** 配置 vitest environment=jsdom，启用 jest-dom
**Step 3:** 跑一次空测试（或 smoke）验证可执行

**Verify:**
```bash
cd second-brain-ai/frontend
npm run test
```

---

## Task 3: RED - moveRow 纯事务逻辑测试
**Files:**
- Create: `frontend/src/__tests__/table/moveRow.test.ts`
- (可能) Modify: `frontend/src/components/NotionEditor.tsx`（仅导出/抽取被测 helper）

**Step 1:** 写一个最小可复现：构造包含 table 的 ProseMirror 文档，调用 moveRow，将 row 从 index A 移动到 index B，断言 row 顺序变更。
**Step 2:** `npm run test` 观察失败（功能未满足/接口不匹配）。

---

## Task 4: RED - 表格基础能力（新增/删除行列）测试
**Files:**
- Create: `frontend/src/__tests__/table/tableBasics.test.tsx` 或 `.test.ts`

**Step 1:** 覆盖“新增行/删除行/新增列/删除列”至少各 1 个用例（优先调用现有 command/helper；若只有 UI 操作入口，则用 Testing Library 走最小交互）。
**Step 2:** `npm run test` 观察失败。

---

## Task 5: GREEN - 修复实现
**Files:**
- Modify: `frontend/src/components/NotionEditor.tsx`

**Step 1:** 修复 moveRow：当需要插入多段 Node 时，用 `Fragment.fromArray(nodes)` 而不是直接传 Node[]。
**Step 2:** 修复 hover 高频 re-render：将 hover 状态更新节流/去抖，或仅在 hover key 变化时 setState（避免 mousemove 导致频繁 render）。
**Step 3:** 修复 timeout 未清理：组件卸载时清理 timeout，并通过 ref 防止卸载后 setState。

**Verify:**
```bash
cd second-brain-ai/frontend
npm run test
```

---

## Task 6: 回归验证 + 汇报
**Step 1:** 全量 `npm run test` 通过。
**Step 2:** 汇总：测试用例列表、Vitest 输出（通过数/耗时）。
