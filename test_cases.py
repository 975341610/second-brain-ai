
import sys
import os
sys.path.insert(0, '/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo')
from backend.services.spellcheck_engine import SpellcheckEngine

def test_engine_directly():
    e = SpellcheckEngine()
    e.build()
    
    # Test cases
    cases = [
        "地确有这回事", # 应匹配 "地确" -> "的确"
        "他跑的很快",    # 应匹配 "的" -> "得" (template)
        "的地确确",      # 规则库有吗？有 ("的地确确", "的确确实", "常见别字")
    ]
    
    for c in cases:
        res = e.check(c)
        print(f"Text: {c}, Result: {res}")

if __name__ == "__main__":
    test_engine_directly()
