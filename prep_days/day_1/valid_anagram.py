"""
Valid Anagram — Day 1, Problem 4
Target time: 5 min
Actual time: ___

Clarifying questions (write 2–3 BEFORE coding):
- ?
- ?
- ?
"""


def is_anagram(s: str, t: str) -> bool:
    # your code here
    ...


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    print("ok")
