from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio
import os

app = FastAPI()

app.mount("/api/media/files", StaticFiles(directory="nova_repo/data/uploads"), name="test_mount")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
