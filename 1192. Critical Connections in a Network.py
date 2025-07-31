from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        def dfs(u: int, parent: int):
            nonlocal time
            visited[u] = True
            dfn[u] = low[u] = time
            time += 1

            for v in graph[u]:
                if v == parent:
                    continue
                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > dfn[u]:
                        result.append([u, v])
                else:
                    low[u] = min(low[u], dfn[v])

        # Build graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        dfn = [0] * n          # Discovery time of each node
        low = [0] * n          # Lowest discovery time reachable
        visited = [False] * n
        time = 1
        result = []

        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        return result