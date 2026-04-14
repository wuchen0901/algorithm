package com.leetcode;

import java.util.ArrayDeque;
import java.util.Queue;

public class LeetCode_994_Rotting_Oranges {
    public int orangesRotting(int[][] grid) {
        Queue<int[]> queue = new ArrayDeque<>();

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        int[][] dirs = new int[][]{
                {0, 1},
                {0, -1},
                {1, 0},
                {-1, 0},
        };

        int minutes = 0; // is this varible name valid?

        while (!queue.isEmpty()) {
            int size = queue.size();
            boolean spread = false;
            for (int s = 0; s < size; s++) {
                int[] rottenOrange = queue.poll();
                int u = rottenOrange[0];
                int v = rottenOrange[1];
                for (int[] dir : dirs) {
                    int x = u + dir[0];
                    int y = v + dir[1];

                    if (0 <= x && x < grid.length && 0 <= y && y < grid[x].length) {
                        if (grid[x][y] == 1) {
                            grid[x][y] = 2;
                            queue.offer(new int[]{x, y});
                            spread = true;
                        }
                    }
                }
            }

            if (spread)
                minutes++;
        }

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    return -1;
                }
            }
        }

        return minutes;
    }
}
