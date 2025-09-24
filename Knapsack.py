from collections import defaultdict
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


# === Problem Type 3: Count the number of ways to fill the knapsack ===


# Version 1: Number of ways to fill the knapsack exactly (Count solutions)
def knapsack_count_ways(weights: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    dp[0] = 1
    for w in weights:
        for j in range(capacity, w - 1, -1):
            dp[j] += dp[j - w]
    return dp[capacity]


# Version 2: Number of ways (Complete/Unbounded Knapsack) — combinations (order DOES NOT matter)
def complete_knapsack_count_ways(weights: List[int], capacity: int) -> int:
    """
    Count combinations to reach exactly `capacity` using unlimited copies of each weight.
    Order does NOT matter: [1,2,2] and [2,1,2] are the same.
    """
    # sanitize: remove non-positive and duplicates, and clip to capacity
    ws = sorted({w for w in weights if 1 <= w <= capacity})
    dp = [0] * (capacity + 1)
    dp[0] = 1
    for w in ws:
        for c in range(w, capacity + 1):
            dp[c] += dp[c - w]
    return dp[capacity]


# Version 3: Number of ways (Complete/Unbounded Knapsack) — permutations (order DOES matter)
def complete_knapsack_count_permutations(weights: List[int], capacity: int) -> int:
    """
    Count permutations to reach exactly `capacity` using unlimited copies of each weight.
    Order DOES matter: [1,2,2] and [2,1,2] are different.
    """
    ws = sorted({w for w in weights if 1 <= w <= capacity})
    dp = [0] * (capacity + 1)
    dp[0] = 1
    for c in range(1, capacity + 1):
        for w in ws:
            if c >= w:
                dp[c] += dp[c - w]
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


#
# Unbounded Knapsack Problem
def can_reach_unbounded(nums: List[int], target: int) -> bool:
    max_count = target // min(nums)

    reachable = {0}
    for count in range(1, max_count + 1):
        reachable = {s + num for num in nums for s in reachable if s + num <= target}

        if target in reachable:
            return True

    return False


from collections import defaultdict
from typing import List, Dict


def count_ordered_sums_unbounded(nums: List[int], target: int) -> int:
    """
    Count the number of ORDERED sequences (permutations with repetition allowed)
    drawn from `nums` that sum to `target`, where sequence length is between 1
    and floor(target / min(nums)). This is intentionally order-sensitive:
    e.g., with nums=[1,2], target=3, the sequences [1,2] and [2,1] are distinct.

    Note: This matches a permutation-style counting (LC 377 style if you iterate over sums),
    but here we advance by sequence length layers and accumulate across lengths.
    """

    max_len = target // min(nums)  # maximum sequence length allowed by smallest number

    # Counts for sequences of EXACT length = 1: sum -> ways
    curr_len_counts: Dict[int, int] = defaultdict(int)
    for x in nums:
        curr_len_counts[x] = 1

    cumulative_counts = curr_len_counts.copy()

    # Grow sequences by length: 2 .. max_len
    for _len in range(2, max_len + 1):
        next_len_counts: Dict[int, int] = defaultdict(int)
        for sum_so_far, ways in curr_len_counts.items():
            for x in nums:
                next_len_counts[sum_so_far + x] += ways

        # accumulate counts across lengths (still ORDER-sensitive)
        for s, w in next_len_counts.items():
            cumulative_counts[s] += w

        curr_len_counts = next_len_counts

    return cumulative_counts[target]


print("count_ordered_sums: ", count_ordered_sums_unbounded([1, 2], 3))


def count_combinations_unbounded(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for x in nums:  # iterate items
        for s in range(x, target + 1):  # go UP for unbounded
            dp[s] += dp[s - x]
    return dp[target]


print("count_combinations_unbounded: ", count_combinations_unbounded([1, 2], 3))
