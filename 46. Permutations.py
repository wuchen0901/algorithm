from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def dfs(path, remaining):
            if not remaining:
                permutations.append(path.copy())
                return

            for n in remaining:
                path.append(n)
                rest = remaining.copy()
                rest.remove(n)
                dfs(path, rest)
                path.pop()

        dfs([], nums)

        return permutations
