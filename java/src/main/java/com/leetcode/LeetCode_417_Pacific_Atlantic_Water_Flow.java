package com.leetcode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class LeetCode_417_Pacific_Atlantic_Water_Flow {
    private static final int[][] DIRECTIONS = {
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0}
    };

    boolean[][] pacificReachable;
    boolean[][] atlanticReachable;

    // Multi-source DFS: all cells on the corresponding ocean boundary are sources.
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

    // Multi-source BFS: start from each ocean's boundary and traverse uphill in reverse.
    public List<List<Integer>> pacificAtlanticBFS(int[][] heights) {
        int rows = heights.length;
        int cols = heights[0].length;

        boolean[][] pacific = new boolean[rows][cols];
        Deque<int[]> pacificQueue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            addSource(r, 0, pacificQueue, pacific);
        }
        for (int c = 0; c < cols; c++) {
            addSource(0, c, pacificQueue, pacific);
        }
        bfs(heights, pacificQueue, pacific);

        boolean[][] atlantic = new boolean[rows][cols];
        Deque<int[]> atlanticQueue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            addSource(r, cols - 1, atlanticQueue, atlantic);
        }
        for (int c = 0; c < cols; c++) {
            addSource(rows - 1, c, atlanticQueue, atlantic);
        }
        bfs(heights, atlanticQueue, atlantic);

        List<List<Integer>> result = new ArrayList<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (pacific[r][c] && atlantic[r][c]) {
                    result.add(List.of(r, c));
                }
            }
        }
        return result;
    }

    private void addSource(int r, int c, Deque<int[]> queue, boolean[][] visited) {
        if (!visited[r][c]) {
            visited[r][c] = true;
            queue.offer(new int[]{r, c});
        }
    }

    private void bfs(int[][] heights, Deque<int[]> queue, boolean[][] visited) {
        int rows = heights.length;
        int cols = heights[0].length;

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0];
            int c = cell[1];

            for (int[] direction : DIRECTIONS) {
                int nr = r + direction[0];
                int nc = c + direction[1];

                if (0 <= nr && nr < rows && 0 <= nc && nc < cols
                        && !visited[nr][nc]
                        && heights[r][c] <= heights[nr][nc]) {
                    visited[nr][nc] = true;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
    }

    void dfs(int[][] heights, int r, int c, boolean[][] reachable) {

        if (reachable[r][c]) {
            return;
        }

        reachable[r][c] = true;

        for (int[] direction : DIRECTIONS) {
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
