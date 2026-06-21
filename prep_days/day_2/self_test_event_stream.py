"""
Self-test — Top event types in a stream
Day 2, Self-test
Target time: 3 min  —  NO LOOKUPS, NO CONCEPT BRIEF, NO DOCS

Actual time: ___
"""


def top_event_types(events: list[str], k: int = 3) -> list[str]:
    # your code here
    ...


if __name__ == "__main__":
    # Unique counts to avoid tiebreak ambiguity in tests
    events = ["a", "b", "a", "c", "a", "b", "c", "c", "c"]
    # counts: c=4, a=3, b=2

    assert top_event_types(events, k=3) == ["c", "a", "b"]
    assert top_event_types(events, k=2) == ["c", "a"]
    assert top_event_types(events, k=1) == ["c"]
    assert top_event_types([], k=3) == []

    # Default k=3
    assert top_event_types(events) == ["c", "a", "b"]

    print("ok")
