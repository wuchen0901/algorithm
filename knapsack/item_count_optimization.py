"""Optimize the number of items selected under knapsack-style constraints."""

from math import inf
from typing import Iterable, List


def _sanitize_weights(weights: Iterable[int], capacity: int) -> List[int]:
    """Filter out non-positive weights and those exceeding capacity."""
    if capacity <= 0:
        return []
    return [w for w in weights if 1 <= w <= capacity]


def knapsack_max_items_01(weights: Iterable[int], capacity: int) -> int:
    """
    0-1 knapsack: maximum number of items that can be packed without
    exceeding ``capacity``. Returns 0 if no positive-weight items fit.
    """
    valid = _sanitize_weights(weights, capacity)
    if not valid:
        return 0
    dp = [-inf] * (capacity + 1)
    dp[0] = 0
    for weight in valid:
        for total in range(capacity, weight - 1, -1):
            if dp[total - weight] != -inf:
                dp[total] = max(dp[total], dp[total - weight] + 1)
    best = max((count for count in dp if count >= 0), default=0)
    return int(best)


def knapsack_max_items_unbounded(weights: Iterable[int], capacity: int) -> int:
    """
    Unbounded knapsack: maximum item count with unlimited copies per item
    without exceeding ``capacity``. Returns 0 if no feasible packing exists.
    """
    valid = _sanitize_weights(weights, capacity)
    if not valid:
        return 0
    dp = [-inf] * (capacity + 1)
    dp[0] = 0
    for weight in valid:
        for total in range(weight, capacity + 1):
            if dp[total - weight] != -inf:
                dp[total] = max(dp[total], dp[total - weight] + 1)
    best = max((count for count in dp if count >= 0), default=0)
    return int(best)


def knapsack_min_items_01(weights: Iterable[int], target: int) -> int:
    """
    0-1 knapsack: minimum number of items needed to hit ``target`` exactly.
    Returns ``-1`` if no combination matches the target weight.
    """
    valid = _sanitize_weights(weights, target)
    if target == 0:
        return 0
    if not valid:
        return -1
    dp = [inf] * (target + 1)
    dp[0] = 0
    for weight in valid:
        for total in range(target, weight - 1, -1):
            if dp[total - weight] != inf:
                dp[total] = min(dp[total], dp[total - weight] + 1)
    return int(dp[target]) if dp[target] != inf else -1


def knapsack_min_items_unbounded(weights: Iterable[int], target: int) -> int:
    """
    Unbounded knapsack: minimum number of items needed to reach ``target`` exactly.
    Returns ``-1`` if ``target`` cannot be formed.
    """
    valid = _sanitize_weights(weights, target)
    if target == 0:
        return 0
    if not valid:
        return -1
    dp = [inf] * (target + 1)
    dp[0] = 0
    for weight in valid:
        for total in range(weight, target + 1):
            if dp[total - weight] != inf:
                dp[total] = min(dp[total], dp[total - weight] + 1)
    return int(dp[target]) if dp[target] != inf else -1


# 2D DP version of unbounded knapsack for minimum number of items to reach target
def knapsack_min_items_unbounded_2d(weights: Iterable[int], target: int) -> int:
    """
    Unbounded knapsack: 2D DP version.
    Minimum number of items needed to reach ``target`` exactly.
    Returns ``-1`` if ``target`` cannot be formed.
    """
    valid = _sanitize_weights(weights, target)
    if target == 0:
        return 0
    if not valid:
        return -1

    n = len(valid)
    dp = [[inf] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        w = valid[i - 1]
        for t in range(target + 1):
            dp[i][t] = dp[i - 1][t]
            if t >= w and dp[i][t - w] != inf:
                dp[i][t] = min(dp[i][t], dp[i][t - w] + 1)

    return int(dp[n][target]) if dp[n][target] != inf else -1


__all__ = [
    "knapsack_max_items_01",
    "knapsack_max_items_unbounded",
    "knapsack_min_items_01",
    "knapsack_min_items_unbounded",
    "knapsack_min_items_unbounded_2d",
]
