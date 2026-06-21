# `bisect` — from first principles

## The problem it solves

You have a **sorted list**. You want to find where a target value would "fit" — the position where you'd insert it to keep the list sorted.

```python
arr = [1, 3, 5, 7, 9]
# Where does 4 go? Between 3 and 5 — at index 2.
```

Why care? Because that insertion point is also the **boundary** between "everything less than target" and "everything ≥ target." For a sorted list of timestamps and a target of `now - 3600`, the insertion point is the index of the first event in the last hour. Slice from there → window.

## Why not just scan?

Linear scan is O(n). For 1M events, that's 1M comparisons. Binary search on a sorted list halves the search space each step — ~20 comparisons for 1M events. **O(log n) vs O(n).**

## The binary search intuition

You know the list is sorted, so when you check the middle element, you can rule out half the list in one comparison. Repeat on the surviving half. Twenty halvings on a million-element list and you're down to one.

You don't implement this yourself — `bisect` ships it.

## The two functions

```python
import bisect
arr = [1, 3, 5, 5, 5, 7, 9]

bisect.bisect_left(arr, 5)   # → 2  (leftmost position where 5 could go)
bisect.bisect_right(arr, 5)  # → 5  (rightmost position where 5 could go)
bisect.bisect_left(arr, 4)   # → 2  (no 4 — goes between 3 and 5)
bisect.bisect_left(arr, 6)   # → 5  (goes between 5 and 7)
```

Two functions exist because when the target already lives in the array, there are **two valid insertion points** — just before the duplicates or just after.

- `bisect_left` → left edge of equal values
- `bisect_right` → right edge of equal values

**Default to `bisect_left` for time-window queries** — it gives you "first event with timestamp ≥ cutoff," which is the inclusive lower bound you want.

## The interview-critical pattern

### Lower-bound only (e.g., "last hour")

```python
import bisect

timestamps = [10, 20, 35, 47, 58, 62, 75]  # sorted ascending
now, window = 70, 60                        # last 60 seconds

cutoff = now - window
start_idx = bisect.bisect_left(timestamps, cutoff)  # first idx where ts >= cutoff
events_in_window = timestamps[start_idx:]           # everything from there on
```

### Bounded window (e.g., "between t_start and t_end inclusive")

```python
start_idx = bisect.bisect_left(timestamps, t_start)
end_idx   = bisect.bisect_right(timestamps, t_end)
window    = timestamps[start_idx:end_idx]
count     = end_idx - start_idx  # no slicing needed if you just want count
```

That last line is the move — **skip allocating the slice and just subtract indices**. O(log n) total, zero extra memory.

## Edge cases to watch

| Edge | What `bisect_left` returns |
|---|---|
| Target less than every element | `0` |
| Target greater than every element | `len(arr)` |
| Empty array | `0` |
| Target exactly matches an element | leftmost index of that element |

All of these "just work" with the `end_idx - start_idx` count pattern — no special-casing needed. Trust the indices.

## Bonus: `bisect.insort`

If you need to keep a list sorted while inserting new items one at a time:

```python
bisect.insort(arr, new_value)  # finds the right spot AND inserts in O(n)
```

Note: the *find* is O(log n), but the *insert* is O(n) because Python lists shift elements. For out-of-order ingest at scale, you'd reach for something else (heap, segment tree, time-bucketed buffer). Mention this as a trade-off if it comes up.

## Connection to the Tubi prompt

Top-K-items-in-last-hour:

1. Store events sorted by timestamp.
2. `bisect.bisect_left(timestamps, now - 3600)` → `start_idx`.
3. Slice `events[start_idx:]` → events in the window.
4. `Counter(items_in_window).most_common(k)` → top-K.

That's the whole top-K-last-hour query. Sub-millisecond on a million events.
