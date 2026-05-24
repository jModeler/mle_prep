# Day 1 — Deep dive ("textbook")

For when the brief feels too thin. Built from first principles. Skip sections you already know cold.

---

## Section 0 — Why complexity matters in an interview

A staff-level signal isn't just "did you write working code." It's "do you know which choice scales and why." Interviewers grade on whether you can say:

> "Lookup in a list is O(n). I'm doing this lookup inside a loop, so this is O(n²). I'll convert to a set first — O(n) build, O(1) lookups, total O(n)."

If you can narrate that one sentence on every problem today, you've absorbed Day 1.

---

## Section 1 — Memory model in 60 seconds

Two ideas you need:

**Contiguous memory.** A "list" in Python is internally an array — a block of memory where item `i` lives at offset `i * pointer_size`. Reading `nums[5]` is just arithmetic: jump to `base_address + 5 * 8 bytes`. That's why index access is O(1) — it's a single hardware operation, doesn't depend on list length.

**Hash tables.** A dict (or set) is an array under the hood too, but the index isn't `i`. The index is `hash(key) % table_size`. Compute the hash of the key, mod by table size, jump to that slot. That's why lookup is O(1) average — same arithmetic-then-jump, just with a hash function in front. We'll unpack hash tables in Section 3.

That's it. Everything else in this doc comes from these two ideas.

---

## Section 2 — Lists (a.k.a. dynamic arrays)

### Why append is O(1) amortized — not "always O(1)"

A Python list is backed by a fixed-size C array. When you `.append()` and there's still room, it's just "write to slot `i`, increment `i`" — O(1). When the array fills up, Python allocates a **bigger** array (typically ~1.125× larger in CPython, but think of it as doubling for analysis), copies all old elements over, then writes the new one. That copy is O(n).

"Amortized" means: across many appends, the cost averages out to O(1). The math:

- After n appends, you've done ~log(n) resize events.
- Total copy work is `1 + 2 + 4 + 8 + ... + n/2 + n ≈ 2n` operations.
- Divided by n appends, that's O(1) per append on average.

So in interview-speak: "append is O(1) amortized." For competitive analysis, treat it as O(1).

### Why insert-at-front is O(n)

`nums.insert(0, x)` has to shift every existing element one slot to the right to make room. n elements moved → O(n). Same for `pop(0)`.

**Reflex:** If you need fast append-and-pop from both ends, use `collections.deque` (Day 2 material). It's a doubly-linked block structure — O(1) at both ends.

### Why `in` on a list is O(n)

`if x in nums` is implemented as a linear scan: check `nums[0] == x`, `nums[1] == x`, ... until you find it or hit the end. There's no shortcut — the list isn't sorted, isn't hashed, just a flat array.

**The classic O(n²) interview trap:**

```python
duplicates = []
for x in nums:
    if x in duplicates:     # O(len(duplicates))
        ...
    duplicates.append(x)
```

Total work: 1 + 2 + 3 + ... + n ≈ n²/2 = **O(n²)**. The fix is to use a set:

```python
seen = set()
for x in nums:
    if x in seen:           # O(1)
        ...
    seen.add(x)
```

Total: O(n). This is the single highest-yield reflex on Day 1.

### List slicing

`nums[a:b]` creates a **new list** of length `b - a`. That's O(b - a) time and space. Don't slice in a hot loop without thinking.

---

## Section 3 — Dicts (hash tables)

### What's a hash function?

`hash(x)` is a function that turns an object into a (large) integer, deterministically. Same input → same hash, always (within a Python process). Different inputs usually → different hashes (collisions are possible but rare for good hash functions).

```python
>>> hash("apple")
-3613886112720006247
>>> hash(42)
42
>>> hash((1, 2))
3713081631934410656
```

### How a dict stores `{"apple": 3, "banana": 5}`

Internally:

1. Allocate an array of "slots" (say, size 8 to start).
2. To insert `"apple": 3`: compute `hash("apple") % 8 = 3`. Write `("apple", 3)` into slot 3.
3. To insert `"banana": 5`: compute `hash("banana") % 8 = 7`. Write into slot 7.
4. To look up `"apple"`: compute `hash("apple") % 8 = 3`, jump to slot 3, return the value.

All O(1) — same as array index access, just with `hash()` first.

### What happens on collision

Two keys can hash to the same slot. CPython handles this with **open addressing** (probing): if slot 3 is taken, try slot 4, then 5, etc., until you find an empty one. On lookup, same probe sequence.

For most realistic key distributions, the average probe length stays near 1 — that's why we say O(1) "average." The worst case is O(n) if every key collides into the same slot (e.g., an adversary chose your keys to attack you), but you'll never hit that in a normal interview problem.

### Why dict insert order is preserved (Python 3.7+)

CPython stores entries in a separate **insertion-order array** and the hash table just holds indices into that array. So iteration follows insertion order, and the hash table still gives O(1) lookup. (Don't need to know this for the interview; just know it's true.)

### Why dict keys must be hashable

A dict needs to call `hash(key)`. Lists are mutable — if you used a list as a key, then mutated it, its hash would change, and the dict could no longer find it. To prevent this footgun, mutable types raise `TypeError: unhashable type` when you try to hash them.

**Hashable:** ints, floats, strings, tuples (of hashables), frozensets, None, bools.
**Unhashable:** lists, dicts, sets.

