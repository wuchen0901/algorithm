"""Feasibility checks for 0-1 and unbounded knapsack variants."""

from typing import List


def knapsack_can_fill_01(weights: List[int], capacity: int) -> bool:
    """
    0-1 knapsack feasibility: can we select items (each at most once)
    whose weights sum exactly to ``capacity``?
    """
    dp = [False] * (capacity + 1)
    dp[0] = True
    for w in weights:
        for total in range(capacity, w - 1, -1):
            dp[total] = dp[total] or dp[total - w]
    return dp[capacity]


def knapsack_can_fill_unbounded(nums: List[int], target: int) -> bool:
    """Unbounded knapsack feasibility: can we reuse items to hit ``target`` exactly?"""
    if not nums:
        return False
    filtered = [n for n in nums if n > 0 and n <= target]
    if not filtered:
        return False
    reachable = {0}
    max_count = target // min(filtered)
    for _ in range(1, max_count + 1):
        next_reachable = {s + n for n in filtered for s in reachable if s + n <= target}
        if target in next_reachable:
            return True
        reachable = next_reachable
        if not reachable:
            break
    return False


def knapsack_can_fill_unbounded_v2(nums: List[int], target: int) -> bool:
    """
    Unbounded knapsack feasibility: can we reuse items to hit `target` exactly?
    Assumes all nums[i] > 0. Negative or zero weights are invalid.
    """
    if not nums:
        return False

    l = len(nums)
    dp = [[0 for _ in range(target + 1)] for _ in range(l + 1)]
    for i in range(1, l + 1):
        num = nums[i - 1]
        for used_capacity in range(target + 1):
            dp[i][used_capacity] = dp[i - 1][used_capacity]
            if 0 <= used_capacity - num:
                dp[i][used_capacity] = max(dp[i][used_capacity], dp[i][used_capacity - num] + num)

    return dp[l][target] == target


print("knapsack_can_fill_unbounded_v2", knapsack_can_fill_unbounded_v2([9, 5, 17], 30))


def knapsack_min_items(weights: List[int], capacity: int) -> int:
    """Minimum number of items (0-1) needed to reach ``capacity`` exactly; ``-1`` if impossible."""
    INF = float("inf")
    dp = [INF] * (capacity + 1)
    dp[0] = 0
    for w in weights:
        for total in range(capacity, w - 1, -1):
            if dp[total - w] != INF:
                dp[total] = min(dp[total], dp[total - w] + 1)
    return dp[capacity] if dp[capacity] != INF else -1


__all__ = [
    "knapsack_can_fill_01",
    "knapsack_can_fill_unbounded",
    "knapsack_min_items",
]
