import sys
import os
from fastapi.testclient import TestClient

# 修正导入路径
root_dir = os.path.abspath(os.path.join(os.getcwd(), "nova_repo"))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from backend.main import app

client = TestClient(app)

print("--- All Registered Routes ---")
for route in app.routes:
    print(f"  {getattr(route, 'path', 'N/A')} ({getattr(route, 'name', 'N/A')})")

print("\n--- API Test: Stickers ---")
resp_stickers = client.get("/api/stickers/list")
print(f"URL: /api/stickers/list -> Status: {resp_stickers.status_code}")
print(f"Response: {resp_stickers.text}")

print("\n--- API Test: Music Library ---")
resp_music = client.get("/api/media/music-library")
print(f"URL: /api/media/music-library -> Status: {resp_music.status_code}")
print(f"Response: {resp_music.text}")
