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

# combination-style backtracking
def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    num_items = len(weights)
    max_value = 0

    def backtrack(start: int, total_weight: int, total_value: int):
        nonlocal max_value
        if total_weight > capacity:
            return

        max_value = max(max_value, total_value)

        for i in range(start, num_items):
            backtrack(i + 1, total_weight + weights[i], total_value + values[i])

    backtrack(0, 0, 0)
    return max_value


# choose/skip-style backtracking
def knapsack_backtrack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    max_value = 0

    def backtrack(index: int, total_weight: int, total_value: int):
        nonlocal max_value
        # Capacity Validation
        if capacity < total_weight:
            return

        # Choose/skip backtracking ends here.
        if index == len(weights):
            max_value = max(max_value, total_value)
            return

        backtrack(index + 1, total_weight, total_value)

        backtrack(index + 1, total_weight + weights[index], total_value + values[index])

    backtrack(0, 0, 0)
    return max_value


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    result = knapsack_backtrack_optimized(weights, values, capacity)
    print("Maximum value:", result)  # Expected output: 4


# memoized recursion (top-down DP) using lru_cache
def knapsack_memo_lru_cache(weights: List[int], values: List[int], capacity: int) -> int:
    from functools import lru_cache

    n = len(weights)

    @lru_cache(maxsize=None)
    def dp(index: int, remaining_capacity: int) -> int:
        if index == n:
            return 0

        # Option 1: skip this item
        not_take = dp(index + 1, remaining_capacity)

        # Option 2: take this item if it fits
        take = 0
        if weights[index] <= remaining_capacity:
            take = values[index] + dp(index + 1, remaining_capacity - weights[index])

        return max(take, not_take)

    return dp(0, capacity)


# memoized recursion (top-down DP) using manual dictionary
def knapsack_memo_manual(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    memo = {}

    def dp(index: int, remaining_capacity: int) -> int:
        if index == n:
            return 0
        if (index, remaining_capacity) in memo:
            return memo[(index, remaining_capacity)]

        # Option 1: skip this item
        not_take = dp(index + 1, remaining_capacity)

        # Option 2: take this item if it fits
        take = 0
        if weights[index] <= remaining_capacity:
            take = values[index] + dp(index + 1, remaining_capacity - weights[index])

        memo[(index, remaining_capacity)] = max(take, not_take)
        return memo[(index, remaining_capacity)]

    return dp(0, capacity)


# bottom-up DP (tabulation)
def knapsack_dp_table(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]  # can't take item i-1
            else:
                dp[i][j] = max(
                    dp[i - 1][j],  # don't take item
                    dp[i - 1][j - weights[i - 1]] + values[i - 1]  # take item
                )

    return dp[n][capacity]


# bottom-up DP with 1D array (space optimized)

def knapsack_dp_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[capacity]


# === Problem Type 3: Count the number of ways to fill the knapsack ===

# Version 3: Number of ways to fill the knapsack exactly (Count solutions)
def knapsack_count_ways(weights: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    dp[0] = 1
    for w in weights:
        for j in range(capacity, w - 1, -1):
            dp[j] += dp[j - w]
    return dp[capacity]


# === Problem Type 4: Find all valid subsets that sum to exactly capacity ===

# Version 4: Return all valid subsets that sum to exactly capacity
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

# Version 5: Minimum number of items needed to reach exactly the target
def knapsack_min_items(weights: List[int], capacity: int) -> int:
    INF = float('inf')
    dp = [INF] * (capacity + 1)
    dp[0] = 0
    for w in weights:
        for j in range(capacity, w - 1, -1):
            if dp[j - w] != INF:
                dp[j] = min(dp[j], dp[j - w] + 1)
    return dp[capacity] if dp[capacity] != INF else -1
