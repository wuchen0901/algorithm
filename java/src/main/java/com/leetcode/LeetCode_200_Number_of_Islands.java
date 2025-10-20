package com.leetcode;

public class LeetCode_200_Number_of_Islands {
    public int numIslands(char[][] grid) {
        int numberOfIslands = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    numberOfIslands++;
                }
            }
        }

        return numberOfIslands;
    }

    private void dfs(char[][] grid, int i, int j) {
        if (i < 0 || grid.length <= i || j < 0 || grid[i].length <= j) {
            return;
        }

        if (grid[i][j] == '0') {
            return;
        }

        grid[i][j] = '0';

        dfs(grid, i - 1, j);
        dfs(grid, i + 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
    }
}
