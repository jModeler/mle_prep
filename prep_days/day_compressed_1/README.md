# Day Compressed 1 — Sun 2026-06-21

**Interview:** Tue 2026-06-23 (coding round)
**Active mode:** concept reading → drills → Mock #2.

## State

Mock #1 (Day 18 prompt) was cut short after 15 min — three real gaps surfaced before the 60-min ran out:

1. Filtering massive event data without scanning everything → **bisect over sorted timestamps**.
2. Leveraging `Counter` reflexively for top-K.
3. Collaborative filtering from scratch.

(1) and (2) collapse into one technique. (3) is its own primer.

## Pass bar reminder (from the PDF rubric)

Aim for **≥2 (Acceptable)** on every core component — not 4 on one and 0 on the rest. Rubric explicitly names: **working solution, binary search ideas where relevant, testing.** Assumption-stating and trade-off narration are also graded.

## Today's drill sequence

For each row: read the concept (if any), then attempt the drill from the blank function body. Tests are in each `.py` file — run as you build.

| # | Concept (read first) | Drill | Target | What it builds |
|---|---|---|---:|---|
| 1 | `concept_bisect.md` | `drill_bisect.py` | 5 min | binary search on sorted timestamps |
| 2 | `concept_counter.md` | `drill_counter.py` | 10 min | top-K via bisect + Counter (the Mock #1 unlock) |
| 3 | `concept_collaborative_filtering.md` | `drill_collaborative_filtering.py` | 25 min | user-user CF with Jaccard |
| 4 | (your ML knowledge) | `drill_distance.py` | 15 min | dot / norm / euclidean / manhattan / cosine |
| 5 | (your ML knowledge) | `drill_weighted_sampler.py` | 15 min | prefix-sum + bisect sampling (preview of Mock #2) |
| 6 | (your ML knowledge) | `drill_knn.py` | 15 min | majority-vote classifier |
| 7 | (your ML knowledge) | `drill_kmeans.py` | 20 min | from-scratch clustering |

**Total target:** ~105 min focused work + breaks. Push to evening if needed.

## Mock #2 — after the drills

When you've cleared the drills (or hit a stopping point you're happy with):

- `MOCK_2_PROMPT.md` (sealed — don't peek until clock starts)
- `mock_2_solution.py` (stub with assumption block)

Same protocol: 60-min strict, think out loud, Claude as interviewer.

## Rules

- Allowed: stdlib only — `collections`, `bisect`, `heapq`, `random`, `math`. Google for syntax. **No LLMs.**
- Don't peek at MOCK_2_PROMPT.md until the clock starts.
- For each drill: read concept → pause 30 sec ("how would I approach this?") → attempt blank function → run tests.
- If a drill blows past target by 2× and you're stuck, ask for a hint. Don't grind silently.

## Self-score after each drill (0–4)

| Drill | Time vs target | Score | Notes |
|---|---|---|---|
| bisect | | | |
| counter | | | |
| collaborative_filtering | | | |
| distance | | | |
| weighted_sampler | | | |
| knn | | | |
| kmeans | | | |
| Mock #2 | | | |

## After-action

Update `Memory/progress.md` at end of session with what landed cleanly vs. what needs another rep tomorrow.
