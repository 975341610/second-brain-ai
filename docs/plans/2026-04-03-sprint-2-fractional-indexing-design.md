# Sprint 2 设计文档：基于 Fractional Indexing 的无限层级树排序

## 1. 背景与目标
在无限层级树结构中，传统的 `sort_order` (整数索引) 在频繁移动节点时会导致大量节点的索引重写（$O(N)$ 复杂度）。为了支持高效的拖拽重排和云端同步冲突解决，我们采用 **Fractional Indexing (分数字段排序)**，类似于 Jira 的 LexoRank。

## 2. 数据模型
节点结构定义：
```typescript
interface TreeNode {
  id: string;
  parentId: string | null;
  sortKey: string; // 使用 Base64 或 ASCII 字符串表示的分数
  title: string;
  children?: TreeNode[];
}
```

## 3. 核心算法：Fractional Indexing
### 3.1 排序键生成
- **Midpoint 计算**：给定两个字符串 `prev` 和 `next`，计算它们之间的“中值”字符串。
- **边界处理**：
  - 如果没有 `prev`，在 `next` 之前生成。
  - 如果没有 `next`，在 `prev` 之后生成。
  - 如果 `prev` 和 `next` 连续（如 "a" 和 "b"），则增加字符串长度（如 "an"）。

### 3.2 拖拽场景处理 (`moveNode`)
- **Drop-into (作为子节点)**：将 `parentId` 设为目标节点 ID，`sortKey` 生成为目标节点现有子节点末尾。
- **Drop-before (移至上方)**：`parentId` 同级，`sortKey` 为 `prev` 和当前位置节点的中间值。
- **Drop-after (移至下方)**：`parentId` 同级，`sortKey` 为当前位置节点和 `next` 的中间值。

## 4. 边界与健壮性
- **删除父节点**：逻辑上删除父节点时，其 `parentId` 指向该节点的子节点也将从树构建中剔除。
- **精度限制**：虽然字符串理论上无限长，但为了性能，当 `sortKey` 长度超过阈值（如 100 字符）时，触发重均衡（Rebalance）建议（本阶段暂不实现自动重均衡）。

## 5. 前端状态结合
- 树结构由扁平数组通过 `buildTree` 实时生成。
- 拖拽仅修改受影响节点的 `parentId` 和 `sortKey`，触发本地数据库更新。
