"""
Top K Frequent Elements — Day 2, Problem 1
Target time: 7 min
Actual time: ___

Clarifying questions (write 2–3 BEFORE coding):
- ?
- ?
- ?
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # your code here
    ...


if __name__ == "__main__":
    # Order within result doesn't matter — normalize with sorted()
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6], 2)) == [4, 5]
    assert sorted(top_k_frequent([1, 2, 3, 4, 5], 5)) == [1, 2, 3, 4, 5]
    print("ok")
