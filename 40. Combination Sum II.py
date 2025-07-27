from bisect import bisect_right
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def backtrack(path, curr_sum, start):
            if target == curr_sum:
                combinations.append(path.copy())
                return

            if target < curr_sum:
                return

            if start == len(candidates):
                return

            i = start

            while i < len(candidates):
                path.append(candidates[i])
                backtrack(path, curr_sum + candidates[i], i + 1)
                path.pop()
                i = bisect_right(candidates, candidates[i], i)

        backtrack([], 0, 0)

        return combinations
