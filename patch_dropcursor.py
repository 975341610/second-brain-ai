import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the global drop cursor cleanup
cleanup_effect = """
  // Global drop cursor cleanup
  useEffect(() => {
    const clearDropCursor = () => {
      [0, 50, 100, 200].forEach(delay => {
        setTimeout(() => {
          document.querySelectorAll('.ProseMirror-dropcursor').forEach(el => {
            if (el && el.parentNode) {
              el.parentNode.removeChild(el);
            }
          });
        }, delay);
      });
    };

    window.addEventListener('dragend', clearDropCursor);
    window.addEventListener('drop', clearDropCursor);
    window.addEventListener('mouseup', clearDropCursor); // For safety

    return () => {
      window.removeEventListener('dragend', clearDropCursor);
      window.removeEventListener('drop', clearDropCursor);
      window.removeEventListener('mouseup', clearDropCursor);
    };
  }, []);

  useEffect(() => {
"""

content = content.replace("  useEffect(() => {", cleanup_effect, 1)

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("DropCursor cleanup patched!")
