import requests
import json
try:
    r = requests.get('http://127.0.0.1:8765/api/emoticons/list')
    print("Status:", r.status_code)
    print("Data:", json.dumps(r.json(), indent=2))
except Exception as e:
    print(e)
