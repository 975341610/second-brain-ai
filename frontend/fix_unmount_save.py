import os

editor_path = os.path.join(os.path.dirname(__file__), 'src/components/notion/NotionEditor.tsx')
with open(editor_path, 'r', encoding='utf-8') as f:
    code = f.read()

old_execute_save = """    const executeSave = async (isSync = false) => {
      if (!isModified && !isSync) return;
      if (isUnmountedRef.current) return;
      
      const currentContent = editor.getHTML();"""

new_execute_save = """    const executeSave = async (isSync = false) => {
      if (!isModified && !isSync) return;
      
      // Allow saving even if unmounted, just skip React state updates
      const currentContent = editor.getHTML();"""

if old_execute_save in code:
    code = code.replace(old_execute_save, new_execute_save)
    with open(editor_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Fixed executeSave unmount bug")
else:
    print("Could not find old_execute_save")
