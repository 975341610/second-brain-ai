import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        req = {
            "action": "ask",
            "prompt": "Hello",
            "context": ""
        }
        async with client.stream("POST", "http://127.0.0.1:8765/api/ai/inline", json=req) as response:
            print("Response:", response.status_code)
            async for chunk in response.aiter_text():
                print("CHUNK:", repr(chunk))

asyncio.run(main())
