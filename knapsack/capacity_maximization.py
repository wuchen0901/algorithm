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
