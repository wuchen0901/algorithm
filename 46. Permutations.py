from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack([], nums, result)
        return result

    def backtrack(self, path, remaining, result):
        if not remaining:
            result.append(path.copy())
            return

        for i in remaining:
            next_remaining = remaining.copy()
            next_remaining.remove(i)
            path.append(i)
            self.backtrack(path, next_remaining, result)
            path.pop()
