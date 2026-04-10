import requests

try:
    r = requests.post('http://127.0.0.1:8765/api/notes', json={"title": "Note X", "content": "hello"})
    print("Status:", r.status_code)
    print("Response:", r.text)
except Exception as e:
    print(e)
