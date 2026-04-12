import asyncio
import sys
import os
import json
from pathlib import Path

# 环境准备
current_dir = Path(__file__).parent
nova_repo_path = current_dir / "nova_repo"
sys.path.append(str(nova_repo_path))
sys.path.append(str(nova_repo_path / "backend"))

async def test_scenarios():
    try:
        from services.local_ai import local_ai_manager
    except ImportError:
        sys.path.append(str(current_dir))
        from nova_repo.backend.services.local_ai import local_ai_manager
    
    print("[*] 正在初始化模型...")
    await local_ai_manager.initialize_model()
    status = local_ai_manager.get_status()
    print(f"[*] 模型状态: {status}")
    
    if not status["is_ready"]:
        print("[!] 模型未就绪，退出测试")
        return

    scenarios = [
        {"name": "修改标题", "prompt": "【把标题改成会议记录】", "expected": 'type="set_title"'},
        {"name": "插入代码", "prompt": "【写一个 Python 冒泡排序代码块】", "expected": 'type="insert_code_block"'},
    ]

    for scene in scenarios:
        print(f"\n" + "="*30)
        print(f"[*] 测试场景: {scene['name']}")
        
        full_response = ""
        count = 0
        try:
            async for chunk in local_ai_manager.generate_chat_stream(scene['prompt']):
                count += 1
                # 打印前几个 chunk 看看格式
                if count < 5:
                    print(f"DEBUG Chunk {count}: {repr(chunk)}")
                
                if chunk.startswith("data: "):
                    raw = chunk[6:].strip()
                    if raw == "[DONE]": continue
                    try:
                        data = json.loads(raw)
                        text = data.get("text", "")
                        full_response += text
                    except:
                        pass
        except Exception as e:
            print(f"[!] 发生异常: {e}")

        print(f"[*] AI 汇总响应: {full_response}")
        if scene['expected'] in full_response:
            print("[+] 验证成功")
        else:
            print("[-] 验证失败")

if __name__ == "__main__":
    asyncio.run(test_scenarios())
