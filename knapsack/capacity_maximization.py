"""Maximize used capacity (weight) for 0-1 and unbounded knapsack."""

from typing import List


def knapsack_capacity_max_01(weights: List[int], capacity: int) -> int:
    """Maximum total weight not exceeding ``capacity`` when each item is used at most once."""
    dp = [0] * (capacity + 1)
    for w in weights:
        if w <= 0 or w > capacity:
            continue
        for total in range(capacity, w - 1, -1):
            dp[total] = max(dp[total], dp[total - w] + w)
    return max(dp)


def knapsack_capacity_max_01(weights: List[int], capacity: int) -> int:
    """Maximum total weight not exceeding ``capacity`` when each item is used at most once."""
    l = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(l + 1)]
    # w: 3 2 4
    #     0  1  2  3  4  5
    # dp  0
    # dp  0        3
    # dp  0     2  3     5
    # dp  0     2  3  4  5
    for i in range(1, l + 1):
        weight = weights[i - 1]
        for c in range(capacity, weight - 1, -1):
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - weight] + weight)

    return dp[l][capacity]


def knapsack_capacity_max_unbounded(weights: List[int], capacity: int) -> int:
    """Maximum total weight not exceeding ``capacity`` with unlimited copies of each item."""
    dp = [0] * (capacity + 1)
    for w in weights:
        if w <= 0 or w > capacity:
            continue
        for total in range(w, capacity + 1):
            dp[total] = max(dp[total], dp[total - w] + w)
    return max(dp)


__all__ = ["knapsack_capacity_max_01", "knapsack_capacity_max_unbounded"]
