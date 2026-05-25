# Day 2 — Concept brief (quick reference)

`collections`: `Counter`, `defaultdict`, `deque`, `OrderedDict`. One page. Glance, then solve.

---

## Complexity cheat sheet

| Operation                            | `Counter` | `defaultdict` | `deque`        | `OrderedDict` |
| ------------------------------------ | --------- | ------------- | -------------- | ------------- |
| Construct from iterable of length n  | O(n)      | O(n)          | O(n)           | O(n)          |
| Lookup `d[k]` / `k in d`             | O(1) avg  | O(1) avg      | O(n) middle    | O(1) avg      |
| Append / push                        | O(1)      | O(1) avg      | O(1) both ends | O(1) avg      |
| Pop                                  | O(1)      | O(1) avg      | O(1) both ends | O(1) avg      |
| `most_common(k)`                     | **O(n log k)** | —          | —              | —             |
| `move_to_end(k)`                     | —         | —             | —              | O(1)          |

**The big one:** `deque` is for queues, **not** arbitrary indexing. `dq[i]` for middle `i` is O(n). If you need both fast ends and fast middle, you're using the wrong data structure.

---

## Idioms to memorize

### `Counter` — counting hashables

```python
from collections import Counter

c = Counter(["a", "b", "a", "c", "a"])
# Counter({'a': 3, 'b': 1, 'c': 1})

c.most_common(2)        # [('a', 3), ('b', 1)]   — top-2 by count
c["a"]                  # 3
c["z"]                  # 0   — Counter returns 0 for missing, not KeyError
c.total()               # 5   — sum of all counts (Python 3.10+)

# Multiset equality — the canonical anagram check
Counter("aab") == Counter("baa")     # True
Counter("aab") == Counter("abb")     # False  — fixes Day 1's valid_anagram bug
```

### `defaultdict` — auto-create on missing key

```python
from collections import defaultdict

groups = defaultdict(list)
for user, item in events:
    groups[user].append(item)        # no `if user not in groups` needed

counts = defaultdict(int)
for word in words:
    counts[word] += 1                # missing → 0, then += 1

nested = defaultdict(lambda: defaultdict(int))
nested["a"]["b"] += 1                # both levels auto-create
```

### `deque` — double-ended queue, O(1) at both ends

```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)           # right
dq.appendleft(0)       # left
dq.pop()               # right → 4
dq.popleft()           # left → 0

# Fixed-size sliding window — auto-evicts from other end
window = deque(maxlen=3)
for x in stream:
    window.append(x)   # if len > 3, leftmost is dropped
```

### `OrderedDict` — when insertion order plus `move_to_end` matters

```python
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od.move_to_end("a")        # O(1) — used in LRU caches
od.popitem(last=False)     # pop from left (oldest)
```

Regular `dict` preserves insertion order since Python 3.7. Use `OrderedDict` only if you need `move_to_end` or order-sensitive equality.

---

## Reflexes — "If I'm doing X, reach for Y"

| If you're doing...                                          | Reach for...                       |
| ----------------------------------------------------------- | ---------------------------------- |
| Counting occurrences of items                               | `Counter(seq)`                     |
| Top-K frequent items                                        | `Counter(seq).most_common(k)`      |
| Multiset equality (anagram, "same bag of items?")           | `Counter(a) == Counter(b)`         |
| Group-by (key → list of values)                             | `defaultdict(list)`                |
| Inverted index (key → set of values)                        | `defaultdict(set)`                 |
| BFS or level-order traversal                                | `deque` as queue, `popleft()`      |
| Sliding window over a stream                                | `deque`, often with `maxlen`       |
| LRU cache / "move to most-recent"                           | `OrderedDict.move_to_end`          |

---

## The two templates worth memorizing

### BFS over a graph

```python
from collections import deque

def bfs(start, neighbors):
    queue = deque([start])
    seen = {start}
    while queue:
        node = queue.popleft()
        for nb in neighbors(node):
            if nb not in seen:
                seen.add(nb)
                queue.append(nb)
    return seen
```

### Sliding window — count events in last `W` seconds at every tick

```python
from collections import deque

def counts_in_window(timestamps, W):
    q = deque()
    out = []
    for ts in timestamps:
        q.append(ts)
        while q and q[0] < ts - W:
            q.popleft()
        out.append(len(q))
    return out
```

---

## Gotchas (the ones that bite in interviews)

1. **`Counter` arithmetic drops zero/negative counts.** `Counter({'a':3}) - Counter({'a':5})` is `Counter()`, not `Counter({'a': -2})`. If you want signed differences, subtract `.values()` manually.
2. **`Counter[k]` returns 0 for missing**, not `KeyError`. Sometimes desired (counting), sometimes hides bugs (you'd want `KeyError` to fire). For non-counting lookups, use a plain dict.
3. **Reading `defaultdict[k]` for a missing key INSERTS the key.** Use `.get()` or `in` for "look without inserting." `dict(my_defaultdict)` before returning if the caller shouldn't see surprise auto-inserts.
4. **`deque` middle access is O(n).** Don't write `dq[len(dq)//2]` in a loop. Convert to list if you need indexed scans.
5. **`Counter(seq).most_common(k)`** is O(n log k), but `most_common()` with no argument sorts everything — O(n log n). Pass `k` when you have one.
6. **Ties in `most_common`** are not guaranteed-stable across Python versions. If you need deterministic tiebreaking, sort with an explicit key.

---

## Staff-level habits — apply to every problem today

(Cross-reference: same list as Day 1.)

1. **Clarify first.** Input shape? Are ties allowed in top-K? What if k > unique items? Empty input?
2. **State assumptions.** "I'll return top-K with ties broken arbitrarily; flag if the spec needs deterministic order."
3. **Brute force first.** `sorted(counts.items(), key=...)[:k]` is O(n log n) but takes 30 seconds — write it, ship, then upgrade to heap if asked.
4. **Modularize.** `count_events`, `top_k`, `format_output` — even if each is 3 lines.
5. **Test as you go.** Before declaring done: invent ONE counter-test beyond the file's asserts. (This is the Day 1 lesson made into a checklist item.)
6. **Narrate trade-offs.** "`most_common(k)` is O(n log k); sorting is O(n log n). Heap wins when k « n."
