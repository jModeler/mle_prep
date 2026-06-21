"""
Drill: K-Means clustering from scratch (pure Python).

Target: 20 min
Actual: ___

Implement kmeans(points, k, max_iter=100, tol=1e-4):
    Returns (centroids, assignments):
        centroids: list of k cluster centers, each a list of floats with dim D
        assignments: list of length n, each in {0, ..., k-1}

Algorithm:
1. Initialize k centroids by picking k random points from the input (use random.sample).
2. Assign each point to the nearest centroid (Euclidean distance).
3. Recompute each centroid as the mean of its assigned points.
4. Repeat until total centroid movement < tol, or max_iter reached.

Edge cases:
- An empty cluster after assignment: re-initialize that centroid to a random point.
- All points identical: converges in one iteration.

Caller is responsible for setting random.seed() if reproducibility is needed.
"""

import math
import random


def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def kmeans(points, k, max_iter=100, tol=1e-4):
    # Your code here.
    pass


if __name__ == "__main__":
    # 3 well-separated 2D clusters
    points = [
        [0, 0], [0.1, 0.1], [0, 0.2],          # cluster A around origin
        [10, 10], [10.1, 10], [10, 10.2],      # cluster B around (10, 10)
        [-5, 5], [-5.1, 5], [-5, 5.2],         # cluster C around (-5, 5)
    ]

    # Retry a few seeds to dodge unlucky inits
    found_three_clusters = False
    for seed in [1, 2, 3, 4, 5]:
        random.seed(seed)
        centroids, assignments = kmeans(points, k=3)

        # Hand-crafted invariants
        in_cluster = (
            assignments[0] == assignments[1] == assignments[2]
            and assignments[3] == assignments[4] == assignments[5]
            and assignments[6] == assignments[7] == assignments[8]
        )
        three_distinct = len(set(assignments)) == 3
        if in_cluster and three_distinct:
            found_three_clusters = True
            break
    assert found_three_clusters, "could not recover 3 clusters across 5 seeds"

    # k=1 — everything in one cluster
    random.seed(0)
    centroids, assignments = kmeans(points, k=1)
    assert all(a == 0 for a in assignments)
    # Centroid should be the mean of all points
    mean_x = sum(p[0] for p in points) / len(points)
    mean_y = sum(p[1] for p in points) / len(points)
    assert abs(centroids[0][0] - mean_x) < 1e-6
    assert abs(centroids[0][1] - mean_y) < 1e-6

    # Identical points — converge immediately
    pts = [[1, 1]] * 5
    random.seed(0)
    centroids, assignments = kmeans(pts, k=1)
    assert abs(centroids[0][0] - 1.0) < 1e-9
    assert abs(centroids[0][1] - 1.0) < 1e-9

    print("all tests passed")
