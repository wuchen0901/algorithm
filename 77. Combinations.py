from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        collections = [i + 1 for i in range(n)]

        def backtrack(path, start):
            if len(path) == k:
                combinations.append(path.copy())
                return

            for i in range(start, len(collections)):
                path.append(collections[i])
                backtrack(path, i + 1)
                path.pop()

        combinations = []
        backtrack([], 0)
        return combinations
