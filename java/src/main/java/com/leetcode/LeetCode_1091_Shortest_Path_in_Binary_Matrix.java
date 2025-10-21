package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class LeetCode_1091_Shortest_Path_in_Binary_Matrix {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
        if (n == 1) return 1;

        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0});
        grid[0][0] = 1;

        int[][] directions = {
                {1, 0}, {-1, 0}, {0, 1}, {0, -1},
                {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
        };

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int row = curr[0], col = curr[1];
            int dist = grid[row][col];

            for (int[] dir : directions) {
                int nr = row + dir[0], nc = col + dir[1];
                if (0 <= nr && nr < n && 0 <= nc && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = dist + 1;
                    if (nr == n - 1 && nc == n - 1) return grid[nr][nc];
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
        return -1;
    }
}
