"""
Design HashMap — Day 2, Problem 3
Target time: 15 min
Actual time: ___

Constraints: do NOT use dict, set, Counter, or any other built-in hash-table type.
Use a list of buckets with chaining.

Clarifying questions (write 2–3 BEFORE coding):
- ?
- ?
- ?
"""


class MyHashMap:
    def __init__(self):
        # your code here
        ...

    def put(self, key: int, value: int) -> None:
        # insert or update
        ...

    def get(self, key: int) -> int:
        # return -1 if key not found
        ...

    def remove(self, key: int) -> None:
        # no-op if key not present
        ...


if __name__ == "__main__":
    m = MyHashMap()

    m.put(1, 1)
    m.put(2, 2)
    assert m.get(1) == 1
    assert m.get(3) == -1

    m.put(2, 1)  # update
    assert m.get(2) == 1

    m.remove(2)
    assert m.get(2) == -1

    # Collision-friendly: many keys, small bucket count exercise
    for i in range(100):
        m.put(i, i * 10)
    for i in range(100):
        assert m.get(i) == i * 10
    for i in range(0, 100, 2):
        m.remove(i)
    for i in range(100):
        assert m.get(i) == (-1 if i % 2 == 0 else i * 10)

    print("ok")
