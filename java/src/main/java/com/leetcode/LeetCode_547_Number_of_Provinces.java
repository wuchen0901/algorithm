package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class LeetCode_547_Number_of_Provinces {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int provinces = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                provinces++;
                dfs(isConnected, visited, i);
            }
        }

        return provinces;
    }

    void dfs(int[][] isConnected, boolean[] visited, int city) {
        visited[city] = true;

        for (int next = 0; next < isConnected.length; next++) {
            if (isConnected[city][next] == 1 && !visited[next]) {
                dfs(isConnected, visited, next);
            }
        }
    }

    public int findCircleNumBfs(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int provinceCount = 0;
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            provinceCount++;
            queue.offer(i);
            visited[i] = true;
            while (!queue.isEmpty()) {
                int city = queue.poll();
                for (int neighbor = 0; neighbor < n; neighbor++) {
                    if (isConnected[city][neighbor] == 1 && !visited[neighbor]) {
                        visited[neighbor] = true;
                        queue.offer(neighbor);
                    }
                }
            }
        }

        return provinceCount;
    }

    static class UnionFind {
        int[] parents;
        int count;

        public UnionFind(int n) {
            count = n;

            parents = new int[n];
            for (int i = 0; i < n; i++) {
                parents[i] = i;
            }
        }

        int find(int x) {
            // 0 1 2 3 3 5 4
            if (parents[x] == x) {
                return parents[x];
            }

            int i = find(parents[x]);
            return parents[x] = i;
        }

        void union(int m, int n) {
            int rootM = find(m);
            int rootN = find(n);

            if (rootM == rootN) {
                return;
            }

            parents[rootM] = rootN;
            count--;
        }
    }

    public int findCircleNumUnionFind(int[][] isConnected) {
        int n = isConnected.length;
        UnionFind union = new UnionFind(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    union.union(i, j);
                }
            }
        }

        return union.count;
    }

    public static void main(String[] args) {
        LeetCode_547_Number_of_Provinces solution =
                new LeetCode_547_Number_of_Provinces();

        int[][] isConnected = {
                {1, 1, 0},
                {1, 1, 0},
                {0, 0, 1}
        };

        int provinces = solution.findCircleNumUnionFind(isConnected);

        System.out.println(provinces);
    }
}
