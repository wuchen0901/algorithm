"""Classic value-maximizing knapsack solvers (0-1 variants)."""

from functools import lru_cache
from typing import Dict, List, Tuple


def knapsack_combination(weights: List[int], values: List[int], capacity: int) -> int:
    """Backtracking that explores combinations (items used at most once)."""
    n = len(weights)
    max_value = 0
    def backtrack(curr_weight: int, curr_value: int, start: int) -> None:
        nonlocal max_value
        if curr_weight > capacity:
            return
        max_value = max(max_value, curr_value)
        for idx in range(start, n):
            backtrack(curr_weight + weights[idx], curr_value + values[idx], idx + 1)
    backtrack(0, 0, 0)
    return max_value


def knapsack_backtrack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """Backtracking with explicit choose/skip branching."""
    n = len(weights)
    max_value = 0
    def backtrack(curr_weight: int, curr_value: int, index: int) -> None:
        nonlocal max_value
        if curr_weight > capacity:
            return
        if index == n:
            max_value = max(max_value, curr_value)
            return
        backtrack(curr_weight + weights[index], curr_value + values[index], index + 1)
        backtrack(curr_weight, curr_value, index + 1)
    backtrack(0, 0, 0)
    return max_value


def knapsack_memo_lru_cache(weights: List[int], values: List[int], capacity: int) -> int:
    """Top-down DP using ``functools.lru_cache``."""
    n = len(weights)
    @lru_cache(maxsize=None)
    def dp(index: int, remaining: int) -> int:
        if index == n:
            return 0
        not_take = dp(index + 1, remaining)
        take = 0
        if weights[index] <= remaining:
            take = values[index] + dp(index + 1, remaining - weights[index])
        return max(take, not_take)
    return dp(0, capacity)


def knapsack_memo_manual(weights: List[int], values: List[int], capacity: int) -> int:
    """Top-down DP with an explicit memo dictionary."""
    n = len(weights)
    memo: Dict[Tuple[int, int], int] = {}
    def dp(index: int, remaining: int) -> int:
        if index == n:
            return 0
        key = (index, remaining)
        if key in memo:
            return memo[key]
        not_take = dp(index + 1, remaining)
        take = 0
        if weights[index] <= remaining:
            take = values[index] + dp(index + 1, remaining - weights[index])
        memo[key] = max(take, not_take)
        return memo[key]
    return dp(0, capacity)


def knapsack_dp_2d(weights: List[int], values: List[int], capacity: int) -> int:
    """Classic 2-D bottom-up DP solution."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(capacity + 1):
            if weights[i - 1] <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - weights[i - 1]] + values[i - 1])
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[n][capacity]


def knapsack_dp_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """1-D space-optimized bottom-up DP."""
    dp = [0] * (capacity + 1)
    for i, w in enumerate(weights):
        v = values[i]
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]


def knapsack_v1(weights: List[int], values: List[int], capacity: int) -> int:
    """Legacy 2-D DP implementation kept for compatibility."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for item in range(1, n + 1):
        weight = weights[item - 1]
        value = values[item - 1]
        for cap in range(capacity + 1):
            dp[item][cap] = dp[item - 1][cap]
            if cap >= weight:
                dp[item][cap] = max(dp[item][cap], dp[item][cap - weight] + value)
    return dp[n][capacity]


__all__ = [
    "knapsack_combination",
    "knapsack_backtrack_optimized",
    "knapsack_memo_lru_cache",
    "knapsack_memo_manual",
    "knapsack_dp_2d",
    "knapsack_dp_optimized",
    "knapsack_v1",
]
