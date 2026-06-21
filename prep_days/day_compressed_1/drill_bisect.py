"""
Drill: bisect over a sorted timestamp list.

Target: 5 min
Actual: ___

Given a sorted list of timestamps and a window [t_start, t_end],
return the COUNT of events in the window (inclusive of both endpoints).
Use bisect — no linear scan.

Hint: count = right_index - left_index, no slicing needed.
"""

import bisect


def count_in_window(timestamps: list[int], t_start: int, t_end: int) -> int:
    # Your code here.
    pass


if __name__ == "__main__":
    # Test 1 — basic window
    ts = [1, 5, 7, 9, 12, 15, 20]
    assert count_in_window(ts, 7, 15) == 4, "expected 4 events in [7, 15]"

    # Test 2 — window covers everything
    assert count_in_window(ts, 0, 100) == 7

    # Test 3 — window covers nothing (before all events)
    assert count_in_window(ts, -10, 0) == 0

    # Test 4 — window covers nothing (after all events)
    assert count_in_window(ts, 25, 100) == 0

    # Test 5 — single-point window matches exact timestamp
    assert count_in_window(ts, 9, 9) == 1

    # Test 6 — single-point window misses
    assert count_in_window(ts, 10, 10) == 0

    # Test 7 — empty input
    assert count_in_window([], 0, 100) == 0

    print("all tests passed")
