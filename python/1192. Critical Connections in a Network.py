from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        discovery_time = [-1] * n  # When each node is first visited
        earliest_reachable = [-1] * n  # The lowest discovery time reachable from this node
        bridges = []
        time = 0

        def dfs(node: int, parent: int):
            nonlocal time
            discovery_time[node] = earliest_reachable[node] = time
            time += 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if discovery_time[neighbor] == -1:
                    dfs(neighbor, node)
                    earliest_reachable[node] = min(earliest_reachable[node], earliest_reachable[neighbor])
                    if earliest_reachable[neighbor] > discovery_time[node]:
                        bridges.append([node, neighbor])
                else:
                    earliest_reachable[node] = min(earliest_reachable[node], discovery_time[neighbor])

        for i in range(n):
            if discovery_time[i] == -1:
                dfs(i, -1)

        return bridges
