"""
Problem: Find All Articulation Points in an Undirected Graph

Description:
Given an undirected connected graph with n nodes labeled from 0 to n - 1,
and a list of bidirectional connections (edges), return all the articulation
points in the graph.

A node is an articulation point if removing it (and all its connected edges)
increases the number of connected components in the graph.

Return the list of articulation points sorted in ascending order. If there
are no articulation points, return an empty list.

Input:
- n (int): Number of nodes in the graph. 1 <= n <= 10^5
- connections (List[List[int]]): Each edge is [u, v], a bidirectional edge.

Output:
- A list of articulation points in ascending order.

Example:
Input:
n = 5
connections = [[0, 1], [1, 2], [1, 3], [3, 4]]
Output:
[1, 3]

Constraints:
- The graph is connected and does not contain self-loops or multiple edges.
- Your algorithm should run in O(N + M) time, where N is nodes and M is edges.
"""
class Solution:
    def find_articulation_points(self, n: int, connections: list) -> list:
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        discovery_time = [-1] * n
        lowest_reachable = [-1] * n
        visited = [False] * n
        articulation_points = set()
        time = [0]  # use list for mutability in nested scope

        def dfs(node: int, parent: int):
            visited[node] = True
            discovery_time[node] = lowest_reachable[node] = time[0]
            time[0] += 1
            children = 0

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not visited[neighbor]:
                    dfs(neighbor, node)
                    lowest_reachable[node] = min(lowest_reachable[node], lowest_reachable[neighbor])
                    if parent != -1 and lowest_reachable[neighbor] >= discovery_time[node]:
                        articulation_points.add(node)
                    children += 1
                else:
                    lowest_reachable[node] = min(lowest_reachable[node], discovery_time[neighbor])

            if parent == -1 and children > 1:
                articulation_points.add(node)

        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        return sorted(articulation_points)
