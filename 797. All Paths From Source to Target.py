from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """Finds all paths from node 0 to the last node in a DAG."""
        result = []
        self._dfs(0, [0], graph, result)
        return result

    def _dfs(self, node: int, path: List[int], graph: List[List[int]], result: List[List[int]]) -> None:
        if node == len(graph) - 1:
            result.append(path.copy())
            return

        for neighbor in graph[node]:
            path.append(neighbor)
            self._dfs(neighbor, path, graph, result)
            path.pop()
