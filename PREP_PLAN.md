# Tubi ML Coding — 25-Day Prep Plan

**Interview window:** ~2026-06-18 (Day 26)
**Daily budget:** 2–2.5 focused hours
**Format:** 60 min, Python 3 on CoderPad, no LLMs, allowed: `collections`, `bisect`, `heapq`, `random`, `math`
**Failure mode to beat:** most candidates can't *complete* the end-to-end ML pipeline in 60 min — so the plan optimizes for **fluency + speed of building a working pipeline first, polish second.**

---

## How to use this file

- Check off `- [ ]` boxes as you finish each day.
- Each day has: **Concept (~20 min)** + **Implementation/problems (~90 min)** + **Self-test (~10 min)**.
- If a day runs long, don't skip the self-test — that's the muscle memory.
- Keep a `scratch/` folder in this repo. Every implementation goes in there; never delete.

---

## Staff-level habits — drill these into muscle memory

Re-read this list before every mock. These are what separate "completes the problem" from "Staff hire."

1. **Clarify before coding (2–3 min).** Input shape? Output format? Volume? Streaming or batch? Out-of-order allowed? Tied scores — break how? Ask 2–3 sharp questions, *then* code.
2. **State assumptions out loud.** "I'll assume events arrive sorted by timestamp; flag a TODO to extend." Free points.
3. **Start dumb, then optimize.** Get a correct O(n²) running in 10 min. Optimize only after it works. Most candidates fail by trying to be clever first.
4. **Modularize from minute one.** `ingest(...)`, `featurize(...)`, `train(...)`, `predict(...)`, `evaluate(...)` — even if each is 3 lines. Reviewers grade on structure.
5. **Test as you go.** Hand-craft a 3-row example. Run after every function. Don't write 40 lines then debug.
6. **Narrate trade-offs.** "Heap is O(n log k), sort is O(n log n) — heap wins when k << n." Say it out loud.
7. **Production lens.** "At scale, I'd shard by user_id" / "This loses precision on out-of-order events past the window — I'd buffer." One sentence is enough.
8. **Time-box yourself.** If stuck >5 min on syntax, pseudo-code it and move on. Working pipeline > perfect function.

---

## Phase 1 — Python + DSA foundations (Days 1–7)

Goal: be **fluent** with the building blocks. Every idiom below should be writable from a blank file in under 2 minutes by Day 7.

### Day 1 — Sun 2026-05-24 — Lists, dicts, sets, tuples
- [x] **Concept:** time complexity of common ops (list append O(1), insert O(n), `in` for list vs set, dict lookup O(1)).
- [x] **Idioms to memorize:** list comprehensions, `enumerate`, `zip`, dict-of-lists pattern, `dict.get(k, default)`, set operations (`&`, `|`, `-`).
- [x] **Problems:** Two Sum, Group Anagrams, Contains Duplicate, Valid Anagram.
- [x] **Self-test:** "Given a list of (user_id, item_id) events, return a dict of user_id → set of items." Write in <5 min, no lookups.

### Day 2 — Mon 2026-05-25 — `collections` module
- [ ] **Concept:** `Counter`, `defaultdict(list/int/set)`, `deque` (O(1) append+popleft), `OrderedDict`.
- [ ] **Idioms:** `Counter(seq).most_common(k)`, `defaultdict(list).append(...)`, deque for sliding windows and BFS queues.
- [ ] **Problems:** Top K Frequent Elements (use Counter + heap), First Unique Character, Design HashMap.
- [ ] **Self-test:** "Count event types in a stream, return top-3." Under 3 min.

### Day 3 — Tue 2026-05-26 — Sorting
- [ ] **Concept:** `sorted()` is stable; `key=lambda x: (x[0], -x[1])` for multi-key; `reverse=True`.
- [ ] **Idioms:** sort by tuple, sort dict items by value, custom comparator via `functools.cmp_to_key`.
- [ ] **Problems:** Sort Colors, Merge Intervals, Largest Number.
- [ ] **Self-test:** "Given list of (user, score, timestamp), return top-3 per user by score, tiebreak by latest timestamp." Under 7 min.

