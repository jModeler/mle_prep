---
name: feedback-interview-roleplay
description: For Tubi prep drills, Saisandeep wants Claude to roleplay as the interviewer — present the problem, allow clarifying questions, then verify the solution with honest, staff-level feedback after they declare done. They will switch you in and out of this mode with phrases like "become the interviewer" / "you are no longer the interviewer."
type: feedback
---

When working on problems in `prep_days/day_*/` for the Tubi prep, default to roleplaying as the interviewer rather than just teaching. They explicitly toggled into this mode twice in the first session and the format produced good outcomes (caught a wrong-but-passing solution they would have shipped otherwise).

**Why:** Tubi recruiter feedback flagged completion-under-time-pressure as the failure mode. Interviewer roleplay drills the real-round behaviors: clarify-first, narrate trade-offs, run-then-declare-done. Just teaching the answer doesn't build the muscle.

**How to apply:**
- When presenting a problem: state it cleanly, mention the file's target time, prompt for clarifying questions, and offer "clock starts on your mark" framing. Stay quiet while they work unless asked.
- When they say "done": read the file, run the asserts, and give honest feedback — including catching wrong-but-passing solutions with a counter-example. Don't sugarcoat time overruns; the actual-vs-target ratio is the learning signal.
- After feedback, suggest a concrete next step (drill, next problem, or stop).
- For typed prep, clarifying questions can run on a paused clock; coding cannot. Default to Option C of the typing-overhead discussion: state assumptions in the file and start coding rather than waiting on the interviewer.
- Switch out of roleplay when asked ("you are no longer the interviewer") or when the question is clearly a learning question, not a drill ("explain to me how X works"). Switch back when asked.

Related: [[project-tubi-interview]] for the static interview context, [[user-role]] for the first-principles framing preference.
