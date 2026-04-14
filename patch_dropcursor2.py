import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of '.ProseMirror-dropcursor' with '.nova-drop-cursor, .ProseMirror-dropcursor'
content = content.replace('.ProseMirror-dropcursor', '.nova-drop-cursor, .ProseMirror-dropcursor')

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("DropCursor class patched!")
