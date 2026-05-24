# Day 1 — Problems

Solve in order. Each problem has a **timer target**. Start the clock when you start reading the problem. Stop when all examples pass. Note your actual time at the top of your `.py` file.

For every problem, before writing code, jot 2–3 **clarifying questions** as comments at the top of the file. Even if the spec is obvious — practice the reflex.

---

## Problem 1 — Two Sum (target: 5 min)

Given a list of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`. Assume exactly one solution exists. Cannot use the same element twice.

**Signature:**
```python
def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    ...
```

**Examples:**
- `two_sum([2, 7, 11, 15], 9)` → `(0, 1)` (because `nums[0] + nums[1] == 9`)
- `two_sum([3, 2, 4], 6)` → `(1, 2)`
- `two_sum([3, 3], 6)` → `(0, 1)`

**Hint (don't read unless stuck > 2 min):** Build a dict as you go — for each `x`, check if `target - x` is already in the dict. Store value → index.

---

## Problem 2 — Group Anagrams (target: 10 min)

Given a list of strings, group the anagrams together. An anagram is a rearrangement: `"eat"` and `"tea"` and `"ate"` are all anagrams. Return a list of groups (order within / between groups doesn't matter).

**Signature:**
```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    ...
```

**Examples:**
- `group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])`
  → `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`
- `group_anagrams([""])` → `[[""]]`
- `group_anagrams(["a"])` → `[["a"]]`

**The whole problem is: what's the dict key that groups anagrams together?** Two options. Pick one, then mention the other when you'd switch. (Hint: sorted string. Or, character count tuple — better for very long strings, since sort is O(L log L) vs counting is O(L).)

---

## Problem 3 — Contains Duplicate (target: 3 min)

Given a list of integers, return `True` if any value appears at least twice, else `False`.

**Signature:**
```python
def contains_duplicate(nums: list[int]) -> bool:
    ...
```

**Examples:**
- `contains_duplicate([1, 2, 3, 1])` → `True`
- `contains_duplicate([1, 2, 3, 4])` → `False`
- `contains_duplicate([])` → `False`

This should be a one-liner using a set. Aim for under 3 min. Then think: what's the one-liner version, and what's the early-exit version? Trade-off?

---

## Problem 4 — Valid Anagram (target: 5 min)

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`.

**Signature:**
```python
def is_anagram(s: str, t: str) -> bool:
    ...
```

**Examples:**
- `is_anagram("anagram", "nagaram")` → `True`
- `is_anagram("rat", "car")` → `False`
- `is_anagram("", "")` → `True`

Same "what's the right key" question as Group Anagrams, but reduced to a comparison instead of a grouping. Two approaches — sorted vs counted. Discuss which is faster when (out loud, to yourself).

---

## Self-test — User → Items (target: 5 min, **no lookups, no concept brief, no docs**)

Given a list of `(user_id, item_id)` tuples, return a dict mapping each `user_id` to the **set** of items they interacted with.

**Signature:**
```python
def user_items(events: list[tuple[str, str]]) -> dict[str, set[str]]:
    ...
```

**Example:**
- `user_items([("u1", "a"), ("u2", "b"), ("u1", "a"), ("u1", "c")])`
  → `{"u1": {"a", "c"}, "u2": {"b"}}`

This one is the "should be muscle memory by Day 7" baseline. If it takes more than 5 minutes today, that's fine — it's Day 1. Note the time. Re-do it without lookups on Day 2 and Day 7.

---

## After you finish

Fill in `reflection.md` with:
1. Actual time per problem.
2. The one idiom you fumbled most.
3. Which staff-level habit you forgot (clarify? brute-force first? test as you go?).
