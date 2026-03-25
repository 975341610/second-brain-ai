import { describe, it, expect, beforeEach } from 'vitest';
import { Editor } from '@tiptap/react';
import { Table } from '@tiptap/extension-table';
import { TableRow } from '@tiptap/extension-table-row';
import { TableCell } from '@tiptap/extension-table-cell';
import { TableHeader } from '@tiptap/extension-table-header';
import StarterKit from '@tiptap/starter-kit';
import { moveTableRow } from './tableCommands';

describe('moveTableRow transaction logic', () => {
  let editor: Editor;

  beforeEach(() => {
    editor = new Editor({
      extensions: [
        StarterKit,
        Table.configure({ resizable: true }),
        TableRow,
        TableHeader,
        TableCell,
      ],
      content: `
        <table>
          <tr><th>Header 1</th><th>Header 2</th></tr>
          <tr><td>Row 1</td><td>Data 1</td></tr>
          <tr><td>Row 2</td><td>Data 2</td></tr>
          <tr><td>Row 3</td><td>Data 3</td></tr>
        </table>
      `,
    });
  });

  it('should move Row 1 (index 1) to after Row 2 (index 2)', () => {
    // Current rows: [Header(0), Row1(1), Row2(2), Row3(3)]
    // Target: [Header(0), Row2(1), Row1(2), Row3(3)]
    
    // Set selection inside table
    editor.commands.focus(10); // inside Row 1

    let result = false;
    editor.commands.command(({ tr, state }) => {
      result = moveTableRow(tr, state, 1, 2);
      return result;
    });

    expect(result).toBe(true);
    const html = editor.getHTML();
    
    // Verify Row 2 is now before Row 1
    // Simplified regex check for row order
    const row1Idx = html.indexOf('Row 1');
    const row2Idx = html.indexOf('Row 2');
    expect(row2Idx).toBeLessThan(row1Idx);
  });

  it('should move Row 3 (index 3) to after Header (index 0)', () => {
    editor.commands.focus(10);
    
    editor.commands.command(({ tr, state }) => {
      return moveTableRow(tr, state, 3, 1);
    });

    const html = editor.getHTML();
    const row3Idx = html.indexOf('Row 3');
    const headerIdx = html.indexOf('Header 1');
    const row1Idx = html.indexOf('Row 1');
    
    expect(headerIdx).toBeLessThan(row3Idx);
    expect(row3Idx).toBeLessThan(row1Idx);
  });
});
