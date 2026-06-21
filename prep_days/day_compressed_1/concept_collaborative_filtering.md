# Collaborative filtering — from first principles

## The core idea

You have a sparse **user × item** interaction matrix. Entries are ratings, watches, clicks — anything that says "user U engaged with item I." Most entries are empty. Goal: predict what user U would like that they haven't seen.

Two flavors:

- **User-user CF**: "Find users with similar tastes to you, recommend what they liked that you haven't seen."
- **Item-item CF**: "Find items similar to ones you liked, recommend more like those."

For a from-scratch interview implementation, **user-user is simpler**. Both are O(n²) at the similarity step — they fall over at scale, which is why production uses matrix factorization, two-tower embeddings, or ANN indices. For a 60-min interview, the dumb O(n²) version is the right answer; mention the production replacement as a trade-off.

## Algorithm (user-user)

Given:
- `events`: stream of `(user_id, item_id)` (or with ratings)
- `target_user`: the user we're recommending for
- `k`: number of items to return
- `n_similar`: number of nearest-neighbor users to aggregate from

Steps:

1. **Build the user → items map.** `user_items[uid] = set_of_items` (or dict of `item → rating` if you have ratings).
2. **Compute similarity** between `target_user` and every other user.
3. **Pick top-N similar users.**
4. **Aggregate items** those users liked that the target hasn't seen.
5. **Score each candidate item** (weighted sum by similarity).
6. **Return top-K** by score.

Worked example:

```
target_user "u1" has {a, b, c}

Other users:
  u2: {a, b, d}        sim with u1 = 2/4 = 0.5
  u3: {a, b, c, e}     sim with u1 = 3/4 = 0.75
  u4: {x, y, z}        sim with u1 = 0/6 = 0

Top similar (positive only): u3 (0.75), u2 (0.5)
Their items not in u1's set:
  u3 → e (score += 0.75)
  u2 → d (score += 0.5)

Recommend: [e, d].
```

## Similarity metrics

### Jaccard (sets — simplest)

```
jaccard(A, B) = |A ∩ B| / |A ∪ B|
```

Range [0, 1]. Use when all you have is "user engaged or didn't."

```python
def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)
```

### Cosine (vectors — when ratings matter)

```
cosine(u, v) = dot(u, v) / (||u|| × ||v||)
```

Range [-1, 1] (effectively [0, 1] for non-negative ratings).

```python
import math

def cosine(u: dict, v: dict) -> float:
    common = set(u) & set(v)
    if not common:
        return 0.0
    dot = sum(u[k] * v[k] for k in common)
    norm_u = math.sqrt(sum(x * x for x in u.values()))
    norm_v = math.sqrt(sum(x * x for x in v.values()))
    if norm_u == 0 or norm_v == 0:
        return 0.0
    return dot / (norm_u * norm_v)
```

For an interview from scratch, **Jaccard is faster to type and harder to fumble**. Default to it unless you have rating data and want to show the upgrade.

## Cold start (free talking points)

- **New user**: no history → can't find similar users → fall back to popularity, or use content-based features.
- **New item**: nobody has interacted → won't appear in any user's set → forced exploration / content-embedding fallback.

Mention these in passing during the interview to signal staff-level awareness. Don't implement unless asked.

## Why this isn't the production answer

- **O(n²) similarity** — explodes at millions of users.
- **No latent factors** — can't generalize across users with zero overlap.
- **No content signals** — only co-occurrence.

Production reaches for:
- **Matrix factorization** (ALS, SVD) — latent user and item embeddings.
- **Two-tower neural** — separate encoders, ANN serving (FAISS / ScaNN).
- **Item-item with ANN** — precompute item embeddings, serve nearest neighbors at query time.

If asked "how would you scale this," that's the answer. One sentence each is enough unless they probe.

## Connection to the Tubi prompt

For `recommend(user_id, k)`:
1. Build `user_items` once from the event store.
2. For target user, compute Jaccard with every other user.
3. Take top-N similar users (e.g., N=10).
4. Aggregate items from those users not in target's set, weighted by similarity.
5. Return top-K by score.
