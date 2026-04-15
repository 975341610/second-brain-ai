import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """  useEffect(() => {
    if (!editor || typeof ResizeObserver === 'undefined') {
      return;
    }

    const scrollContainer = scrollContainerRef.current;
    const editorElement = editor.view.dom;

    if (!scrollContainer || !editorElement) {
      return;
    }"""

new_code = """  useEffect(() => {
    if (!editor || typeof ResizeObserver === 'undefined') {
      return;
    }

    const scrollContainer = scrollContainerRef.current;
    let editorElement: Element | null = null;
    try {
      // Accessing editor.view throws an error in Tiptap if the view is not mounted yet
      if (editor.isDestroyed) return;
      editorElement = editor.view.dom;
    } catch (e) {
      return;
    }

    if (!scrollContainer || !editorElement) {
      return;
    }"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched successfully!")
else:
    print("Could not find the target code to patch.")

