package com.leetcode;

import java.util.*;

public class LeetCode_1971_Find_if_Path_Exists_in_Graph {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source == destination) return true;

        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        Deque<Integer> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[n];

        queue.offer(source);
        visited[source] = true;

        while (!queue.isEmpty()) {
            int vertex = queue.poll();
            for (int neighbor : graph.get(vertex)) {
                if (neighbor == destination) {
                    return true;
                }

                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }

        return false;
    }
}
