import asyncio
import os
import sys

# Ensure PYTHONPATH
sys.path.append("/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo")

from backend.services.local_ai import local_ai_manager

async def verify():
    print("[*] Initializing Local AI Manager...")
    await local_ai_manager.initialize_model()
    status = local_ai_manager.get_status()
    print(f"[*] Status: {status}")
    
    if status["is_ready"]:
        print("[*] Testing generation...")
        async for chunk in local_ai_manager.generate_chat_stream([{"role": "user", "content": "hello"}]):
            print(chunk, end="", flush=True)
        print("\n[*] Generation finished.")
    else:
        print("[!] Manager is not ready!")

if __name__ == "__main__":
    asyncio.run(verify())
