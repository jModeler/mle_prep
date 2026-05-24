"""
Self-test — User → Items
Day 1, Self-test
Target time: 5 min  —  NO LOOKUPS, NO CONCEPT BRIEF, NO DOCS

Actual time: ___
"""


def user_items(events: list[tuple[str, str]]) -> dict[str, set[str]]:
    # your code here
    ...


if __name__ == "__main__":
    assert user_items([("u1", "a"), ("u2", "b"), ("u1", "a"), ("u1", "c")]) == {
        "u1": {"a", "c"},
        "u2": {"b"},
    }
    assert user_items([]) == {}
    assert user_items([("u1", "a")]) == {"u1": {"a"}}
    print("ok")
