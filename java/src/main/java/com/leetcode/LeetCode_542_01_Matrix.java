package com.leetcode;

import java.util.ArrayDeque;
import java.util.Queue;

public class LeetCode_542_01_Matrix {
    public int[][] updateMatrix(int[][] mat) {

        Queue<int[]> queue = new ArrayDeque<>();

        int inf = 10000;
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                } else {
                    mat[i][j] = inf;
                }
            }
        }

        int[][] dirs = new int[][]{
                {0, 1},
                {1, 0},
                {0, -1},
                {-1, 0},
        };

        int distance = 0;

        while (!queue.isEmpty()) {

            int size = queue.size();

            for (int s = 0; s < size; s++) {
                int[] cell = queue.poll();
                int u = cell[0];
                int v = cell[1];

                for (int[] dir : dirs) {
                    int x = u + dir[0];
                    int y = v + dir[1];

                    if (0 <= x && x < mat.length && 0 <= y && y < mat[x].length) {
                        if (mat[x][y] == inf) {
                            mat[x][y] = distance + 1;
                            queue.offer(new int[]{x, y});
                        }
                    }
                }
            }

            distance++;
        }

        return mat;
    }
}
