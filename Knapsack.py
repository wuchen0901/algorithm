from collections import defaultdict
from typing import List, Counter, Dict


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
    类型：完全背包 · 排列计数（顺序敏感，等价“有序组合”/ compositions）。
    典型特征：外层按 sum 或长度推进会计入不同顺序；[1,2] 与 [2,1] 视为两种。
    Type: Unbounded Knapsack · Permutation counting (order-sensitive, equivalent to compositions).
    Typical characteristic: Outer loop by sum or length includes different orders; [1,2] and [2,1] are treated as two distinct ways.
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
    """
    类型：完全背包 · 可行性判定（是否存在解）。
    典型特征：元素可重复使用；只需判断能否恰好达到 target；顺序是否去重不影响结论。
    Type: Unbounded Knapsack · Feasibility check (existence).
    Typical characteristic: Elements can be reused unlimited times; only need to check if target can be exactly reached; order or deduplication does not affect the result.
    """
    max_count = target // min(nums)

    reachable = {0}
    for count in range(1, max_count + 1):
        reachable = {s + num for num in nums for s in reachable if s + num <= target}

        if target in reachable:
            return True

    return False


def count_ordered_sums_unbounded(nums: List[int], target: int) -> int:
    """
    Count the number of ORDERED sequences (permutations with repetition allowed)
    drawn from `nums` that sum to `target`, where sequence length is between 1
    and floor(target / min(nums)). This is intentionally order-sensitive:
    e.g., with nums=[1,2], target=3, the sequences [1,2] and [2,1] are distinct.
    类型：完全背包 · 排列计数（顺序敏感，等价“有序组合”/ compositions）。
    典型特征：外层按 sum 或长度推进会计入不同顺序；[1,2] 与 [2,1] 视为两种。
    Type: Unbounded Knapsack · Permutation counting (order-sensitive, equivalent to compositions).
    Typical characteristic: Outer loop by sum or length includes different orders; [1,2] and [2,1] are treated as two distinct ways.
    """

    max_len = target // min(nums)  # maximum sequence length allowed by smallest number

    curr = Counter({0: 1})
    cumulative = Counter(curr)

    for _len in range(1, max_len + 1):
        next_counter = Counter()
        for s, ways in curr.items():
            for n in nums:
                next_counter[s + n] += ways

        cumulative += next_counter
        curr = next_counter

    return cumulative[target]


print("count_ordered_sums: ", count_ordered_sums_unbounded([1, 2], 3))


def count_combinations_unbounded_v1(nums: List[int], target: int) -> int:
    if target == 0:
        return 1
    max_len = target // min(nums)

    curr: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
    for n in nums:
        curr[n][n] = 1

    cumulative = Counter()

    for s, last_element_to_ways in curr.items():
        cumulative[s] = sum(last_element_to_ways.values())

    for _len in range(2, max_len + 1):
        next_counter: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
        for s, last_element_to_ways in curr.items():
            for last_element, ways in last_element_to_ways.items():
                for n in nums:
                    if n <= last_element:
                        next_counter[s + n][n] += ways

        if not next_counter:
            break

        for k, v in next_counter.items():
            cumulative[k] += sum(v.values())

        curr = next_counter

    return cumulative[target]


print("count_combinations_unbounded_v1: ", count_combinations_unbounded_v1([1, 2, 5], 5))


def count_combinations_unbounded_v2(nums: List[int], target: int) -> int:
    nums.sort()
    res = []

    def backtrack(curr: List[int], curr_sum: int, start: int):
        if target <= curr_sum:
            if target == curr_sum:
                res.append(curr[:])
            return

        for i in range(start, len(nums)):
            curr.append(nums[i])
            curr_sum += nums[i]
            backtrack(curr, curr_sum, i)
            curr.pop()
            curr_sum -= nums[i]

    backtrack([], 0, 0)

    return len(res)


print("count_combinations_unbounded_v2: ", count_combinations_unbounded_v2([1, 2, 5], 5))


def count_combinations_unbounded_v3(nums: List[int], target: int) -> int:
    nums.sort()
    res = 0

    def backtrack(curr_sum: int, start: int):
        nonlocal res
        if target <= curr_sum:
            if target == curr_sum:
                res += 1
            return

        for i in range(start, len(nums)):
            curr_sum += nums[i]
            backtrack(curr_sum, i)
            curr_sum -= nums[i]

    backtrack(0, 0)

    return res


print("count_combinations_unbounded_v3: ", count_combinations_unbounded_v3([1, 2, 5], 5))


def count_combinations_unbounded_v4(nums: List[int], target: int) -> int:
    if target == 0:
        return 1

    nums.sort()
    n = len(nums)
    dp: List[List[int]] = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0] = 1

    #     coin\sum      0   1   2   3   4   5   6   7
    #   nums[0]:[]      1   0
    #   nums[1]:[1]     1   1   1   1   1   1   1   1
    #   nums[2]:[1, 3]  1   1   1   2   2   2   3   3
    # 1 + 3 + 3
    # 1 + 1 + 1 + 1 + 3
    # 1 + 1 + 1 + 1 + 1 + 1 + 1
    for c in range(1, n + 1):
        for s in range(target + 1):
            dp[c][s] = dp[c - 1][s]
            # dp[1][0] = dp[0][0]
            # dp[1][7] = dp[0][7]
            if 0 <= s - nums[c - 1]:
                dp[c][s] += dp[c][s - nums[c - 1]]
                # dp[1][1] += dp[1][0]
                # dp[1][7] += dp[1][6]
                # c = 1, s = target, dp[1][7 - 1]:1

    return dp[n][target]


print("count_combinations_unbounded_v4: ", count_combinations_unbounded_v4([1, 2, 7], 30))


def count_combinations_unbounded_v5(nums: List[int], target: int) -> int:
    """
    类型：完全背包 · 组合计数（顺序不敏感，去重）。
    典型特征：外层遍历物品、内层容量递增；[1,2,2] 与 [2,1,2]只算一种。
    Type: Unbounded Knapsack · Combination counting (order-insensitive, deduplicated).
    Typical characteristic: Outer loop iterates items, inner loop increases capacity; [1,2,2] and [2,1,2] count as one way.
    """
    dp = [0] * (target + 1)
    dp[0] = 1
    for x in nums:  # iterate items
        for s in range(x, target + 1):  # go UP for unbounded
            dp[s] += dp[s - x]
    return dp[target]


print("count_combinations_unbounded_v5: ", count_combinations_unbounded_v5([1, 2, 7], 30))

from typing import List


def knapsack_v1(weights: List[int], values: List[int], W: int) -> int:
    """
    weights: list of item weights
    values:  list of item values
    W:       maximum capacity of the knapsack
    return:  maximum achievable total value
    """
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for item in range(1, n + 1):
        for capacity in range(1, W + 1):
            dp[item][capacity] = max(dp[item - 1][capacity],
                                     (dp[item][capacity - weights[item - 1]] + values[item - 1]) if 0 <= capacity -
                                                                                                    weights[
                                                                                                        item - 1]
                                     else 0)
    return dp[n][W]
    # weight: 3 5 1 2
    # value : 4 2 3 1
    # W     : 8
    # 0 1 2 3 4   5 6 7 8
    #
    # 0 0 0 0 0
    # 0 0 0 4 4   4  8  8  8
    # 0 0 0 4 4   4  8  8  8
    # 0 3 6 9 12 15 18 21 24
