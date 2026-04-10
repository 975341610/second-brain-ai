import re
def extract_manual_links(content: str) -> list[int]:
    if not content: return []
    pattern = r'data-id="(\d+)"'
    ids = re.findall(pattern, content)
    return list(set(int(id_str) for id_str in ids))

content = '<span data-type="note-link" data-id="8" data-label="Note A">📝 Note A</span>'
print(extract_manual_links(content))
