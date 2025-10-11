"""Enumeration helpers for knapsack-style search problems."""

from typing import List


def knapsack_find_all_subsets(weights: List[int], capacity: int) -> List[List[int]]:
    """List every subset of ``weights`` (0-1) that sums exactly to ``capacity``."""
    result: List[List[int]] = []
    def backtrack(index: int, curr: List[int], total: int) -> None:
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


def count_combinations_unbounded_v2(nums: List[int], target: int) -> int:
    """Backtracking enumeration for unbounded combinations; returns the count of valid lists."""
    nums = [n for n in nums if n > 0 and n <= target]
    nums.sort()
    res: List[List[int]] = []
    def backtrack(curr: List[int], curr_sum: int, start: int) -> None:
        if curr_sum >= target:
            if curr_sum == target:
                res.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(curr, curr_sum + nums[i], i)
            curr.pop()
    backtrack([], 0, 0)
    return len(res)


__all__ = ["knapsack_find_all_subsets", "count_combinations_unbounded_v2"]
