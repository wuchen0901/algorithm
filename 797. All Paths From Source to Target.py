from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        self.allPaths([0], graph, result)
        return result

    def allPaths(self, path, graph, result):
        children = graph[path[-1]]
        if not children:
            result.append(path.copy())

        for child in children:
            path.append(child)
            self.allPaths(path, graph, result)
            path.pop()
