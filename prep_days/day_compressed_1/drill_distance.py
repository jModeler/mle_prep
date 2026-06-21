"""
Drill: vector distance / similarity metrics from scratch (pure Python).

Target: 15 min total (all five)
Actual: ___

Implement:
- dot(a, b)       — dot product
- norm(a)         — L2 norm: sqrt(sum of squares)
- euclidean(a, b) — sqrt(sum of squared differences)
- manhattan(a, b) — sum of absolute differences
- cosine(a, b)    — dot(a, b) / (norm(a) * norm(b))

Edge cases:
- Raise ValueError if vectors are different lengths.
- Cosine on a zero vector: return 0.0 (no defined direction).
"""

import math


def dot(a, b):
    pass


def norm(a):
    pass


def euclidean(a, b):
    pass


def manhattan(a, b):
    pass


def cosine(a, b):
    pass


if __name__ == "__main__":
    # dot
    assert dot([1, 2, 3], [4, 5, 6]) == 32
    assert dot([0, 0], [1, 1]) == 0
    assert dot([-1, 2], [3, -4]) == -11

    # norm
    assert abs(norm([3, 4]) - 5.0) < 1e-9
    assert norm([0, 0, 0]) == 0
    assert abs(norm([1, 1, 1]) - math.sqrt(3)) < 1e-9

    # euclidean
    assert abs(euclidean([0, 0], [3, 4]) - 5.0) < 1e-9
    assert euclidean([1, 1], [1, 1]) == 0

    # manhattan
    assert manhattan([0, 0], [3, 4]) == 7
    assert manhattan([1, 2, 3], [1, 2, 3]) == 0
    assert manhattan([-1, -1], [1, 1]) == 4

    # cosine
    assert abs(cosine([1, 0], [1, 0]) - 1.0) < 1e-9       # identical direction
    assert abs(cosine([1, 0], [0, 1]) - 0.0) < 1e-9       # perpendicular
    assert abs(cosine([1, 0], [-1, 0]) - (-1.0)) < 1e-9   # opposite
    assert cosine([0, 0], [1, 1]) == 0.0                  # zero vector — return 0
    assert cosine([1, 1], [0, 0]) == 0.0                  # zero vector other side

    # length mismatch — should raise
    for f in (dot, euclidean, manhattan, cosine):
        try:
            f([1, 2], [1, 2, 3])
            assert False, f"{f.__name__} should raise ValueError on length mismatch"
        except ValueError:
            pass

    print("all tests passed")
