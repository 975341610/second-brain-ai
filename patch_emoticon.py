import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_use_effect = """  // 鐐瑰嚮澶栭儴鍏抽棴琛ㄦ儏闈㈡澘
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (emoticonPanelRef.current && !emoticonPanelRef.current.contains(event.target as Node)) {
        setIsEmoticonPanelOpen(false);
      }
    };

    if (isEmoticonPanelOpen) {
      document.addEventListener('mousedown', handleClickOutside);
    }
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [isEmoticonPanelOpen]);"""

new_use_effect = """  // 鐐瑰嚮澶栭儴鍏抽棴琛ㄦ儏闈㈡澘
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (emoticonPanelRef.current && !emoticonPanelRef.current.contains(event.target as Node)) {
        setIsEmoticonPanelOpen(false);
      }
    };

    let timer: any;
    if (isEmoticonPanelOpen) {
      // Use setTimeout to avoid catching the current mousedown event that might be bubbling up
      timer = setTimeout(() => {
        document.addEventListener('mousedown', handleClickOutside);
      }, 0);
    }
    return () => {
      clearTimeout(timer);
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [isEmoticonPanelOpen]);"""

if old_use_effect in content:
    content = content.replace(old_use_effect, new_use_effect)
    with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched successfully.")
else:
    print("Could not find the target code to patch.")

