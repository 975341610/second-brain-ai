import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to inject the cleanup effect somewhere around line 1312 (after previous state/effect declarations)

injection = """
  // Global drop cursor ghost cleanup (running during drag)
  useEffect(() => {
    let cleanupTimer: any = null;
    const cleanupGhosts = () => {
      if (cleanupTimer) return;
      cleanupTimer = requestAnimationFrame(() => {
        cleanupTimer = null;
        const cursors = document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor');
        if (cursors.length > 1) {
          // Keep the last one in the DOM, remove the rest
          for (let i = 0; i < cursors.length - 1; i++) {
            if (cursors[i].parentNode) {
              cursors[i].parentNode?.removeChild(cursors[i]);
            }
          }
        }
      });
    };

    window.addEventListener('dragover', cleanupGhosts);
    window.addEventListener('drag', cleanupGhosts);
    
    // Safety net on drag end as well
    const forceCleanAll = () => {
      setTimeout(() => {
        document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => el.remove());
      }, 50);
      setTimeout(() => {
        document.querySelectorAll('.nova-drop-cursor, .ProseMirror-dropcursor').forEach(el => el.remove());
      }, 300);
    };
    window.addEventListener('dragend', forceCleanAll);
    window.addEventListener('drop', forceCleanAll);

    return () => {
      window.removeEventListener('dragover', cleanupGhosts);
      window.removeEventListener('drag', cleanupGhosts);
      window.removeEventListener('dragend', forceCleanAll);
      window.removeEventListener('drop', forceCleanAll);
      if (cleanupTimer) cancelAnimationFrame(cleanupTimer);
    };
  }, []);
"""

# Find a good place to inject this. After "const latestNoteRef = useRef(note);"
target_line = "  const latestNoteRef = useRef(note);"
content = content.replace(target_line, target_line + "\n" + injection)

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Ghost cleanup patched!")
