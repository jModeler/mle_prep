"""
Drill: top-K event types in a time window.

Target: 10 min
Actual: ___

Given events as a sorted-by-timestamp list of (timestamp, item_id) tuples,
return the k most-common items in the inclusive window [t_start, t_end].

Use bisect to slice to the window (O(log n)), then Counter.most_common(k) for top-K.

Returned format: list of (item_id, count) tuples, sorted by count descending.
Tied counts can be in any order.

Hint: extract a parallel list of timestamps once at the top so bisect can work on it.
"""

import bisect
from collections import Counter


def top_k_in_window(events, t_start, t_end, k):
    # Your code here.
    pass


if __name__ == "__main__":
    events = [
        (1, "a"), (2, "b"), (3, "a"), (4, "c"),
        (5, "b"), (6, "a"), (7, "c"), (8, "b"),
        (9, "a"), (10, "d"),
    ]

    # Test 1 — full window, k=2
    result = top_k_in_window(events, 0, 100, 2)
    assert dict(result) == {"a": 4, "b": 3}, f"got {result}"

    # Test 2 — partial window [4, 8]: items c, b, a, c, b → b=2, c=2, a=1
    result = top_k_in_window(events, 4, 8, 3)
    rd = dict(result)
    assert rd.get("b") == 2 and rd.get("c") == 2 and rd.get("a") == 1, f"got {result}"

    # Test 3 — k larger than distinct items in window
    result = top_k_in_window(events, 0, 100, 100)
    assert len(result) == 4, f"expected 4 distinct items, got {result}"

    # Test 4 — window with no events
    assert top_k_in_window(events, 100, 200, 3) == []

    # Test 5 — k=0
    assert top_k_in_window(events, 0, 100, 0) == []

    # Test 6 — single event in window
    assert top_k_in_window(events, 10, 10, 5) == [("d", 1)]

    print("all tests passed")
