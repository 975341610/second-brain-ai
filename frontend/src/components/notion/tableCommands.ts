import type { EditorState, Transaction } from '@tiptap/pm/state';
import { Fragment, Node } from '@tiptap/pm/model';

// Pure transaction helper for table row drag/reorder.
// Implemented via ProseMirror transaction so it is unit-testable.
export function moveTableRow(
  tr: Transaction,
  state: EditorState,
  fromIndex: number,
  toIndex: number
): boolean {
  if (fromIndex === toIndex) return false;

  const { selection } = state;
  const { $from } = selection;
  
  // Find table node
  let tablePos = -1;
  let tableNode: Node | null = null;
  for (let i = $from.depth; i > 0; i--) {
    if ($from.node(i).type.name === 'table') {
      tablePos = $from.before(i);
      tableNode = $from.node(i);
      break;
    }
  }

  if (tablePos === -1 || !tableNode) return false;

  const rows: Node[] = [];
  tableNode.forEach((node) => rows.push(node));

  if (fromIndex < 0 || fromIndex >= rows.length || toIndex < 0 || toIndex >= rows.length) return false;

  const movedRow = rows[fromIndex];
  const newRows = [...rows];
  newRows.splice(fromIndex, 1);
  newRows.splice(toIndex, 0, movedRow);

  // Use Fragment.fromArray to correctly insert multiple nodes
  tr.replaceWith(tablePos + 1, tablePos + tableNode.nodeSize - 1, Fragment.fromArray(newRows));
  return true;
}
