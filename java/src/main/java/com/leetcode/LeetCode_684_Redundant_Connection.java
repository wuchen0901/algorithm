package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_684_Redundant_Connection {
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        int[] parents = new int[n + 1];
        for (int i = 0; i < parents.length; i++) {
            parents[i] = i;
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int pu = find(parents, u);
            int pv = find(parents, v);

            if (pv == pu) {
                return edge;
            }

            parents[pu] = pv;
        }

        return new int[0];
    }

    private int find(int[] parents, int x) {
        if (parents[x] == x) {
            return x;
        }

        parents[x] = find(parents, parents[x]);
        return parents[x];
    }
}
