"""
Drill: KNN classifier from scratch.

Target: 15 min
Actual: ___

Implement knn_classify(X_train, y_train, x_query, k):
    Returns the predicted class label (majority vote among k nearest neighbors).

Use Euclidean distance.
Tiebreak ties in vote count by lower-class-label (deterministic).
Assume 1 <= k <= len(X_train), and all training points have the same dimensionality.
"""

import math
from collections import Counter


def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def knn_classify(X_train, y_train, x_query, k):
    # Your code here.
    pass


if __name__ == "__main__":
    X = [
        [0, 0], [0, 1], [1, 0],            # class 0
        [10, 10], [10, 11], [11, 10],      # class 1
    ]
    y = [0, 0, 0, 1, 1, 1]

    # Query close to class 0
    assert knn_classify(X, y, [0.5, 0.5], k=3) == 0

    # Query close to class 1
    assert knn_classify(X, y, [10, 10.5], k=3) == 1

    # k=1 just picks nearest
    assert knn_classify(X, y, [0, 0.1], k=1) == 0
    assert knn_classify(X, y, [10, 10.1], k=1) == 1

    # k=6 (all data) — balanced 3-3, tiebreak to lower label (0)
    assert knn_classify(X, y, [5, 5], k=6) == 0

    # 3-class case
    X3 = [[0, 0], [0, 1], [10, 10], [10, 11], [20, 20], [20, 21]]
    y3 = [0, 0, 1, 1, 2, 2]
    assert knn_classify(X3, y3, [0, 0.5], k=2) == 0
    assert knn_classify(X3, y3, [10, 10.5], k=2) == 1
    assert knn_classify(X3, y3, [20, 20.5], k=2) == 2

    print("all tests passed")
