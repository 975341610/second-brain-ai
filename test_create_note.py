import requests

r1 = requests.post('http://127.0.0.1:8765/api/notes', json={"title": "Note 8", "content": '<span data-type="note-link" data-id="123">link</span>'})
print(r1.status_code, r1.text)
