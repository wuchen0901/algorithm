package com.leetcode;

public class LeetCode_695_Max_Area_of_Island {

    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    maxArea = Math.max(maxArea, islandArea(grid, i, j));
                }
            }
        }
        return maxArea;
    }

    int islandArea(int[][] grid, int r, int c) {
        if (grid[r][c] == 0) {
            return 0;
        }

        grid[r][c] = 0;

        int[][] directions = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        int sum = 1;
        for (int[] direction : directions) {
            int dr = direction[0];
            int dc = direction[1];
            if (0 <= r + dr && r + dr < grid.length && 0 <= c + dc && c + dc < grid[r + dr].length) {
                sum += islandArea(grid, r + dr, c + dc);
            }
        }

        return sum;
    }
}
