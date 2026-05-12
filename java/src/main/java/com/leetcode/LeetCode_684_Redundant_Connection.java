package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LeetCode_684_Redundant_Connection {
    static class UnionFind {
        int[] parents;

        public UnionFind(int n) {
            parents = new int[n];

            for (int i = 0; i < n; i++) {
                parents[i] = i;
            }
        }

        boolean union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);

            if (rootX == rootY) {
                return false;
            }

            parents[rootX] = rootY;

            return true;
        }

        int find(int x) {
            if (parents[x] == x) {
                return x;
            }

            return parents[x] = find(parents[x]);
        }
    }

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        UnionFind uf = new UnionFind(n + 1);
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            if (!uf.union(u, v)) {
                return edge;
            }
        }

        return new int[2];
    }

    public int[] findRedundantConnectionDFS(int[][] edges) {
        int n = edges.length;
        Map<Integer, List<Integer>> graph = new HashMap<>();

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            boolean[] visited = new boolean[n + 1];
            if (hasPath(graph, u, v, visited)) {
                return edge;
            }

            graph.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
            graph.computeIfAbsent(v, k -> new ArrayList<>()).add(u);
        }

        return new int[]{};
    }

    private boolean hasPath(Map<Integer, List<Integer>> graph, int current, int target, boolean[] visited) {
        visited[current] = true;
        for (int neighbor : graph.getOrDefault(current, new ArrayList<>())) {
            if (neighbor == target) {
                return true;
            }

            if (visited[neighbor]) {
                continue;
            }

            if (hasPath(graph, neighbor, target, visited)) {
                return true;
            }
        }

        return false;
    }
}
