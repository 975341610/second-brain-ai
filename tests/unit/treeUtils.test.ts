import { describe, it, expect } from 'vitest';
import { buildTree, generateMidpoint, moveNode, TreeNode } from '../../frontend/src/lib/treeUtils';

describe('treeUtils - Fractional Indexing', () => {
  describe('generateMidpoint', () => {
    it('should generate a midpoint between two strings', () => {
      expect(generateMidpoint('a', 'c')).toBe('b');
      expect(generateMidpoint('a', 'b').startsWith('a')).toBe(true);
      expect(generateMidpoint('a', 'b').length).toBeGreaterThan(1);
    });

    it('should handle null boundaries', () => {
      // Start of list
      const first = generateMidpoint(null, 'm');
      expect(first < 'm').toBe(true);
      
      // End of list
      const last = generateMidpoint('m', null);
      expect(last > 'm').toBe(true);
      
      // Empty list
      const middle = generateMidpoint(null, null);
      expect(typeof middle).toBe('string');
      expect(middle.length).toBeGreaterThan(0);
    });
  });

  describe('buildTree', () => {
    it('should build a nested tree from a flat array sorted by sortKey', () => {
      const flatNodes: TreeNode[] = [
        { id: '1', parentId: null, sortKey: 'm', title: 'Root' },
        { id: '2', parentId: '1', sortKey: 'a', title: 'Child 1' },
        { id: '3', parentId: '1', sortKey: 'b', title: 'Child 2' },
      ];
      const tree = buildTree(flatNodes);
      expect(tree[0].id).toBe('1');
      expect(tree[0].children?.[0].id).toBe('2');
      expect(tree[0].children?.[1].id).toBe('3');
    });

    it('should filter out children whose parent is missing', () => {
      const flatNodes: TreeNode[] = [
        { id: '2', parentId: '1', sortKey: 'a', title: 'Orphan' },
      ];
      const tree = buildTree(flatNodes);
      expect(tree.length).toBe(0);
    });
  });

  describe('moveNode', () => {
    const mockNodes: TreeNode[] = [
      { id: '1', parentId: null, sortKey: 'm', title: 'Node 1' },
      { id: '2', parentId: null, sortKey: 'p', title: 'Node 2' },
      { id: '3', parentId: '1', sortKey: 'm', title: 'Child 1' },
    ];

    it('should handle drop-before', () => {
      // Move Node 2 before Node 1
      const result = moveNode(mockNodes, '2', '1', 'before');
      expect(result.parentId).toBe(null);
      expect(result.sortKey < 'm').toBe(true);
    });

    it('should handle drop-after', () => {
      // Move Node 1 after Node 2
      const result = moveNode(mockNodes, '1', '2', 'after');
      expect(result.parentId).toBe(null);
      expect(result.sortKey > 'p').toBe(true);
    });

    it('should handle drop-into', () => {
      // Move Node 2 into Node 1
      const result = moveNode(mockNodes, '2', '1', 'into');
      expect(result.parentId).toBe('1');
      // Should be after Child 1 ('m')
      expect(result.sortKey > 'm').toBe(true);
    });
  });
});
