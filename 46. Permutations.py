from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        visited = [False] * n

        def backtrack(path: List[int]):
            if len(path) == n:
                result.append(path.copy())
                return

            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                visited[i] = False

        backtrack([])
        return result