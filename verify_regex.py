import re

def test_regex():
    # 模拟包含多行代码的 AI 输出
    stream_buffer = '这里是一些废话 <Action type="insert_code_block" language="python">def fib(n):\n    if n <= 1: return n\n    return fib(n-1) + fib(n-2)</Action> 后面还有一些废话'
    
    action_regex = re.compile(r'<Action\s+type="([^"]+)"(?:\s+language="([^"]+)")?>([\s\S]*?)<\/Action>', re.MULTILINE)
    
    matches = list(action_regex.finditer(stream_buffer))
    print(f"Found {len(matches)} matches")
    for match in matches:
        print(f"Type: {match.group(1)}")
        print(f"Language: {match.group(2)}")
        print(f"Content:\n{match.group(3)}")

if __name__ == "__main__":
    test_regex()
