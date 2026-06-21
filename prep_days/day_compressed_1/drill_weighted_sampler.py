"""
Drill: weighted random sampling with prefix sums + bisect.

Target: 15 min
Actual: ___

Implement weighted_sample(items, weights):
    Returns a single item sampled with probability proportional to its weight.

Algorithm:
1. Build cumulative-sum (prefix-sum) array of weights.
2. Draw r = uniform(0, total_weight).
3. Use bisect to find which item's bucket r falls into.
4. Return that item.

This is O(n) to build prefix sums (once) and O(log n) per sample.

For this drill, build prefix sums inside the function for simplicity.
For repeated sampling in production, you'd build them once outside.

Edge cases:
- All weights zero → raise ValueError (no valid sample).
- Negative weight → raise ValueError.
- Mismatched lengths → raise ValueError.
"""

import bisect
import random
from collections import Counter


def weighted_sample(items, weights):
    # Your code here.
    pass


if __name__ == "__main__":
    # Edge: single item — always returned
    assert weighted_sample(["a"], [1.0]) == "a"
    assert weighted_sample(["only"], [42]) == "only"

    # Empirical: heavy-weighted item should dominate
    random.seed(42)
    items = ["a", "b", "c"]
    weights = [1, 1, 98]  # c should win ~98% of the time
    counts = Counter(weighted_sample(items, weights) for _ in range(10_000))
    assert counts["c"] > 9500, f"expected c dominance (~9800), got {counts}"

    # Empirical: balanced
    counts = Counter(weighted_sample(["x", "y"], [1, 1]) for _ in range(10_000))
    assert 4500 < counts["x"] < 5500, f"expected balance, got {counts}"

    # Empirical: 3-way roughly proportional
    counts = Counter(weighted_sample(["p", "q", "r"], [1, 2, 7]) for _ in range(10_000))
    # p: ~10%, q: ~20%, r: ~70%
    assert 800 < counts["p"] < 1300, f"got {counts}"
    assert 1700 < counts["q"] < 2300, f"got {counts}"
    assert 6500 < counts["r"] < 7500, f"got {counts}"

    # Error cases
    try:
        weighted_sample(["a"], [0])
        assert False, "expected ValueError for all-zero weights"
    except ValueError:
        pass

    try:
        weighted_sample(["a", "b"], [1])
        assert False, "expected ValueError for length mismatch"
    except ValueError:
        pass

    try:
        weighted_sample(["a", "b"], [1, -1])
        assert False, "expected ValueError for negative weight"
    except ValueError:
        pass

    print("all tests passed")
