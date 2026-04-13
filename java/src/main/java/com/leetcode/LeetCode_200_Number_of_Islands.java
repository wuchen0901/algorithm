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

    public int numIslandsBFS(char[][] grid) {
        int islandCount = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    islandCount++;
                    bfs(grid, i, j);
                }
            }
        }
        return islandCount;
    }

    private void bfs(char[][] grid, int i, int j) {
        java.util.Queue<int[]> queue = new java.util.ArrayDeque<>();
        queue.offer(new int[]{i, j});
        grid[i][j] = '0';

        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int u = cell[0];
            int v = cell[1];

            for (int[] ints : dirs) {
                int x = u + ints[0];
                int y = v + ints[1];

                if (0 <= x && x < grid.length && 0 <= y && y < grid[x].length) {
                    if (grid[x][y] == '1') {
                        grid[x][y] = '0';
                        queue.offer(new int[]{x, y});
                    }
                }
            }
        }
    }
}
