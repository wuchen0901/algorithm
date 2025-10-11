from collections import deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque()
        queue.append(source)

        visited = set()
        visited.add(source)
        while queue:
            cur = queue.popleft()
            for node in graph[cur]:
                if node == destination:
                    return True
                if node in visited:
                    continue
                visited.add(node)
                queue.append(node)
        return False
