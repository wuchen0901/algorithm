from typing import List


# === Problem Type 1: Can we exactly fill the knapsack? ===

# Version 1: Can we exactly fill the knapsack? (Boolean)
def knapsack_can_fill(weights: List[int], capacity: int) -> bool:
    dp = [False] * (capacity + 1)
    dp[0] = True
    for w in weights:
        for j in range(capacity, w - 1, -1):
            dp[j] = dp[j] or dp[j - w]
    return dp[capacity]


# === Problem Type 2: Maximize value (0/1 Knapsack standard) ===

# Version 1: combination-style backtracking
def knapsack_combination(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    max_value = 0

    def backtrack(current_weight, current_value, start):
        nonlocal max_value

        if capacity < current_weight:
            return

        max_value = max(max_value, current_value)

        for i in range(start, n):
            backtrack(current_weight + weights[i], current_value + values[i], i + 1)

    backtrack(0, 0, 0)
    return max_value


# Version 2: choose/skip-style backtracking
def knapsack_backtrack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    max_value = 0

    def backtrack(current_weight, current_value, i):
        nonlocal max_value
        if capacity < current_weight:
            return

        if i == n:
            max_value = max(max_value, current_value)
            return

        backtrack(current_weight + weights[i], current_value + values[i], i + 1)
        backtrack(current_weight, current_value, i + 1)

    backtrack(0, 0, 0)
    return max_value


# Version 3: Top-down DP with lru_cache
def knapsack_memo_lru_cache(weights: List[int], values: List[int], capacity: int) -> int:
    from functools import lru_cache
    n = len(weights)

    @lru_cache(maxsize=None)
    def dp(index: int, remaining_capacity: int) -> int:
        if index == n:
            return 0
        not_take = dp(index + 1, remaining_capacity)
        take = 0
        if weights[index] <= remaining_capacity:
            take = values[index] + dp(index + 1, remaining_capacity - weights[index])
        return max(take, not_take)

    return dp(0, capacity)


# Version 4: Top-down DP with manual memoization
def knapsack_memo_manual(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    memo = {}

    def dp(index: int, remaining_capacity: int) -> int:
        if index == n:
            return 0
        if (index, remaining_capacity) in memo:
            return memo[(index, remaining_capacity)]
        not_take = dp(index + 1, remaining_capacity)
        take = 0
        if weights[index] <= remaining_capacity:
            take = values[index] + dp(index + 1, remaining_capacity - weights[index])
        memo[(index, remaining_capacity)] = max(take, not_take)
        return memo[(index, remaining_capacity)]

    return dp(0, capacity)


# Version 5: Bottom-up DP (2D DP Table)
def knapsack_dp_2d(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(capacity + 1):
            if weights[i - 1] <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - weights[i - 1]] + values[i - 1])
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[n][capacity]


# Version 6: Bottom-up DP (1D space optimized)
def knapsack_dp_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[capacity]


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    result = knapsack_backtrack_optimized(weights, values, capacity)
    print("Maximum value:", result)  # Expected output: 4


# === Problem Type 3: Count the number of ways to fill the knapsack ===

# Version 1: Number of ways to fill the knapsack exactly (Count solutions)
def knapsack_count_ways(weights: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    dp[0] = 1
    for w in weights:
        for j in range(capacity, w - 1, -1):
            dp[j] += dp[j - w]
    return dp[capacity]


# === Problem Type 4: Find all valid subsets that sum to exactly capacity ===

# Version 1: Return all valid subsets that sum to exactly capacity
def knapsack_find_all_subsets(weights: List[int], capacity: int) -> List[List[int]]:
    result = []

    def backtrack(index: int, curr: List[int], total: int):
        if total > capacity:
            return
        if index == len(weights):
            if total == capacity:
                result.append(curr[:])
            return
        backtrack(index + 1, curr, total)
        curr.append(weights[index])
        backtrack(index + 1, curr, total + weights[index])
        curr.pop()

    backtrack(0, [], 0)
    return result


# === Problem Type 5: Minimum number of items to exactly reach capacity ===

# Version 1: Minimum number of items needed to reach exactly the target
def knapsack_min_items(weights: List[int], capacity: int) -> int:
    INF = float('inf')
    dp = [INF] * (capacity + 1)
    dp[0] = 0
    for w in weights:
        for j in range(capacity, w - 1, -1):
            if dp[j - w] != INF:
                dp[j] = min(dp[j], dp[j - w] + 1)
    return dp[capacity] if dp[capacity] != INF else -1


# Complete Knapsack Problem
def canSum(nums: List[int], target: int) -> bool:
    max_count = target // min(nums)

    reachable = {0}
    for count in range(1, max_count + 1):
        reachable = {s + num for num in nums for s in reachable if s + num <= target}

        if target in reachable:
            return True

    return False
