from collections import defaultdict
from enum import IntEnum
from typing import List


class State(IntEnum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        # Build the graph: edge from course v to course u (u depends on v)
        for u, v in prerequisites:
            graph[v].append(u)

        state = defaultdict(int)

        def backtrack(node):
            # Even without the VISITED state, this code snippet still works, but it performs duplicate computations.
            if state[node] == State.VISITED:
                return False  # Already checked, no cycle
            if state[node] == State.VISITING:
                return True  # Cycle found

            state[node] = State.VISITING
            for child in graph[node]:
                if backtrack(child):
                    return True
            state[node] = State.VISITED
            return False  # No cycle found from this path

        for node in range(numCourses):
            if state[node] == State.UNVISITED:
                if backtrack(node):
                    return False  # If cycle found, cannot finish

        return True  # All nodes processed with no cycles
