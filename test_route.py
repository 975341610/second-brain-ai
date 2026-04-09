import asyncio
from httpx import AsyncClient

async def test():
    async with AsyncClient() as client:
        r = await client.get("http://localhost:8000/api/media/files/test.png")
        print(r.status_code)

asyncio.run(test())
