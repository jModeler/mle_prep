"""
Drill: user-user collaborative filtering from scratch.

Target: 25 min
Actual: ___

Implement Jaccard similarity and a user-user recommender.

Function signatures:

build_user_items(events): events is a list of (user_id, item_id) tuples.
                          Returns dict of user_id -> set of items.

jaccard(set_a, set_b): returns float in [0, 1]. Zero on empty inputs.

recommend(target_user, user_items, k, n_similar=10):
    Returns list of up to k item_ids, sorted by recommendation score descending.

    Scoring:
        - For each user other than target, compute Jaccard with target.
        - Keep only users with similarity > 0.
        - Take top n_similar (by sim, desc).
        - For each candidate item (in their set, not in target's set), accumulate sim.
        - Return top-k items by accumulated score.

    Cold-start case: if target has no overlap with anyone (all sims = 0), return [].
"""

from collections import defaultdict


def build_user_items(events):
    # Your code here.
    pass


def jaccard(a, b):
    # Your code here.
    pass


def recommend(target_user, user_items, k, n_similar=10):
    # Your code here.
    pass


if __name__ == "__main__":
    # --- build_user_items ---
    events = [
        ("u1", "a"), ("u1", "b"),
        ("u2", "a"), ("u2", "c"),
        ("u3", "b"), ("u3", "d"),
    ]
    user_items = build_user_items(events)
    assert user_items["u1"] == {"a", "b"}
    assert user_items["u2"] == {"a", "c"}
    assert user_items["u3"] == {"b", "d"}

    # --- jaccard ---
    assert jaccard({"a", "b"}, {"a", "b"}) == 1.0
    assert jaccard({"a"}, {"b"}) == 0.0
    assert jaccard(set(), {"a"}) == 0.0
    assert abs(jaccard({"a", "b", "c"}, {"a", "b", "d"}) - 2 / 4) < 1e-9

    # --- recommend ---
    # target u1 = {a, b}
    # u2 = {a, b, c, d}    sim = 2/4 = 0.5    contributes c (0.5), d (0.5)
    # u3 = {a, b, e}       sim = 2/3 ≈ 0.67   contributes e (0.67)
    # u4 = {x, y}          sim = 0            contributes nothing
    user_items = {
        "u1": {"a", "b"},
        "u2": {"a", "b", "c", "d"},
        "u3": {"a", "b", "e"},
        "u4": {"x", "y"},
    }
    recs = recommend("u1", user_items, k=3)
    assert len(recs) == 3, f"expected 3 recs, got {recs}"
    assert recs[0] == "e", f"highest score should be 'e', got {recs}"
    assert set(recs) == {"e", "c", "d"}, f"got {recs}"

    # Cold start — target has no overlap with anyone
    cold = {
        "u1": {"a"},
        "u2": {"b"},
        "u3": {"c"},
    }
    assert recommend("u1", cold, k=3) == []

    # k larger than available candidates → returns whatever is available
    recs = recommend("u1", user_items, k=100)
    assert len(recs) == 3, f"got {recs}"

    # Exclude items the target already has
    excl = {
        "u1": {"a", "b"},
        "u2": {"a", "b"},  # sim=1, but all items already in target's set
    }
    assert recommend("u1", excl, k=5) == []

    # n_similar caps neighborhood — only the top n_similar users contribute
    # Setup: u1={a}. u2={a,X} sim=0.5. u3={a,Y} sim=0.5. u4={a,Z} sim=0.5.
    # n_similar=1 → only top-1 user contributes → only ONE of X/Y/Z appears.
    cap = {
        "u1": {"a"},
        "u2": {"a", "X"},
        "u3": {"a", "Y"},
        "u4": {"a", "Z"},
    }
    recs = recommend("u1", cap, k=5, n_similar=1)
    assert len(recs) == 1, f"n_similar=1 should yield 1 candidate item, got {recs}"
    assert recs[0] in {"X", "Y", "Z"}

    print("all tests passed")
