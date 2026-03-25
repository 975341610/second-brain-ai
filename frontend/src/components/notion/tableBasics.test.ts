import { describe, it, expect, beforeEach } from 'vitest';
import { Editor } from '@tiptap/react';
import { Table } from '@tiptap/extension-table';
import { TableRow } from '@tiptap/extension-table-row';
import { TableCell } from '@tiptap/extension-table-cell';
import { TableHeader } from '@tiptap/extension-table-header';
import StarterKit from '@tiptap/starter-kit';

describe('Basic Table Operations', () => {
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
        </table>
      `,
    });
  });

  it('should add a row after current row', () => {
    // Selection in Row 1 (pos 10 is approx Row 1 Cell 1)
    editor.commands.focus(10); 
    editor.commands.addRowAfter();
    
    const html = editor.getHTML();
    const rows = html.match(/<tr/g) || [];
    expect(rows.length).toBe(3); // Header + Row 1 + New Row
  });

  it('should delete current row', () => {
    editor.commands.focus(10);
    editor.commands.deleteRow();
    
    const html = editor.getHTML();
    const rows = html.match(/<tr/g) || [];
    expect(rows.length).toBe(1); // Only Header left
  });

  it('should add a column after current column', () => {
    editor.commands.focus(10);
    editor.commands.addColumnAfter();
    
    const html = editor.getHTML();
    const headers = html.match(/<th/g) || [];
    const cells = html.match(/<td/g) || [];
    expect(headers.length).toBe(3); // 2 + 1
    expect(cells.length).toBe(3);   // 2 + 1
  });

  it('should delete current column', () => {
    editor.commands.focus(10);
    editor.commands.deleteColumn();
    
    const html = editor.getHTML();
    const headers = html.match(/<th/g) || [];
    const cells = html.match(/<td/g) || [];
    expect(headers.length).toBe(1);
    expect(cells.length).toBe(1);
  });
});
