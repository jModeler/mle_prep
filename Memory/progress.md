---
name: progress
description: Running per-day status of the 25-day Tubi prep plan — what's done, where the rough spots were, what to drill next. Update at the end of each day's session.
type: project
---

Per-day progress log. Update at end of each session.

## Day 1 — done 2026-05-25 (one day after the plan's calendar date; this is fine)

**Problems completed (all asserts passing):**
- Two Sum: target 5 min, actual ~16 min. Brute force shipped after a hash-map attempt failed. Then drilled the canonical hash-map version 5× consecutively in `prep_days/day_1/practice/two_sum_practice.py` — clean.
- Group Anagrams: target 10 min, actual 15 min. Solution uses `"".join(sorted(word))` as the key. Hit the "lists/sets aren't hashable as dict keys" rule for the first time.
- Contains Duplicate: target 3 min, actual 2 min — first time under budget.
- Valid Anagram: shipped `set(s) == set(t)` first, which passes the file's asserts but is **incorrect** (`is_anagram("aab", "abb")` returns True). Fixed to `sorted(s) == sorted(t)` and added the counter-test to the assert block. **This is the most important lesson of Day 1.**

**Self-test (`self_test_user_items.py`):** completed. First attempt had `result[user] = {}` (empty dict literal) where `set()` was needed — `.add` failed at runtime. Fixed on second pass.

## Drill priorities going into Day 2

1. **`Counter` and `defaultdict`** are the explicit Day 2 topic and were already wanted on Day 1 (Group Anagrams `defaultdict(list)` cleanup, Valid Anagram `Counter(s) == Counter(t)`). Should land cleanly.
2. **Pre-`return` counter-test habit.** Before saying "done," invent one input the function *should* fail on if you got it slightly wrong. For multiset problems specifically: "did I confuse set-equality with multiset-equality?" If Day 1 had drilled this habit, the Valid Anagram bug would have been caught self-served.
3. **Hashability rule is now solid** — burned in via Group Anagrams. The conversion patterns (`tuple(list)`, `frozenset(set)`, `"".join(sorted_str)`) are mapped.

## What's secure and what's not, going into Day 2

| Pattern | Status |
|---|---|
| Hash-map `seen = {}; for ...; complement in seen` | ✅ muscle memory (5 reps) |
| Set-as-O(1)-membership for dedup | ✅ |
| `"".join(sorted(s))` as anagram key | ✅ |
| Hashability rule (mutable = unhashable) | ✅ |
| `defaultdict(list)` / `defaultdict(set)` to skip the `if key not in d` branch | ⚠️ used but not reflexive |
| `Counter(seq) == Counter(seq2)` for multiset equality | ⚠️ knew of it, didn't reach for it |
| Counter-test habit before declaring done | ❌ failed once today, drill on Day 2 |

## Anchors to the larger plan

- Event-store theme (the most Tubi-flavored coding bucket per the prep PDF) lands explicitly on **Day 15**, with primitives built across Days 4 (`bisect`, marked ⭐), 5 (`heapq`), and 6 (deque sliding window). Today's hash-map work is the *outer* layer of an event store; Day 4 is the inflection point.
- See [[project-tubi-interview]] for the static interview context (date, themes, breadth/depth round).
