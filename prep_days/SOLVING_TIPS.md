# Solving tips (applies to every day)

Practical guidance for working through timed problems alone. Read once, then it's just habit.

---

## How to time yourself

Use **two timers in parallel**, mimicking the real interview:

1. **Phone stopwatch** — counts up. Start when you finish reading the problem, stop when tests pass. Record actual time in the file header.
2. **Countdown timer set to the problem's target** — beeps when you're at the limit. Tells you when to stop rat-holing and wrap up.

This dual-timer habit is exactly what you'll do in the real interview: a clock for "where am I" and a soft alarm for "time to move on."

### What NOT to use

- `time python file.py` — that's execution time, not solve time. Different thing.
- A timer that lives in the same window as your code — context-switch tax. Keep it physical (phone) or in a separate window.

### What to record

Put two lines at the top of every `.py` file before you start:

```
Target time: 5 min
Actual time: ___
```

Fill in `Actual time` when tests pass. The gap (target vs actual) is the data you'll use for Day 24's targeted-gap review.

---

## Clarifying questions when there's no interviewer

In a real interview you'd ask the interviewer. Solo, the muscle you're building is *the reflex of pausing to ask* — not the answers themselves. Write the questions as a comment block at the top of the file **before** coding, then make reasonable assumptions and state them.

```python
# Clarifying Qs:
# - Integers only, or floats too?       → assuming ints
# - Negative numbers allowed?           → assuming yes
# - Exactly one solution guaranteed?    → yes (per problem)
# - Return indices in any order?        → assuming smaller index first
```

The credit is the comment block existing, not the answers being clever. If the comment block isn't there before code, you skipped the habit — that's the failure mode to catch.

### When to escalate to "Claude as interviewer"

Spinning up a Claude session to play interviewer is heavyweight (more tokens, more friction) — only worth it when the spec is genuinely open-ended.

| Phase                 | Clarify mode                                              |
| --------------------- | --------------------------------------------------------- |
| 1 — DSA foundations   | Write Qs in comments, self-answer. Specs are tight.       |
| 2 — ML primitives     | Same — specs are tight.                                   |
| 3 — End-to-end mocks  | **Spin up Claude as interviewer.** Open-ended prompts.    |
| 4 — Polish & mocks    | Claude as interviewer + strict 60-min timer.              |

When you do open a Claude session for interviewer-mode, the prompt should be:

> Play interviewer for this prompt: <paste>. Answer only what I ask. Don't volunteer information. Don't grade until I say I'm done.

That keeps it adversarially honest — same as a real interviewer.

---

## Testing as you go (the other habit that wins time)

After every function, run it with one hand-crafted example. **Don't** write 40 lines then debug — the bug surface is too big to triage in 60 min.

Pattern:

```python
def featurize(events):
    ...

if __name__ == "__main__":
    print(featurize([("u1", "a"), ("u1", "b")]))   # expect: {"u1": ["a","b"]}
```

Then write the next function. Then test. Then the next. The starter files already have an `if __name__ == "__main__"` block with assertions — use it as you build, not just at the end.

---

## Where to find this

This file lives at `prep_days/SOLVING_TIPS.md`. Linked from every day's `README.md`. Re-read on Day 1; refer back when something feels off.
