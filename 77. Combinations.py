from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]) -> None:
            if len(path) == k:
                result.append(path[:])
                return
            # 剪枝：i 最大只能到 n - (k - len(path)) + 1
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result