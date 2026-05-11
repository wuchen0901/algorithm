package com.leetcode;

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
}