### Day 4 — Wed 2026-05-27 — Binary search & `bisect` ⭐ (interview-critical)
- [ ] **Concept:** binary search invariant (loop until `lo == hi`); `bisect_left` vs `bisect_right`.
- [ ] **Idioms:** find insertion point, find first/last occurrence, binary search on answer (search-by-condition).
- [ ] **Problems:** Search Insert Position, Find First and Last Position of Element, Search in Rotated Sorted Array.
- [ ] **Code template** (commit to memory):
  ```python
  import bisect
  # find leftmost i where arr[i] >= target
  i = bisect.bisect_left(arr, target)
  ```
- [ ] **Self-test:** "Given sorted list of timestamps and a window [t1, t2], return count of events in window." Under 4 min using `bisect`.

### Day 5 — Thu 2026-05-28 — Heaps (`heapq`)
- [ ] **Concept:** min-heap by default; negate for max-heap; `heapq.heappush/heappop` O(log n); `heapq.nlargest/nsmallest` for top-K.
- [ ] **Idioms:** top-K with a size-K heap (push then pop if > K), k-way merge, running median (two heaps).
- [ ] **Problems:** Kth Largest Element in Array, Top K Frequent Words, Find Median from Data Stream.
- [ ] **Self-test:** "Maintain top-10 highest-scoring items as scores stream in." Under 5 min.

### Day 6 — Fri 2026-05-29 — Two pointers & sliding window
- [ ] **Concept:** two-pointer for sorted arrays; sliding window for subarray problems; expand-right then contract-left.
- [ ] **Idioms:** fixed-size window (sum/count over last K), variable-size window (longest substring with condition).
- [ ] **Problems:** Longest Substring Without Repeating Characters, Minimum Window Substring, Subarray Sum Equals K.
- [ ] **Self-test:** "Count of events in the last 60 seconds at every tick." Under 5 min with a deque.

### Day 7 — Sat 2026-05-30 — Recap + speed drill
- [ ] **Speed drill (60 min, timed):** redo one problem from each of Days 1–6 against the clock. Target: all 6 in 60 min total.
- [ ] **Build a personal cheat sheet** (one page) of idioms you keep forgetting. Keep open during practice (but **not** during the real interview).
- [ ] **Reflect:** which day was hardest? Schedule a 30-min revisit during Days 22–24.

---

## Phase 2 — ML primitives from scratch (Days 8–14)

Goal: every primitive below implemented from a blank file in **under 20 minutes** by Day 14. Pure Python. No numpy unless noted.

### Day 8 — Sun 2026-05-31 — Distance metrics & vector math helpers
- [ ] Implement: `dot(a, b)`, `norm(a)`, `euclidean(a, b)`, `manhattan(a, b)`, `cosine(a, b)`.
- [ ] Edge cases: zero vectors (cosine), different lengths (raise).
- [ ] **Self-test:** for 100 random vectors of dim 5, find nearest neighbor of each. Under 10 min.

### Day 9 — Mon 2026-06-01 — K-Means ⭐
- [ ] Implement: `kmeans(points, k, max_iter=100, tol=1e-4)` returning centroids + cluster assignments.
- [ ] Steps: random init → assign each point to nearest centroid → recompute centroids → repeat until centroids stable.
- [ ] Then add **k-means++ init** (pick centroids weighted by squared distance from existing).
- [ ] Test on a hand-crafted 2D case with 3 obvious clusters.
- [ ] **Self-test:** write KMeans from blank in 20 min, including convergence check.

### Day 10 — Tue 2026-06-02 — KNN
- [ ] Implement: `knn_classify(X_train, y_train, x_query, k)` (majority vote) and `knn_regress(...)` (mean).
- [ ] Add **distance-weighted** variant: weight = 1 / (distance + eps).
- [ ] Discuss with yourself: when is brute-force fine vs. when do you need a KD-tree? (Answer: KD-tree wins for low-dim, large N, repeated queries.)
- [ ] **Self-test:** classify a 2D toy dataset; verify accuracy by hand.

### Day 11 — Wed 2026-06-03 — Weighted random sampling ⭐
- [ ] Implement: `weighted_sample(items, weights)` using prefix-sum + `bisect`.
- [ ] Implement: `weighted_sample_k(items, weights, k)` — both with and without replacement.
- [ ] Implement: **reservoir sampling** (sample k items from a stream of unknown length).
- [ ] **Problem:** LeetCode 528 "Random Pick with Weight" — code it in <10 min.
- [ ] **Self-test:** verify empirically — sample 100k times, check observed frequencies ≈ weights.

