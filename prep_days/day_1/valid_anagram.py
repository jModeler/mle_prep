"""
Valid Anagram — Day 1, Problem 4
Target time: 5 min
Actual time: 40 sec

Clarifying questions (write 2–3 BEFORE coding):
- Sanity check for inputs?
- ?
- ?
"""


def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    assert is_anagram("aab", "abb") is False
    print("ok")
