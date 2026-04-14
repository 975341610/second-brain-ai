import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Instead of physically ripping nodes out of the DOM (which causes ProseMirror's plugin to crash when it tries to `removeChild` a node it thinks it owns), 
# we should just make the ghost nodes invisible using CSS `display: none` or `opacity: 0`.

old_ghost_cleanup = """        if (cursors.length > 1) {
          // Keep the last one in the DOM, remove the rest
          for (let i = 0; i < cursors.length - 1; i++) {
            if (cursors[i].parentNode) {
              cursors[i].parentNode?.removeChild(cursors[i]);
            }
          }
        }"""

new_ghost_cleanup = """        if (cursors.length > 1) {
          // Keep the last one visible, hide the rest without removing them from DOM
          // This prevents ProseMirror DropCursorView from crashing when it tries to removeChild on nodes we already deleted
          for (let i = 0; i < cursors.length - 1; i++) {
            (cursors[i] as HTMLElement).style.display = 'none';
            (cursors[i] as HTMLElement).style.opacity = '0';
          }
        }"""

content = content.replace(old_ghost_cleanup, new_ghost_cleanup)

# Also update the final forceCleanAll to just hide instead of remove
old_force_clean = """      setTimeout(() => {
        document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => el.remove());
      }, 50);
      setTimeout(() => {
        document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => el.remove());
      }, 300);"""

new_force_clean = """      setTimeout(() => {
        document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => {
          (el as HTMLElement).style.display = 'none';
        });
      }, 50);
      setTimeout(() => {
        document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => {
          (el as HTMLElement).style.display = 'none';
        });
      }, 300);"""

content = content.replace(old_force_clean, new_force_clean)

# Also need to update the top clearDropCursor useEffect 
old_top_clear = """          document.querySelectorAll('.ProseMirror-dropcursor').forEach(el => {
            if (el && el.parentNode) {
              el.parentNode.removeChild(el);
            }
          });"""

new_top_clear = """          document.querySelectorAll('.ProseMirror-dropcursor').forEach(el => {
            (el as HTMLElement).style.display = 'none';
          });"""

content = content.replace(old_top_clear, new_top_clear)

# And the events below in the JSX
old_jsx_dragend = """        onDragEnd={() => {
          document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => el.remove());
        }}"""

new_jsx_dragend = """        onDragEnd={() => {
          document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => {
            (el as HTMLElement).style.display = 'none';
          });
        }}"""
content = content.replace(old_jsx_dragend, new_jsx_dragend)


old_jsx_drop = """        onDrop={(e) => {
          document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => el.remove());
          
          if (!isStickerMode) return;"""

new_jsx_drop = """        onDrop={(e) => {
          document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => {
            (el as HTMLElement).style.display = 'none';
          });
          
          if (!isStickerMode) return;"""
content = content.replace(old_jsx_drop, new_jsx_drop)


old_element_drag_end = """                onElementDragEnd={() => {
                  setTimeout(() => {
                    document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => el.remove());
                  }, 50);
                }}"""

new_element_drag_end = """                onElementDragEnd={() => {
                  setTimeout(() => {
                    document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => {
                      (el as HTMLElement).style.display = 'none';
                    });
                  }, 50);
                }}"""

content = content.replace(old_element_drag_end, new_element_drag_end)

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("DropCursor safe patch applied!")
