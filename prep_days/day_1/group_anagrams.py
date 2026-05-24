"""
Group Anagrams — Day 1, Problem 2
Target time: 10 min
Actual time: ___

Clarifying questions (write 2–3 BEFORE coding):
- ?
- ?
- ?
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    # your code here
    ...


if __name__ == "__main__":
    def _normalize(groups):
        # order-independent comparison
        return sorted(sorted(g) for g in groups)

    assert _normalize(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == _normalize(
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    )
    assert _normalize(group_anagrams([""])) == [[""]]
    assert _normalize(group_anagrams(["a"])) == [["a"]]
    print("ok")