### Day 12 — Thu 2026-06-04 — Linear regression
- [ ] Implement: gradient-descent linear regression on 1D and N-D inputs. `fit(X, y, lr, n_iters)`, `predict(X)`.
- [ ] Compute MSE / RMSE.
- [ ] (Optional) closed-form via normal equation — recognize it but don't implement unless time permits.
- [ ] **Self-test:** fit `y = 3x + 2 + noise`, recover coefficients within 5%.

### Day 13 — Fri 2026-06-05 — Logistic regression + classification metrics
- [ ] Implement: logistic regression with sigmoid + log-loss + gradient descent.
- [ ] Implement metrics: `accuracy`, `precision`, `recall`, `f1`, `confusion_matrix`. Make these reusable — keep in a `metrics.py`.
- [ ] **Self-test:** train on a 2-class toy set; report all metrics.

### Day 14 — Sat 2026-06-06 — Train/test split, evaluation harness
- [ ] Implement: `train_test_split(X, y, test_size=0.2, seed=42)` and `k_fold(X, y, k)`.
- [ ] Build a tiny **evaluation harness**: `evaluate(model, X_test, y_test, metric_fn)`.
- [ ] **End of Phase 2 self-test:** in a single 60-min sitting, implement from blank: euclidean + KMeans + train/test split + evaluate cluster quality (inertia). If you finish, you're ready for Phase 3.

---

## Phase 3 — End-to-end pipelines (Days 15–21)

Goal: practice combining primitives under time pressure. **This phase is where the interview is won.**

### Day 15 — Sun 2026-06-07 — Event store with time-range queries
- [ ] **Build:** `EventStore` class with `log(event_type, timestamp)` and `count(event_type, t_start, t_end)`.
- [ ] First version: store sorted by timestamp, use `bisect` for range queries — O(log n) per query.
- [ ] Then: handle **out-of-order inserts** (sorted insert via `bisect.insort`, O(n) — discuss the trade-off).
- [ ] Extension: support `top_k_event_types_in_window(t_start, t_end, k)` — count + heap.
- [ ] **Discuss out loud:** at 100M events, what would you change? (Bucketed time buckets, sharding by event_type, persistent storage like a TSDB.)

### Day 16 — Mon 2026-06-08 — Recommender system v1
- [ ] **Build:** ingest `(user_id, item_id, rating)` events → for any user, return top-K items they haven't seen.
- [ ] Approach 1: item popularity (global top-K, minus seen items).
- [ ] Approach 2: simple collaborative filtering — find users similar to U (cosine on rating vectors), aggregate their top items.
- [ ] Use the primitives from Days 8 + 10.
- [ ] **Self-test:** seed with 5 users × 10 items, manually verify top-3 makes sense.

### Day 17 — Tue 2026-06-09 — Streaming / online clustering
- [ ] **Build:** `OnlineKMeans` — `update(point)` adjusts the nearest centroid with a learning rate; `predict(point)` returns cluster id.
- [ ] Bonus: handle "cold start" (first K points become initial centroids).
- [ ] Compare batch K-Means (Day 9) vs. online — when does each win?
- [ ] **Production lens (say out loud):** drift handling, decay weights, when to re-init.

### Day 18 — Wed 2026-06-10 — TIMED MOCK #1 ⏱ (60 min, strict)
- [ ] **Prompt (do NOT read in advance — have a friend or just commit cold):** "Design a system that ingests `(user_id, item_id, timestamp)` view events. Support: (1) top-K most-viewed items in the last hour, (2) recommend top-K items to a user based on similar users (collaborative). Optimize for repeated queries."
- [ ] Set a 60-min timer. Use CoderPad or a blank file. No reference material except a one-page Python idioms sheet.
- [ ] Talk out loud the whole time (record yourself if possible — review later).
- [ ] After the timer: write 5 bullets — what worked, what stalled, what idiom you fumbled.

### Day 19 — Thu 2026-06-11 — Mock #1 retrospective + fix weakest part
- [ ] Re-read your Mock #1 code. Refactor for clarity (rename, modularize). Add the tests you skipped.
- [ ] Re-implement the **one component that stalled you** from blank, under 15 min.
- [ ] Re-read the staff-level habits list at the top. Note which ones you violated.

