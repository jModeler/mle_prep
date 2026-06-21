# `Counter` — from first principles

## What it is

`collections.Counter` is a `dict` subclass specialized for counting hashable objects. Pass it an iterable; you get `{item: count}` back.

```python
from collections import Counter

c = Counter(["apple", "banana", "apple", "cherry", "apple", "banana"])
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})
```

It IS a dict — `c["apple"]`, `c.get("foo", 0)`, `"apple" in c`, iteration — everything dict-like works.

## Why reach for it

Two killer features:

1. **`most_common(k)`** — top-K by count, descending. The single most useful interview idiom.
2. **Counter arithmetic** — `+`, `-`, `&`, `|` for multiset operations.

```python
c.most_common(2)        # → [('apple', 3), ('banana', 2)]
c.most_common()         # → all items, sorted by count desc
```

`most_common(k)` uses a heap internally — **O(n log k)**, faster than sorting the whole dict for top-K.

## Counter arithmetic

```python
a = Counter(["x", "y", "y"])
b = Counter(["y", "z"])

a + b   # Counter({'y': 3, 'x': 1, 'z': 1})    — add counts
a - b   # Counter({'x': 1, 'y': 1})            — subtract (drops ≤ 0)
a & b   # Counter({'y': 1})                    — min of counts (intersection)
a | b   # Counter({'y': 2, 'x': 1, 'z': 1})    — max of counts (union)
```

## Multiset equality (the Day 1 lesson, banked)

```python
Counter("aab") == Counter("aba")  # True  — same multiset
Counter("aab") == Counter("abb")  # False — different multiset

set("aab") == set("aba")          # True  — also True (same letters)
set("aab") == set("abb")          # True  — WRONG, but set says True
```

**Counter is the correct anagram check.** Set equality silently loses duplicate information.

## Counter vs `defaultdict(int)`

|  | `Counter(seq)` | `defaultdict(int)` |
|---|---|---|
| Build from iterable | one line | manual loop |
| Top-K | `c.most_common(k)` built-in | sort manually |
| Missing key | `c[k]` returns `0` | also returns `0` |
| Use case | "count then query / top-K" | "count then iterate / consume raw" |

For counting + top-K, **always Counter**. For counting + immediate consumption, either is fine.

## Connection to the Tubi prompt

For "top-K items in last hour":

```python
import bisect
from collections import Counter

# events: sorted list of (timestamp, item_id) tuples
cutoff = now - 3600
start_idx = bisect.bisect_left([e[0] for e in events], cutoff)
items_in_window = [e[1] for e in events[start_idx:]]
top_k = Counter(items_in_window).most_common(k)
# → [(item_id, count), ...] sorted desc
```

Two-line query after the data is in the right layout.
