from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # grid = [
        #   ["1","1","1","1","0"],
        #   ["1","1","0","1","0"],
        #   ["1","1","0","0","0"],
        #   ["0","0","0","0","0"]
        # ]

        def dfs(row: int, i: int):
            if not (0 <= row < len(grid) and 0 <= i < len(grid[row])):
                return

            if grid[row][i] == "0":
                return

            grid[row][i] = "0"

            dfs(row - 1, i)
            dfs(row + 1, i)
            dfs(row, i - 1)
            dfs(row, i + 1)

        number = 0
        # Iterate over the grid
        for row in range(len(grid)):  # 0 1 2 3
            for i in range(len(grid[row])):  # 0 1 2 3 4
                if grid[row][i] == "1":
                    number += 1
                    # DFS from here to mark every "1" to "0"
                    dfs(row, i)

        return number
