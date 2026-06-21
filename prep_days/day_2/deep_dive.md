# Day 2 — Deep dive ("textbook")

For when the brief feels too thin. Built from first principles. Skip sections you already know cold.

---

## Section 0 — Why `collections` is interview gold

Every Tubi coding theme (event store, weighted sampling, recommendations) involves either *counting things* or *windowing over a stream* or both. Plain `dict` and `list` can do it, but you'll burn 30+ seconds writing `if k not in d: d[k] = []` boilerplate every time. The four utilities below replace that boilerplate with one-liners — and more importantly, they *signal fluency* to the interviewer. A staff candidate doesn't write `setdefault(k, []).append(v)`; they write `defaultdict(list)` once at the top of the function and forget about it.

If you absorb one thing today: **count → `Counter`, group → `defaultdict`, queue/window → `deque`.** Those three reflexes save more interview time than any algorithmic trick.

---

## Section 1 — `Counter`

### What it actually is

`Counter` is a subclass of `dict`. It looks like a dict, behaves like a dict, but adds counting-aware constructors and methods. Internally: same hash table, same O(1) average lookup.

```python
from collections import Counter

# Three ways to construct
c1 = Counter(["a", "b", "a"])              # from iterable
c2 = Counter({"a": 2, "b": 1})             # from mapping
c3 = Counter(a=2, b=1)                     # from keyword args

c1 == c2 == c3   # True
```

### The "missing key returns 0" behavior

```python
c = Counter("abc")
c["z"]           # 0  — not KeyError
"z" in c         # False  — still false; access doesn't insert (unlike defaultdict)
```

This is the **opposite** of `defaultdict`'s behavior. `Counter[k]` for a missing key returns 0 *but does not insert*. So you can write `if c[event] > threshold:` safely without polluting the Counter.

### `most_common(k)` — what's actually happening

```python
c = Counter("mississippi")
c.most_common(2)        # [('i', 4), ('s', 4)]
c.most_common()         # [('i', 4), ('s', 4), ('p', 2), ('m', 1)]  — all, sorted
```

Internally, `most_common(k)` uses `heapq.nlargest(k, ...)`, which is **O(n log k)** — strictly better than sorting all n items (O(n log n)) when k « n. With no argument, it falls back to `sorted` and is O(n log n).

So `Counter(items).most_common(k)` is the canonical, single-line top-K implementation. Don't reinvent it.

### Counter arithmetic — the subtle one

```python
c1 = Counter({"a": 3, "b": 1})
c2 = Counter({"a": 1, "b": 2})

c1 + c2          # Counter({'a': 4, 'b': 3})       — element-wise add
c1 - c2          # Counter({'a': 2})               — element-wise subtract, drops <= 0
c1 & c2          # Counter({'a': 1, 'b': 1})       — element-wise min (intersection)
c1 | c2          # Counter({'a': 3, 'b': 2})       — element-wise max (union)
```

**The gotcha**: subtraction drops zero and negative counts. If you actually wanted to know "user lost 2 of item a," `c1 - c2` won't show it. Use `Counter.subtract(other)` if you want to preserve negatives:

```python
c1.subtract(c2)
c1               # Counter({'a': 2, 'b': -1})       — negatives kept
```

### The Day 1 connection — multiset equality

Two Counters compare equal iff they have the same keys with the same counts. That's *exactly* what an anagram is:

```python
def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

One line, O(n), correct. Day 1's Valid Anagram bug (`set(s) == set(t)`) failed because sets discard counts; `Counter` keeps them. **This is the single most useful idiom of the day.**

---

## Section 2 — `defaultdict` (deeper than Day 1)

### The factory pattern, made explicit

`defaultdict(factory)` takes a **zero-argument callable**. When you access a missing key, the factory is called and the result becomes the default value — *and is inserted into the dict*.

```python
from collections import defaultdict

d = defaultdict(list)
d["new_key"].append(1)
# Steps that just happened:
#   1. d["new_key"] is missing
#   2. factory `list` is called → returns []
#   3. [] is inserted under "new_key"
#   4. .append(1) mutates that list to [1]
# Result: d == {"new_key": [1]}
```

### Three things that look right but aren't

```python
defaultdict([])         # ❌ a list instance is not callable
defaultdict(list())     # ❌ same — list() is the empty list, not the type
defaultdict({})         # ❌ a dict is not callable
defaultdict(list)       # ✅ the `list` type itself, which is callable
```

You pass the **type** (or any zero-arg callable), not an instance.

### Custom factories with `lambda`

```python
# Two-level nested counts: d[user][item] = count
nested = defaultdict(lambda: defaultdict(int))
nested["u1"]["item_a"] += 1
nested["u1"]["item_b"] += 1
nested["u2"]["item_a"] += 1