If you need a tuple-like key, use a tuple: `d[(user_id, item_id)] = ...`.

### `dict.get` vs `dict[k]` vs `defaultdict`

```python
# 1. Bracket — raises KeyError if missing
counts[word] += 1                  # KeyError if word not seen

# 2. get with default — returns default but does NOT insert
count = counts.get(word, 0)        # safe; doesn't add the key

# 3. setdefault — returns default AND inserts if missing
counts.setdefault(word, 0)
counts[word] += 1                  # works on first encounter

# 4. defaultdict — auto-inserts default the first time
from collections import defaultdict
counts = defaultdict(int)
counts[word] += 1                  # works on first encounter, key gets added
```

Reflex: building a `dict-of-lists`? Use `defaultdict(list)`. Counting? Use `Counter` (Day 2).

---

## Section 4 — Sets

A set is a dict with no values. Same hash-table machinery, same O(1) average lookup, same hashable-keys requirement. Use a set whenever you need "have I seen this?" and you don't care about associated data.

### Set algebra — and why the operators exist

Pretend sets are math sets. The operators come directly from set theory:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a & b   # intersection         {3, 4}        — items in both
a | b   # union                {1,2,3,4,5,6} — items in either
a - b   # difference           {1, 2}        — in a but not b
a ^ b   # symmetric difference {1, 2, 5, 6}  — in exactly one
```

Each is O(len(a) + len(b)) — you scan both. Useful one-liners:

```python
common_users = set(today_users) & set(yesterday_users)
new_users = set(today_users) - set(yesterday_users)
```

### `frozenset`

Immutable version of a set. Hashable, so you can use it as a dict key or put it in another set. Use when you need to key on "the unordered combination of things" — e.g., grouping anagrams could (badly) use `frozenset(word)` as a key, except that doesn't account for duplicate letters. (We'll see the right key shortly.)

---

## Section 5 — Tuples

A tuple is an immutable list. Two consequences:

1. **Hashable** (if all elements are). So usable as dict keys / set members.
2. **Fixed memory layout** known at creation. Slightly more compact than a list. Marginally faster to construct.

The interview reason to use tuples is almost always reason 1: you want a compound dict key.

```python
trip_counts = defaultdict(int)
for from_city, to_city in trips:
    trip_counts[(from_city, to_city)] += 1   # tuple key
```

### Named tuples — when readability > brevity

```python
from collections import namedtuple
Event = namedtuple("Event", ["user_id", "item_id", "timestamp"])
e = Event("u42", "item7", 1716543210)
e.user_id            # "u42"
e[0]                 # still works
```

Use named tuples when you'd otherwise be writing `event[2]` in 4 different places and forgetting which index is which. For interview problems, plain tuples are usually fine; just call out the field names in comments.

---

## Section 6 — The big gotchas

### Gotcha 1: Mutating a list while iterating it

```python
nums = [1, 2, 3, 4]
for x in nums:
    if x % 2 == 0:
        nums.remove(x)        # surprising results — iterator gets confused
```

Iterate over a copy, or build a new list:

```python
nums = [x for x in nums if x % 2 != 0]
```

### Gotcha 2: Mutable default arguments

```python
def add_item(item, bucket=[]):     # bucket is created ONCE at def time
    bucket.append(item)
    return bucket

add_item("a")    # ['a']
add_item("b")    # ['a', 'b']   ← surprising! bucket is shared
```

Fix:

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

### Gotcha 3: String concatenation in a loop

```python
s = ""
for chunk in chunks:
    s += chunk          # creates a new string each time — O(n²) total
```

Strings are immutable, so `s += chunk` allocates a brand-new string of length `len(s) + len(chunk)`. Use `join`:

```python
s = "".join(chunks)     # O(total length)
```

### Gotcha 4: Shallow vs deep copy

```python
a = [[1, 2], [3, 4]]
b = a[:]            # shallow — outer list copied, inner lists shared
b[0].append(99)
a                   # [[1, 2, 99], [3, 4]]  ← a was mutated too
```

For nested structures, `copy.deepcopy(a)`. In interviews, almost always use shallow copy + rebuild rather than `deepcopy` — it's faster to reason about.

---

## Section 7 — Production lens (one-sentence-per-row table)

| You're doing this in toy code...        | At scale, you'd reach for...                       |
| --------------------------------------- | -------------------------------------------------- |
| `defaultdict(list)` to group events     | A real groupby (pandas, SQL), or shuffled MR step  |
| `Counter` over all events in memory     | A streaming counter (HLL for cardinality, CMS for top-k) |
| `set()` of "seen IDs" growing forever   | A bloom filter / probabilistic dedup / TTL cache   |
| dict from `user_id` → big object        | A KV store (Redis, RocksDB) or a feature store     |

You don't need to *implement* the right-hand-side. You just need to *name* it when you're discussing extensions. One sentence is worth a full grade level.

---

## Section 8 — How to apply this to today's problems

For each problem, before you code:

1. **What's the input shape?** List of ints? List of strings? Pairs?
2. **What lookup or grouping am I doing?** That's your signal for which container to reach for.
3. **What's the brute-force complexity?** Almost always O(n²).
4. **Can I drop to O(n) by adding a set or dict?** Almost always yes.
5. **What's the right key for my dict / set?** That's the actual problem.

This last one — *what's the right key* — is the entire skill being tested in Group Anagrams and Valid Anagram. The container is obvious. The key isn't.

Now go solve.
