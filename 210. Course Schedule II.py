from collections import defaultdict
from enum import IntEnum
from typing import List


class State(IntEnum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        state = [State.UNVISITED] * numCourses
        stack = []

        def dfs(node):
            if state[node] == State.VISITED:
                return False
            if state[node] == State.VISITING:
                return True

            state[node] = State.VISITING

            for child in graph[node]:
                if dfs(child):
                    return True

            state[node] = State.VISITED
            stack.append(node)
            return False

        for node in range(numCourses):
            if state[node] == State.UNVISITED:
                if dfs(node):
                    return []

        return stack[::-1]
