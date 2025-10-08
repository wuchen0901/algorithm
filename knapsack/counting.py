"""Counting variants for knapsack problems (0-1 and unbounded)."""

from collections import Counter, defaultdict
from typing import Dict, List


def knapsack_count_ways(weights: List[int], capacity: int) -> int:
    """0-1 knapsack: number of subsets that sum exactly to ``capacity``."""
    dp = [0] * (capacity + 1)
    dp[0] = 1
    for w in weights:
        for total in range(capacity, w - 1, -1):
            dp[total] += dp[total - w]
    return dp[capacity]


def complete_knapsack_count_ways(weights: List[int], capacity: int) -> int:
    """Unbounded knapsack combinations (order-insensitive)."""
    ws = sorted({w for w in weights if 1 <= w <= capacity})
    dp = [0] * (capacity + 1)
    dp[0] = 1
    for w in ws:
        for total in range(w, capacity + 1):
            dp[total] += dp[total - w]
    return dp[capacity]


def complete_knapsack_count_permutations(weights: List[int], capacity: int) -> int:
    """Unbounded knapsack permutations (order-sensitive)."""
    ws = sorted({w for w in weights if 1 <= w <= capacity})
    dp = [0] * (capacity + 1)
    dp[0] = 1
    for total in range(1, capacity + 1):
        for w in ws:
            if total >= w:
                dp[total] += dp[total - w]
    return dp[capacity]


def count_ordered_sums_unbounded(nums: List[int], target: int) -> int:
    """Unbounded permutations counted by sequence length progression."""
    if not nums:
        return 0
    filtered = [n for n in nums if n > 0 and n <= target]
    if not filtered:
        return 0
    max_len = target // min(filtered)
    curr = Counter({0: 1})
    cumulative = Counter(curr)
    for _ in range(1, max_len + 1):
        next_counter = Counter()
        for total, ways in curr.items():
            for n in filtered:
                next_counter[total + n] += ways
        cumulative += next_counter
        curr = next_counter
        if not curr:
            break
    return cumulative[target]


def count_combinations_unbounded_v1(nums: List[int], target: int) -> int:
    if target == 0:
        return 1
    filtered = [n for n in nums if n > 0 and n <= target]
    if not filtered:
        return 0
    max_len = target // min(filtered)
    curr: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
    for n in filtered:
        curr[n][n] = 1
    cumulative = Counter()
    for total, last_to_ways in curr.items():
        cumulative[total] = sum(last_to_ways.values())
    for _ in range(2, max_len + 1):
        next_counter: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
        for total, last_to_ways in curr.items():
            for last, ways in last_to_ways.items():
                for n in filtered:
                    if n <= last:
                        next_counter[total + n][n] += ways
        if not next_counter:
            break
        for total, buckets in next_counter.items():
            cumulative[total] += sum(buckets.values())
        curr = next_counter
    return cumulative[target]


def count_combinations_unbounded_v3(nums: List[int], target: int) -> int:
    nums = [n for n in nums if n > 0 and n <= target]
    nums.sort()
    res = 0
    def backtrack(curr_sum: int, start: int) -> None:
        nonlocal res
        if curr_sum >= target:
            if curr_sum == target:
                res += 1
            return
        for i in range(start, len(nums)):
            backtrack(curr_sum + nums[i], i)
    backtrack(0, 0)
    return res


def count_combinations_unbounded_v4(nums: List[int], target: int) -> int:
    if target == 0:
        return 1
    nums = [n for n in nums if n > 0 and n <= target]
    nums.sort()
    n = len(nums)
    dp: List[List[int]] = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for c in range(1, n + 1):
        for total in range(target + 1):
            dp[c][total] = dp[c - 1][total]
            if total - nums[c - 1] >= 0:
                dp[c][total] += dp[c][total - nums[c - 1]]
    return dp[n][target]


def count_combinations_unbounded_v5(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for x in nums:
        if x <= 0:
            continue
        for total in range(x, target + 1):
            dp[total] += dp[total - x]
    return dp[target]


__all__ = [
    "knapsack_count_ways",
    "complete_knapsack_count_ways",
    "complete_knapsack_count_permutations",
    "count_ordered_sums_unbounded",
    "count_combinations_unbounded_v1",
    "count_combinations_unbounded_v3",
    "count_combinations_unbounded_v4",
    "count_combinations_unbounded_v5",
]
