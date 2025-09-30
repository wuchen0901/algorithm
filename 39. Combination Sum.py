from typing import List


class Solution:
    # Unbounded Knapsack – Enumeration Problems
    def combinationSum_v1(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(curr: List[int], start: int):
            curr_sum = sum(curr)
            if target < curr_sum:
                return
            if target == curr_sum:
                res.append(curr[:])
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(curr, i)
                curr.pop()

        backtrack([], 0)

        return res

    def combinationSum_v2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(curr: List[int], curr_sum: int, start: int):
            if target < curr_sum:
                return
            if target == curr_sum:
                res.append(curr[:])
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                curr_sum += candidates[i]
                backtrack(curr, curr_sum, i)
                curr.pop()
                curr_sum -= candidates[i]

        backtrack([], 0, 0)

        return res
