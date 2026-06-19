package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_797 {
    List<List<Integer>> paths = new ArrayList<>();
    boolean[] visited;

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int n = graph.length;
        visited = new boolean[n];
        visited[0] = true;
        List<Integer> path = new ArrayList<>();
        path.add(0);
        backtrack(graph, path, 0);

        return paths;
    }

    void backtrack(int[][] graph, List<Integer> path, int node) {
        if (node == graph.length - 1) {
            paths.add(new ArrayList<>(path));
            return;
        }

        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                path.add(neighbor);
                backtrack(graph, path, neighbor);
                path.remove(path.size() - 1);
                visited[neighbor] = false;
            }
        }
    }
}
