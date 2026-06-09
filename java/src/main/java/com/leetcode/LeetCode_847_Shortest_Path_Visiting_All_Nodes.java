package com.leetcode;

import java.util.ArrayDeque;
import java.util.Queue;

public class LeetCode_847_Shortest_Path_Visiting_All_Nodes {
    public int shortestPathLength(int[][] graph) {
        int n = graph.length;
        boolean[][] visited = new boolean[n][1 << n];
        Queue<int[]> queue = new ArrayDeque<>();
        // 0 F T F F F F F F
        // 1 F F T F F F F F
        // 2 F F F F T F F F

        for (int i = 0; i < n; i++) {
            int mask = 1 << i;
            visited[i][mask] = true;
            queue.offer(new int[] { i, mask, 0 });
        }

        int finalMask = (1 << n) - 1;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int s = 0; s < size; s++) {
                int[] state = queue.poll();
                int node = state[0];
                int mask = state[1];
                int step = state[2];

                if (mask == finalMask) {
                    return step;
                }

                for (int neighbor : graph[node]) {
                    int nextMask = mask | (1 << neighbor);
                    int nextNode = neighbor;
                    if (!visited[nextNode][nextMask]) {
                        visited[nextNode][nextMask] = true;
                        queue.offer(new int[] { nextNode, nextMask, step + 1 });
                    }
                }
            }
        }

        return -1;
    }
}
