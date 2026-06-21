# Mock #2 — Cold

**⚠️ Do not read past the line below until the clock starts.**

Solo time-keeping: 60-min countdown + count-up stopwatch. Record at the top of `mock_2_solution.py`.

---

## Prompt

Design a **weighted item sampler** with time decay and mid-stream additions.

You're given items, each with a current score. Implement:

1. **`add_item(item_id, score)`** — register a new item and its initial score. New items can be added at any time and are eligible for sampling immediately.

2. **`view_item(item_id, timestamp)`** — record a view. Used to track when the score should decay from.

3. **`sample(now, n)`** — draw `n` items **without replacement**, with each item's probability proportional to its current *decayed* score.

**Decay rule:** every minute since `last_view_time`, the score is multiplied by `0.95`. Compute the decayed score at the moment `sample` is called.

## Constraints

- Python 3, stdlib only (`collections`, `bisect`, `heapq`, `random`, `math`).
- One file: `mock_2_solution.py`.

## What good looks like

- A class or set of functions with clear responsibilities (`add_item`, `view_item`, `sample`).
- Test as you build — each method with a small example.
- One trade-off mentioned out loud or in a comment (recompute decay on each sample vs. cache vs. lazy).
- A one-line note on what would change at 100M items.

## What "complete" means

A working end-to-end version, even one that recomputes decay on every sample call, is far more valuable than a polished half. Get something running on a 5-item dataset first. Optimize after.

Talk out loud. Claude is your interviewer — quiet unless you ask a clarifying Q.
