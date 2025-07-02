from typing import List


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
def knapsack_backtrack(weights: List[int], values: List[int], capacity: int) -> int:
    max_value = 0

    def backtrack(path: List[int], index: int):
        nonlocal max_value
        # Prune
        if capacity < sum(weights[i] for i in path):
            return

        # Should I put it here? No — because path is still incomplete (not all choices made).
        # max_value = max(max_value, sum(values[i] for i in path))

        # Choose/skip backtracking ends here.
        if index == len(weights):
            # This is the correct place to evaluate max_value — path is complete.
            max_value = max(max_value, sum(values[i] for i in path))
            return

        backtrack(path, index + 1)

        path.append(index)
        backtrack(path, index + 1)
        path.pop()

    backtrack([], 0)
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
