from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(i: int, j: int):
            # 🚫 越界停止递归
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            # 遇到水，停止递归
            if grid[i][j] == '0':
                return

            # 遇到陆地
            if grid[i][j] == '1':
                # ✅ 标记为访问过（淹没这块陆地）
                grid[i][j] = '0'

            # 🔁 递归访问四个方向
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)

        return island_count
