from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def _dfs(node: int, path: List[int]) -> None:
            if node == len(graph) - 1:
                result.append(path.copy())
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                _dfs(neighbor, path)
                path.pop()

        """Finds all paths from node 0 to the last node in a DAG."""
        result = []
        _dfs(0, [0])
        return result
