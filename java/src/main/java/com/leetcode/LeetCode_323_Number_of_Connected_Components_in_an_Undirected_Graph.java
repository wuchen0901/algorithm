package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class LeetCode_323_Number_of_Connected_Components_in_an_Undirected_Graph {
    /**
     * LeetCode 323. Number of Connected Components in an Undirected Graph
     * <p>
     * Description:
     * You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges
     * where edges[i] = [ai, bi] indicates that there is an undirected edge between ai and bi.
     * <p>
     * Return the number of connected components in the graph.
     * <p>
     * Example 1:
     * Input: n = 5, edges = [[0,1],[1,2],[3,4]]
     * Output: 2
     * Explanation: There are two connected components: {0,1,2} and {3,4}.
     * <p>
     * Example 2:
     * Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
     * Output: 1
     * <p>
     * Constraints:
     * - 1 <= n <= 2000
     * - 0 <= edges.length <= 5000
     * - edges[i].length == 2
     * - 0 <= ai, bi < n
     * - ai != bi
     * - No duplicate edges.
     */
    public int countComponents(int n, int[][] edges) {
        int[] parents = new int[n];
        for (int i = 0; i < parents.length; i++) {
            parents[i] = i;
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            int pu = find(parents, u);
            int pv = find(parents, v);

            parents[pu] = pv;
        }

        int count = 0;
        for (int i = 0; i < parents.length; i++) {
            if (parents[i] == i) {
                count++;
            }
        }

        return count;
    }

    private int find(int[] parents, int x) {
        if (parents[x] == x) {
            return x;
        }

        return find(parents, parents[x]);
    }
}
