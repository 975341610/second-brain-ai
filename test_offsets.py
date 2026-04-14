
import ahocorasick
import pytest

def test_pyahocorasick_offsets():
    automaton = ahocorasick.Automaton()
    wrong = "的地确确"
    automaton.add_word(wrong, (wrong, "的确确实", "test"))
    automaton.make_automaton()
    
    text = "我的地确确有这回事"
    # Expected: "的地确确" starts at index 1, ends at index 4 (last char '确')
    
    matches = list(automaton.iter(text))
    print(f"\nMatches: {matches}")
    
    for end_index, (w, s, r) in matches:
        start_index = end_index - len(w) + 1
        print(f"Match: {w}, start: {start_index}, end: {end_index}")
        # In Python:
        # text[1] = '地', text[2] = '确', text[3] = '确', text[4] = '确'
        # Wait, "的地确确" is 4 chars.
        # text[1:5] == "的地确确"
        # end_index should be 4.
        # start_index should be 1.
        assert start_index == 1
        assert text[start_index:end_index+1] == w

if __name__ == "__main__":
    test_pyahocorasick_offsets()
