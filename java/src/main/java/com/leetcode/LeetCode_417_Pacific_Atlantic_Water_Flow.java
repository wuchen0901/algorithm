package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_417_Pacific_Atlantic_Water_Flow {
    boolean[][] pacificReachable;
    boolean[][] atlanticReachable;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;

        pacificReachable = new boolean[m][n];
        atlanticReachable = new boolean[m][n];
        // Pacific Ocean
        for (int r = 0; r < m; r++) {
            dfs(heights, r, 0, pacificReachable);
        }

        for (int c = 0; c < n; c++) {
            dfs(heights, 0, c, pacificReachable);
        }

        // Atlantic Ocean
        for (int r = 0; r < m; r++) {
            dfs(heights, r, n - 1, atlanticReachable);
        }

        for (int c = 0; c < n; c++) {
            dfs(heights, m - 1, c, atlanticReachable);
        }

        List<List<Integer>> result = new ArrayList<>();

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (pacificReachable[r][c] && atlanticReachable[r][c]) {
                    List<Integer> cell = new ArrayList<>();
                    cell.add(r);
                    cell.add(c);
                    result.add(cell);
                }
            }
        }
        return result;
    }

    void dfs(int[][] heights, int r, int c, boolean[][] reachable) {

        if (reachable[r][c]) {
            return;
        }

        reachable[r][c] = true;

        int[][] directions = new int[][]{
                {0, 1},
                {0, -1},
                {1, 0},
                {-1, 0},
        };

        for (int[] direction : directions) {
            int dr = direction[0];
            int dc = direction[1];

            int nr = r + dr;
            int nc = c + dc;

            if (nr < 0 || heights.length <= nr || nc < 0 || heights[nr].length <= nc) {
                continue;
            }

            if (heights[r][c] <= heights[nr][nc]) {
                dfs(heights, nr, nc, reachable);
            }
        }
    }
}
