"""
Group Anagrams — Day 1, Problem 2
Target time: 10 min
Actual time: 15 min

Clarifying questions (write 2–3 BEFORE coding):
- Should I check for valid input (all strings?)
- For repeated words, should we also include the repeats in the list?
- ?
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    seen = {}
    for word in words:
        word_key = "".join(sorted(word))
        if word_key in seen:
            seen[word_key].append(word)
        else:
            seen[word_key] = [word]
    return list(seen.values())

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