### Day 20 — Fri 2026-06-12 — TIMED MOCK #2 ⏱ (60 min, strict)
- [ ] **Prompt:** "Build a weighted item sampler: given items with scores, draw N samples without replacement. Then: scores decay over time (multiply by 0.95 every minute since last view). Then: support adding new items mid-stream."
- [ ] Same rules as Mock #1.

### Day 21 — Sat 2026-06-13 — Mock #2 retro + code-quality refactor
- [ ] Re-read your Mock #2 code with fresh eyes. Pretend you're the interviewer scoring on the rubric. Where would you score 2 vs 3 vs 4?
- [ ] Refactor to push every component to "3" or higher.
- [ ] **Self-grade** on the 0–4 rubric from the PDF.

---

## Phase 4 — Polish & final mocks (Days 22–25)

### Day 22 — Sun 2026-06-14 — TIMED MOCK #3 ⏱ (60 min)
- [ ] **Prompt:** "Implement K-Means clustering on user feature vectors. Then: assign incoming users to clusters in real-time. Then: every 100 new users, retrain centroids. Report cluster sizes."
- [ ] After: 10-min retro.

### Day 23 — Mon 2026-06-15 — Speed drills (blank-file implementations)
- [ ] In one 75-min block, implement from a blank file, untimed individually:
  - [ ] K-Means (target: 20 min)
  - [ ] KNN classifier (target: 15 min)
  - [ ] Weighted sampler (target: 10 min)
  - [ ] Event store with time-window count (target: 15 min)
  - [ ] Train/test split + accuracy metric (target: 10 min)
- [ ] If any goes over target, schedule a 20-min revisit on Day 24.

### Day 24 — Tue 2026-06-16 — Targeted gaps + verbal practice
- [ ] Address the one or two pieces that ran over on Day 23.
- [ ] **Verbal practice:** out loud, explain to an imaginary interviewer how K-Means works, and how you'd handle the case where K is unknown (elbow method, silhouette). 5 min, no slides.
- [ ] Re-read the staff-level habits list. Re-read the PDF's evaluation rubric.

### Day 25 — Wed 2026-06-17 — Light review + rest ⭐
- [ ] **Light** only. Skim your cheat sheet, scan Mock #3 code. **No new problems.**
- [ ] Set up CoderPad practice pad, confirm camera/screen-share works.
- [ ] Sleep 8 hours. Caffeine plan for tomorrow.

### Day 26 — Thu 2026-06-18 — Interview day
- [ ] Eat. Hydrate. 10-min walk before.
- [ ] **First 3 min: clarify.** Don't code yet.
- [ ] **Minutes 3–20: working pipeline.** Even if dumb, get it running end-to-end.
- [ ] **Minutes 20–50: layer features + tests.**
- [ ] **Minutes 50–60: discuss scale, extensions, trade-offs.**
- [ ] You've got this.

---

## Reference resources (pick by need, don't try to read everything)

- **Python idioms:** `python -c "import this"`, `collections` docs, `bisect` docs, `heapq` docs.
- **DSA refresh:** NeetCode 150 (filter to Easy/Medium on arrays, hashing, binary search, sliding window, heap).
- **Weighted sampling specifically:** LeetCode 528 (Random Pick with Weight), 398 (Random Pick Index), 382 (Linked List Random Node) — all directly relevant.
- **ML from scratch:** "ML Algorithms from Scratch" by Jason Brownlee (skim KMeans, KNN, LR posts).
- **Skip:** anything theory-heavy this round (CNNs, transformers, RLHF) — that's for the *other* interview.

---

## Tracking notes

Use the space below to jot per-day reflections (1–2 lines max). Patterns here are gold for Day 24.

- Day 1 (done 2026-05-25, one day late): Two Sum was the rough spot — 16 min vs 5 min target because the hash-map pattern wasn't reflexive; drilled to 5× clean reps. Group Anagrams (15/10 min) surfaced the lists/sets-aren't-hashable rule. Contains Duplicate came in under budget (2/3 min) — pattern transfer working. Valid Anagram was the biggest *learning*: shipped `set(s) == set(t)`, which passed the file's asserts but is wrong (`"aab" vs "abb"` → True). Lesson banked: **invent your own counter-tests before declaring done.** `Counter`/`defaultdict` are explicitly Day 2 and were already wanted today.
- Day 2:
- Day 3:
- ...
