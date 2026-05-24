# Day 1 — Concept brief (quick reference)

Lists, dicts, sets, tuples. One page. Glance, then solve.

---

## Complexity cheat sheet

| Operation                       | list             | dict       | set        | tuple   |
| ------------------------------- | ---------------- | ---------- | ---------- | ------- |
| Index access `x[i]`             | O(1)             | O(1) avg   | —          | O(1)    |
| Lookup membership `k in x`      | **O(n)**         | **O(1) avg** | **O(1) avg** | O(n)  |
| Insert at end / add             | O(1) amortized   | O(1) avg   | O(1) avg   | (immut) |
| Insert at front                 | O(n)             | —          | —          | (immut) |
| Delete by value                 | O(n)             | O(1) avg   | O(1) avg   | (immut) |
| Iterate                         | O(n)             | O(n)       | O(n)       | O(n)    |

**The big one:** `in` on a list is O(n). `in` on a set or dict is O(1). If you find yourself doing `if x in some_list` inside a loop, you've made it O(n²). Convert the list to a set first.

---

## Idioms to memorize

### List comprehensions
```python
squares = [x*x for x in nums]
evens = [x for x in nums if x % 2 == 0]
pairs = [(i, x) for i, x in enumerate(nums) if x > 0]
```

### `enumerate` — index + value
```python
for i, x in enumerate(nums):
    ...
for i, x in enumerate(nums, start=1):  # 1-indexed
    ...
```

### `zip` — parallel iteration
```python
for name, score in zip(names, scores):
    ...
pairs = list(zip(a, b))            # [(a0, b0), (a1, b1), ...]
a2, b2 = zip(*pairs)               # unzip
```

### Dict-of-lists pattern (grouping)
```python
from collections import defaultdict
groups = defaultdict(list)
for user, item in events:
    groups[user].append(item)
```

Without `defaultdict`:
```python
groups = {}
for user, item in events:
    groups.setdefault(user, []).append(item)
```

### `dict.get(k, default)` — safe lookup
```python
count = counts.get(word, 0) + 1
counts[word] = count
```

### Set operations (math notation)
```python
a & b    # intersection
a | b    # union
a - b    # difference (in a, not in b)
a ^ b    # symmetric difference (in one, not both)
a <= b   # subset?
```

### Tuple unpacking
```python
x, y = point
a, *rest = nums          # a = nums[0], rest = nums[1:]
for (user, item) in events:
    ...
```

### Sorting basics
```python
sorted(items)
sorted(items, key=lambda x: x[1])           # by 2nd field
sorted(items, key=lambda x: (-x[0], x[1]))  # desc, then asc tiebreak
items.sort()                                # in-place
```

---

## The four "I should reach for X" reflexes

| If you find yourself...                              | Reach for...        |
| ---------------------------------------------------- | ------------------- |
| Checking `if x in list` inside a loop                | `set(list)` first   |
| Building `if k in d: d[k].append(v) else: d[k]=[v]`  | `defaultdict(list)` |
| Counting occurrences of items                        | `Counter(seq)`      |
| Using a list/dict as a dict key                      | `tuple` / `frozenset` |

---

## Gotchas (the ones that bite in interviews)

1. **Don't mutate a list while iterating over it.** Copy first: `for x in nums[:]:`.
2. **Dict keys must be hashable.** Lists and dicts are not. Tuples (of hashables) and frozensets are.
3. **Default mutable arguments are shared across calls.** `def f(x, acc=[])` is a bug. Use `acc=None` then `if acc is None: acc = []`.
4. **Strings are immutable.** `s += 'a'` in a loop is O(n²). Use `''.join(parts)`.
5. **`is` vs `==`**: `is` is identity (same object), `==` is equality. For ints in `[-5, 256]` and small strings, `is` may coincidentally work because of interning — don't rely on it.

---

## Staff-level habits — apply to every problem today

1. **Clarify first** (2 min). Read the problem aloud. Ask: input shape? size? duplicates? edge cases (empty, single element)?
2. **State assumptions.** "I'll assume all inputs fit in memory."
3. **Brute force first.** Get O(n²) working in 5 min. Then optimize.
4. **Modularize.** Even a 10-line problem deserves a named function with a docstring line.
5. **Test as you go.** Hand-craft 1 example. Run it. *Then* the next function.
6. **Narrate trade-offs.** "Set lookup is O(1) avg, so total is O(n)."
