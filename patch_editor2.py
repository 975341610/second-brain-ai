import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

injection_target = "  const dragHandleRepositionFrameRef = useRef<number | null>(null);"
injection_code = """  const dragHandleRepositionFrameRef = useRef<number | null>(null);
  const dragInteractionRef = useRef<{ startX: number; startY: number; startTime: number } | null>(null);"""

content = content.replace(injection_target, injection_code)

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Editor patched successfully!")