# Constant default that isn't 0/[]/{}
scores = defaultdict(lambda: -1)
scores["unknown"]          # -1, and key is inserted
```

### Reading a missing key INSERTS — the trap

```python
d = defaultdict(list)
if d["might_exist"]:       # ❌ this just inserted "might_exist" → []
    ...
```

Use `.get()` or `in` for read-only checks:

```python
if d.get("might_exist"):   # returns None on missing, doesn't insert
    ...
if "might_exist" in d:     # also doesn't insert
    ...
```

### Convert back to dict before returning

```python
def group(events):
    d = defaultdict(list)
    for u, i in events:
        d[u].append(i)
    return dict(d)         # caller gets a plain dict, no auto-insert surprises
```

If callers do `result["unknown_user"]` on the returned object and you handed them a `defaultdict`, they'll silently get an empty list instead of `KeyError`. That hides bugs. Strip the auto-insert at the boundary.

---

## Section 3 — `deque`

### Why it's O(1) at both ends — and not in the middle

Internally, `deque` is a doubly-linked list of *blocks* — each block is a small array (~64 items in CPython). Appending or popping at either end is O(1) because there's a head pointer and a tail pointer. There's no shifting.

Middle access is **O(n)** because you have to walk the linked block list to find the right block. `deque[len(dq)//2]` looks like indexed access but isn't.

```python
from collections import deque

dq = deque([1, 2, 3, 4])
dq.append(5)            # O(1)
dq.appendleft(0)        # O(1)
dq.pop()                # O(1)
dq.popleft()            # O(1)
dq[2]                   # O(n) — walks blocks
```

### `maxlen` — the underrated feature

```python
window = deque(maxlen=3)
for x in [1, 2, 3, 4, 5]:
    window.append(x)
    print(list(window))
# [1]
# [1, 2]
# [1, 2, 3]
# [2, 3, 4]            ← 1 dropped from the left automatically
# [3, 4, 5]            ← 2 dropped
```

When the deque is full and you append on one end, the opposite end's element is auto-evicted. Useful for "last K events" patterns without writing eviction logic yourself.

### BFS template — the one you'll use most

```python
from collections import deque

def bfs(start, neighbors):
    queue = deque([start])
    seen = {start}
    while queue:
        node = queue.popleft()       # FIFO — what makes it BFS
        for nb in neighbors(node):
            if nb not in seen:
                seen.add(nb)
                queue.append(nb)
    return seen
```

If you use `pop()` instead of `popleft()`, you get DFS. The data structure is the same; the access pattern is the algorithm.

### Sliding window template — variable-width version

For "count events in the last 60 seconds at every tick":

```python
def counts_in_window(timestamps, W):
    q = deque()
    out = []
    for ts in timestamps:
        q.append(ts)
        while q and q[0] < ts - W:    # evict everything too old
            q.popleft()
        out.append(len(q))
    return out
```

This is **O(n)** total across the whole input, even though there's a `while` inside the `for`: each element is pushed once and popped at most once, so total pops ≤ n.

This template — push current, drain stale, record state — is the backbone of every time-window event-store problem on Day 4 and Day 15.

---

## Section 4 — `OrderedDict` — when it still matters

### What changed in Python 3.7

Before 3.7, dict iteration order was *implementation-defined* (effectively random). `OrderedDict` existed to give you insertion-order iteration.

From 3.7 onward, **regular dicts preserve insertion order as a language guarantee.** So for plain "iterate in insertion order" use cases, regular `dict` is fine — `OrderedDict` is redundant.

### When you still reach for it

**1. `move_to_end(k)` is O(1).** Used in LRU caches:

```python
from collections import OrderedDict

class LRU:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, k):
        if k not in self.cache:
            return -1
        self.cache.move_to_end(k)         # mark as most-recently-used
        return self.cache[k]

    def put(self, k, v):
        if k in self.cache:
            self.cache.move_to_end(k)
        self.cache[k] = v
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # evict least-recently-used
```

You *could* implement an LRU with a dict + linked list yourself (this is a popular interview question), but `OrderedDict` packages exactly that internally.

**2. Order-sensitive equality.**

```python
{1: 'a', 2: 'b'} == {2: 'b', 1: 'a'}                # True  — dicts ignore order
OrderedDict([(1,'a'),(2,'b')]) == OrderedDict([(2,'b'),(1,'a')])   # False
```

Niche. Almost never relevant in interview problems.

---

## Section 5 — `namedtuple` (brief)

Already covered in Day 1's deep dive. Quick recap:

```python
from collections import namedtuple
Event = namedtuple("Event", ["user_id", "item_id", "timestamp"])
e = Event("u42", "item7", 1716543210)
e.user_id, e[0]          # "u42", "u42"
```

When to use: you'd otherwise be writing `event[2]` everywhere and forgetting which index is which. Hashable (so usable as dict keys). Slightly more memory-efficient than a dict.

A heavier modern alternative is `dataclasses.dataclass(frozen=True)` — same idea, more features, mutable by default. For interview brevity, named tuples win.

---

## Section 6 — Interview reflexes (the table to internalize)

| Problem shape                                          | Reach for...                       | Why                                    |
| ------------------------------------------------------ | ---------------------------------- | -------------------------------------- |
| "Count how many times each X appears"                  | `Counter`                          | One-line construction                  |
| "Top K most frequent"                                  | `Counter.most_common(k)`           | O(n log k), already written for you    |
| "Are these two collections the same multiset?"         | `Counter(a) == Counter(b)`         | Multiset equality                      |
| "Group items by key into lists"                        | `defaultdict(list)`                | Skips the `if k not in d` branch       |
| "Group items by key into sets / dedup per key"         | `defaultdict(set)`                 | Same, with dedup                       |
| "Two-level grouping: `d[key1][key2] = count`"          | `defaultdict(lambda: defaultdict(int))` | Nested factory                    |
| "BFS / level-order traversal"                          | `deque`, use `popleft()`           | O(1) FIFO                              |
| "Sliding window over a stream"                         | `deque`, drain stale from left     | O(n) total                             |
| "Last K events / fixed-size buffer"                    | `deque(maxlen=K)`                  | Auto-evicts                            |
| "LRU cache / 'mark this as recently used'"             | `OrderedDict.move_to_end`          | O(1) reorder                           |
| "Compound dict key with named fields"                  | `namedtuple` (or `tuple`)          | Hashable, readable                     |

---

## Section 7 — Putting it together: top-K event types over a window

A miniature event-store problem that uses three of today's tools at once:

```python
from collections import Counter, deque

def top_k_in_window(events, W, k):
    """
    events: list of (timestamp, event_type), sorted by timestamp.
    Return list of (last_seen_ts, top_k_types) at every tick.
    A type is in the window if its timestamp is within W of the current ts.
    """
    window = deque()
    counts = Counter()
    out = []

    for ts, et in events:
        window.append((ts, et))
        counts[et] += 1

        # Evict events older than ts - W
        while window and window[0][0] < ts - W:
            old_ts, old_et = window.popleft()
            counts[old_et] -= 1
            if counts[old_et] == 0:
                del counts[old_et]     # keep the Counter clean for most_common

        out.append((ts, [t for t, _ in counts.most_common(k)]))
    return out
```

Three reflexes in eight lines: `deque` for the sliding window, `Counter` for counts, `most_common(k)` for the top-K. This is the shape of a Day 15 event-store extension. Sit with it for two minutes; you should be able to reproduce the pattern (not the exact code) from memory by Day 7.

---

## Section 8 — Production lens (one-sentence-per-row)

| You're doing this in toy code...               | At scale, you'd reach for...                                                |
| ---------------------------------------------- | --------------------------------------------------------------------------- |
| `Counter` over the full event stream           | A streaming counter — HLL for cardinality, Count-Min Sketch for top-K       |
| `deque(maxlen=N)` for recent events            | A Kafka consumer with a retention window, or Redis stream with `XLEN` trim  |
| `OrderedDict`-based LRU                        | Redis with eviction policy `allkeys-lru`, or a CDN cache                    |
| `defaultdict(list)` to group all events        | A real groupby (Spark, SQL `GROUP BY`), or a shuffle in a MapReduce job     |

You don't implement the right column. You **name it** during the trade-offs discussion. One sentence per row is enough to signal staff-level awareness.

---

## Section 9 — How to apply this to today's problems

Before each problem:

1. **Is this a counting problem?** → `Counter`.
2. **Am I grouping by key?** → `defaultdict(list)` or `defaultdict(set)`.
3. **Am I doing FIFO / sliding window / BFS?** → `deque`.
4. **Do I need "move to most-recent"?** → `OrderedDict.move_to_end`.
5. **What's my brute force?** Write it. Then ask "is the bottleneck a count? A scan? A grouping?" — that tells you which tool to apply.

Today's three problems map one-to-one to the first three reflexes. The self-test uses two of them.

Now go solve.
