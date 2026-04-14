import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure to declare the ref inside the component
if "const timerRef = useRef<NodeJS.Timeout>();" in content:
    ref_code = """
  const timerRef = useRef<NodeJS.Timeout>();
  
  // Ref to track mouse interaction for click vs drag detection
  const dragInteractionRef = useRef<{ startX: number; startY: number; startTime: number } | null>(null);
"""
    content = content.replace("  const timerRef = useRef<NodeJS.Timeout>();", ref_code)
else:
    # If not found, inject it right after the component declaration
    component_decl = "export const NovaBlockEditor: React.FC<NovaBlockEditorProps> = ({"
    if component_decl in content:
        # Find the end of props destructuring
        idx = content.find("}) => {")
        if idx != -1:
            injection_point = idx + len("}) => {")
            ref_code = """
  // Ref to track mouse interaction for click vs drag detection
  const dragInteractionRef = useRef<{ startX: number; startY: number; startTime: number } | null>(null);
"""
            content = content[:injection_point] + ref_code + content[injection_point:]

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Editor patched successfully!")
