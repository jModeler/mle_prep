# Day 2 — `collections` module

**Date:** Mon 2026-05-25 (per plan; shift to your actual day if running late)
**Time budget:** ~2 hours
**Goal:** Internalize `Counter`, `defaultdict`, `deque`, `OrderedDict` — the four utilities you'll reach for on every event-store, top-K, and BFS problem from Day 4 onwards.

---

## Why this day matters

Day 1 was the four core containers. Today is the **purpose-built dict subclasses and queue** that sit on top of them. Every theme in the Tubi coding round (event stores, weighted sampling, recommendations) uses at least one of today's tools — usually two. By the end of today, the question "should I use `dict.get(k, 0) + 1` or `Counter`?" should not exist; you reach for `Counter` reflexively.

Day 1's Valid Anagram bug — `set(s) == set(t)` instead of multiset equality — is the exact thing `Counter` was made for: `Counter(s) == Counter(t)` is the one-line correct answer. Today closes that loop.

---

## How to use this folder

1. **Skim** `../SOLVING_TIPS.md` if you haven't read it recently (one-page habit reminders).
2. **Read** `concept_brief.md` (~20 min). One-page reference for the four utilities.
3. **Optional deeper dive:** `deep_dive.md` builds the *why* from first principles — when each tool is best, when it isn't, and the templates (BFS, sliding window, LRU) you should memorize.
4. **Solve** the problems in `problems.md`, in order, against the clock. Each starter file has a timer target at the top.
5. **Self-test** at the end (`self_test_event_stream.py`) — under 3 minutes, no lookups.
6. Add a 1–2 line reflection to `reflection.md`.

---

## How to resume in a new session (for Claude)

Tell the new session:

> Review my Day 2 solutions in `prep_days/day_2/`. Read `problems.md` for the spec and timer targets, then read each `*.py` solution and give me feedback. Focus on: (1) correctness, (2) did I reach for the right `collections` tool, (3) hit timer target, (4) one staff-level habit to drill on Day 3.

Then point it at `Memory/INDEX.md` and `PREP_PLAN.md` for context.

---

## Files

- `README.md` — this file
- `concept_brief.md` — quick reference (idioms + complexity)
- `deep_dive.md` — first-principles "textbook"
- `problems.md` — problem statements + timer targets
- `top_k_frequent.py` — starter (target: 7 min)
- `first_unique_character.py` — starter (target: 4 min)
- `design_hashmap.py` — starter (target: 15 min)
- `self_test_event_stream.py` — starter (target: 3 min, no lookups)
- `reflection.md` — fill in after, 1–2 lines max
