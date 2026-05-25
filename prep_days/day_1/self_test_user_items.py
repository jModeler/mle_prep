"""
Self-test — User → Items
Day 1, Self-test
Target time: 5 min  —  NO LOOKUPS, NO CONCEPT BRIEF, NO DOCS

Actual time: ___
"""


def user_items(events: list[tuple[str, str]]) -> dict[str, set[str]]:
    # create an empty dictionary
    result = {}
    # cycle through the list of tuples
    for user, item in events:
        if user not in result:
            result[user] = set() # initialize set of items for new user
        result[user].add(item)

    return result



if __name__ == "__main__":
    assert user_items([("u1", "a"), ("u2", "b"), ("u1", "a"), ("u1", "c")]) == {
        "u1": {"a", "c"},
        "u2": {"b"},
    }
    assert user_items([]) == {}
    assert user_items([("u1", "a")]) == {"u1": {"a"}}
    print("ok")
