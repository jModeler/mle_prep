# Day 2 — Problems

Solve in order. Each problem has a **timer target**. Start the clock when you start reading the problem. Stop when all examples pass. Note your actual time at the top of your `.py` file.

For every problem, jot 2–3 **clarifying questions** as comments at the top of the file before writing code. Even when the spec is obvious — drill the reflex.

---

## Problem 1 — Top K Frequent Elements (target: 7 min)

Given a list of integers `nums` and an integer `k`, return the `k` most frequent elements. The answer may be returned in any order. Assume `k` is always valid (`1 ≤ k ≤ number of unique elements`).

**Signature:**
```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    ...
```

**Examples:**
- `top_k_frequent([1, 1, 1, 2, 2, 3], 2)` → `[1, 2]`
- `top_k_frequent([1], 1)` → `[1]`
- `top_k_frequent([4, 4, 4, 5, 5, 6], 2)` → `[4, 5]`

**Hint (don't read unless stuck > 2 min):** This is the canonical `Counter.most_common(k)` problem. Build a `Counter`, ask for the top-k. One-liner. The complexity discussion (O(n log k) vs O(n log n) vs O(n) with bucket sort) is what an interviewer cares about, not the code.

**Bonus to discuss out loud:** could you do it in **O(n)** worst case? (Yes — bucket sort by frequency. Useful to mention even if you don't code it.)

---

## Problem 2 — First Unique Character (target: 4 min)

Given a string `s`, return the index of the first character that doesn't repeat anywhere in `s`. Return `-1` if no such character exists.

**Signature:**
```python
def first_unique_char(s: str) -> int:
    ...
```

**Examples:**
- `first_unique_char("leetcode")` → `0` (`'l'` appears once)
- `first_unique_char("loveleetcode")` → `2` (`'v'` appears once; comes before other uniques)
- `first_unique_char("aabb")` → `-1` (no unique character)
- `first_unique_char("")` → `-1`

**Hint:** Two passes. First pass: count chars with `Counter`. Second pass: walk `s`, return the index of the first char whose count is 1.

**Trade-off to mention:** can you do it in **one pass**? (Yes — `OrderedDict` keyed by char, value is `(first_index, count)`. Then iterate the OrderedDict and return the first with `count == 1`. Same big-O but only one scan over `s`.) Counter version is shorter; OrderedDict version is the "I know `move_to_end` exists" signal.

---

## Problem 3 — Design HashMap (target: 15 min)

Implement a HashMap **without** using any built-in hash table libraries (i.e., no `dict`, no `set`, no `Counter`). Support:

- `put(key: int, value: int) -> None` — insert or update.
- `get(key: int) -> int` — return the value, or `-1` if the key doesn't exist.
- `remove(key: int) -> None` — delete the key if it exists; no-op otherwise.

**Constraints:**
- Keys and values are non-negative integers (so `-1` as a sentinel "not found" is safe).
- Use a list of buckets with **chaining** (each bucket is a list of `(key, value)` pairs).

**Signature:**
```python
class MyHashMap:
    def __init__(self):
        ...
    def put(self, key: int, value: int) -> None:
        ...
    def get(self, key: int) -> int:
        ...
    def remove(self, key: int) -> None:
        ...
```

**Example sequence:**
```python
m = MyHashMap()
m.put(1, 1)
m.put(2, 2)
m.get(1)        # → 1
m.get(3)        # → -1
m.put(2, 1)     # update existing
m.get(2)        # → 1
m.remove(2)
m.get(2)        # → -1
```

**Hint:** Allocate a fixed-size list of `N` buckets (e.g., `N = 1024` — pick a power of 2 or a prime, mention the trade-off). Index into buckets via `key % N`. Each bucket is a `list` of `(key, value)` tuples; walk it linearly for find/update/delete.

**What an interviewer probes:**
- Collision handling — you must say "chaining" or "open addressing" explicitly.
- Load factor — at what point would you resize? (Typically when ~70% full, double the bucket count and re-insert.)
- Why `key % N`? Mention you'd use `hash(key) % N` for non-integer keys.

This problem is the *only* one today that tests "do you understand what a dict is doing under the hood." Worth knowing cold for the Tubi event-store theme.

---

## Self-test — Top event types in a stream (target: 3 min, **no lookups, no concept brief, no docs**)

Given a list of event type strings (a stream), return the top-`k` most frequent event types in descending order of count.

**Signature:**
```python
def top_event_types(events: list[str], k: int = 3) -> list[str]:
    ...
```

**Examples:**
- `top_event_types(["a", "b", "a", "c", "a", "b", "c", "c", "c"], k=3)` → `["c", "a", "b"]`
- `top_event_types(["a", "b", "a", "c", "a", "b", "c", "c", "c"], k=2)` → `["c", "a"]`
- `top_event_types([], k=3)` → `[]`

If you have to look up `Counter.most_common`, you've failed the self-test for today — the **whole point** is that this is the one-line reflex. Note your time and revisit on Day 3 and Day 7.

---

## After you finish

Fill in `reflection.md` with:
1. Actual time per problem.
2. Which `collections` tool you fumbled (reached for `dict.get()` when `Counter` was right, etc.).
3. The one staff-level habit you'd grade yourself lowest on today.
4. One thing to drill on Day 3.
