# Mock #1 — Cold

**⚠️ Do not read past the line below until the clock starts.**

Solo time-keeping: start a 60-min countdown + a count-up stopwatch the moment you start reading the prompt. Record `Target: 60 min` and `Actual: ___` at the top of `mock_1_solution.py`.

---

## Prompt

Design a system that ingests view events of the form `(user_id, item_id, timestamp)`.

Support two queries:

1. **`top_k_items_last_hour(k, now)`** — return the K most-viewed items in the hour preceding `now`.
2. **`recommend(user_id, k)`** — return top-K items for this user based on **users similar to them** (collaborative). "Similar" is up to you to define; justify your choice.

**Optimize for repeated queries.** Assume queries happen far more often than ingests over the long run.

## Constraints / what you have

- Python 3, stdlib only: `collections`, `bisect`, `heapq`, `random`, `math`.
- No ML frameworks. No numpy.
- One file: `mock_1_solution.py`.

## What good looks like (don't peek at this until you're done — it's the rubric)

- A clarifying-Qs / assumptions block at the top of the file (4 lines is enough).
- Modular functions: `ingest`, `top_k_items_last_hour`, `recommend`, plus any helpers.
- At least one test per public function in `if __name__ == "__main__":` — run as you build, not at the end.
- Trade-off mentioned somewhere (in code comments OR out loud): why this data layout vs. an alternative.
- A one-line note on what would change at 100M events (sharding, persistent store, bucketed time).

## What "complete" means here

A working end-to-end version, even a dumb one, is **far** more valuable than a polished half. Get something running on a 5-row hand-crafted dataset first. Optimize after.

Talk out loud the whole time. Claude is your interviewer — quiet unless you ask a clarifying Q.
