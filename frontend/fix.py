import sys
import os

editor_path = os.path.join(os.path.dirname(__file__), 'src/components/notion/NotionEditor.tsx')
with open(editor_path, 'r', encoding='utf-8') as f:
    code = f.read()

old_save = """  useEffect(() => {
    if (!editor || !note) return;
    
    let timer: ReturnType<typeof setTimeout>;

    const handleSave = async (targetNoteId: number) => {
      if (isUnmountedRef.current) return;
      
      // [关键修复] 严格校验当前编辑器正在编辑的笔记 ID
      if (noteRef.current?.id !== targetNoteId) {
        return;
      }

      // 防止同一篇笔记的并发保存，允许不同笔记的串行处理
      if (isSavingRef.current === targetNoteId) {
        timer = setTimeout(() => handleSave(targetNoteId), 1000);
        return;
      }

      const currentContent = editor.getHTML();
      const currentText = editor.getText().trim();
      
      const lastNote = noteRef.current;
      if (!lastNote) return;

      let newTitle = lastNote.title || '未命名笔记';
      const isTitleEdited = lastNote.is_title_manually_edited || false;

      if (!isTitleEdited && currentText) {
        const firstLine = currentText.split('\\n')[0].trim();
        if (firstLine) newTitle = firstLine.slice(0, 100);
      }

      if (currentContent === lastNote.content && newTitle === lastNote.title) {
        return;
      }

      isSavingRef.current = targetNoteId;
      if (!isUnmountedRef.current && noteRef.current?.id === targetNoteId) setIsSaving(true);
      
      try {
        if (noteRef.current?.id !== targetNoteId || isUnmountedRef.current) {
          return;
        }

        await onSaveRef.current({ 
          id: targetNoteId, 
          content: currentContent, 
          title: newTitle, 
          icon: lastNote.icon, 
          is_title_manually_edited: isTitleEdited,
          silent: true 
        });

        if (!isUnmountedRef.current && noteRef.current?.id === targetNoteId) {
          setLastSavedAt(new Date().toLocaleTimeString());
        }
      } catch (error) {
        console.error("Auto-save failed", error);
      } finally {
        if (isSavingRef.current === targetNoteId) isSavingRef.current = null;
        if (!isUnmountedRef.current && noteRef.current?.id === targetNoteId) setIsSaving(false);
      }
    };

    const onUpdate = () => {
      const currentNoteId = noteRef.current?.id;
      if (typeof currentNoteId !== 'number') return;
      
      clearTimeout(timer);
      timer = setTimeout(() => handleSave(currentNoteId), 1500); // 停笔 1.5 秒即存
    };

    editor.on('update', onUpdate);

    return () => {
      clearTimeout(timer);
      editor.off('update', onUpdate);
    };
  }, [editor, note?.id]);"""

new_save = """  useEffect(() => {
    if (!editor || !note) return;
    
    let timer: ReturnType<typeof setTimeout>;
    let isModified = false;

    // Use closure variable 'note' which refers to the note of THIS render
    const currentSessionNoteId = note.id;

    const executeSave = async (isSync = false) => {
      if (!isModified && !isSync) return;
      if (isUnmountedRef.current) return;
      
      const currentContent = editor.getHTML();
      const currentText = editor.getText().trim();
      
      let newTitle = note.title || '未命名笔记';
      const isTitleEdited = note.is_title_manually_edited || false;

      if (!isTitleEdited && currentText) {
        const firstLine = currentText.split('\\n')[0].trim();
        if (firstLine) newTitle = firstLine.slice(0, 100);
      }

      if (currentContent === note.content && newTitle === note.title) {
        isModified = false;
        return;
      }

      isSavingRef.current = currentSessionNoteId;
      if (!isUnmountedRef.current && noteRef.current?.id === currentSessionNoteId) setIsSaving(true);
      
      try {
        await onSaveRef.current({ 
          id: currentSessionNoteId, 
          content: currentContent, 
          title: newTitle, 
          icon: note.icon, 
          is_title_manually_edited: isTitleEdited,
          silent: true 
        });

        isModified = false; 
        if (!isUnmountedRef.current && noteRef.current?.id === currentSessionNoteId) {
          setLastSavedAt(new Date().toLocaleTimeString());
        }
      } catch (error) {
        console.error("Auto-save failed", error);
      } finally {
        if (isSavingRef.current === currentSessionNoteId) isSavingRef.current = null;
        if (!isUnmountedRef.current && noteRef.current?.id === currentSessionNoteId) setIsSaving(false);
      }
    };

    const handleSave = async () => {
      if (isSavingRef.current === currentSessionNoteId) {
        timer = setTimeout(handleSave, 1000);
        return;
      }
      await executeSave();
    };

    const onUpdate = () => {
      isModified = true;
      clearTimeout(timer);
      timer = setTimeout(handleSave, 1500); 
    };

    editor.on('update', onUpdate);

    return () => {
      clearTimeout(timer);
      editor.off('update', onUpdate);
      
      // Cleanup happens BEFORE the next render's useEffect.
      // So editor content is still the old one. We MUST save it!
      if (isModified) {
        executeSave(true).catch(console.error);
      }
    };
  }, [editor, note?.id]);"""

if old_save in code:
    code = code.replace(old_save, new_save)
    with open(editor_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Fixed NotionEditor.tsx")
else:
    print("Could not find old_save in NotionEditor.tsx")
