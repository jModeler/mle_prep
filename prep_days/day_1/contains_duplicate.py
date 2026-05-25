"""
Contains Duplicate — Day 1, Problem 3
Target time: 3 min
Actual time: 2 min

Clarifying questions (write 2–3 BEFORE coding):
- ?
- ?
- ?
"""


def contains_duplicate(nums: list[int]) -> bool:
    return (len(nums) != len(set(nums)))


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
    assert contains_duplicate([1, 1, 1, 1]) is True
    print("ok")
