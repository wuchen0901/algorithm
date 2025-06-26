from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Given an adjacency matrix isConnected, return the number of connected components (provinces) in the graph.
        """
        def dfs(node: int):
            for neighbor, connected in enumerate(isConnected[node]):
                if connected and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        n = len(isConnected)
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1

        return count
