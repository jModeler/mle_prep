"""
Two Sum — Day 1, Problem 1
Target time: 5 min
Actual time: 16 min

Clarifying questions (write 2–3 BEFORE coding):
- Assuming only one pair of values will give me the sum
- Assuming I will find said pair that gives me the sum
- ?
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    result = []
    nums_copy = nums.copy()
    for ii, num in enumerate(nums):
        difference = target-num
        candidate_indexes = [jj for jj, val in enumerate(nums) if val == difference and jj != ii]
        if len(candidate_indexes) != 0:
            result = [ii, candidate_indexes[0]]
            return tuple(result)
    # if there is no possibility for finding the sum, return the empty tuple
    return tuple(result)


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)
    print("ok")
