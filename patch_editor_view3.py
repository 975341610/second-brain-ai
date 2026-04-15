with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """  useEffect(() => {
    if (!editor) {
      return;
    }

    const tr = editor.state.tr.setMeta('lockDragHandle', isBlockMenuOpen);
    editor.view.dispatch(tr);
  }, [editor, isBlockMenuOpen]);"""

new_code = """  useEffect(() => {
    if (!editor) {
      return;
    }

    try {
      if (editor.isDestroyed) return;
      const tr = editor.state.tr.setMeta('lockDragHandle', isBlockMenuOpen);
      editor.view.dispatch(tr);
    } catch (e) {
      // Ignore if view is not ready or unmounted
    }
  }, [editor, isBlockMenuOpen]);"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched 3 successfully!")
else:
    print("Could not find the target code to patch.")
