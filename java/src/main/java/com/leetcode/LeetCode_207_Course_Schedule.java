package com.leetcode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class LeetCode_207_Course_Schedule {
    // BFS Kahn's Algorithm solution
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>(numCourses);
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        int[] indegree = new int[numCourses];
        for (int[] prerequisite : prerequisites) {
            int a = prerequisite[0];
            int b = prerequisite[1];

            graph.get(b).add(a);
            indegree[a]++;
        }

        Deque<Integer> queue = new ArrayDeque<>();

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        int taken = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            taken++;
            for (int neighbor : graph.get(node)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        return taken == numCourses;
    }

    // DFS 3-state solution using VISITED, VISITING, UNVISITED states
    public static class DFS3StateSolution {
        private static final int UNVISITED = 0;
        private static final int VISITING = 1;
        private static final int VISITED = 2;

        public boolean canFinish(int numCourses, int[][] prerequisites) {
            List<List<Integer>> graph = new ArrayList<>(numCourses);
            for (int i = 0; i < numCourses; i++) {
                graph.add(new ArrayList<>());
            }
            for (int[] prerequisite : prerequisites) {
                int a = prerequisite[0];
                int b = prerequisite[1];
                graph.get(b).add(a);
            }

            int[] state = new int[numCourses];
            for (int i = 0; i < numCourses; i++) {
                if (state[i] == UNVISITED) {
                    if (hasCycle(i, graph, state)) {
                        return false;
                    }
                }
            }
            return true;
        }

        private boolean hasCycle(int node, List<List<Integer>> graph, int[] state) {
            if (state[node] == VISITING) {
                // Cycle detected
                return true;
            }
            if (state[node] == VISITED) {
                return false;
            }

            state[node] = VISITING;
            for (int neighbor : graph.get(node)) {
                if (hasCycle(neighbor, graph, state)) {
                    return true;
                }
            }
            state[node] = VISITED;
            return false;
        }
    }
}
