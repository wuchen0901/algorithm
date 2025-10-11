from typing import List


# Flood Fill DFS Template with Return Value
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            if not (0 <= i < rows and 0 <= j < cols):
                return 0

            if grid[i][j] == 0:
                return 0

            # Mark cell as visited
            grid[i][j] = 0

            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
