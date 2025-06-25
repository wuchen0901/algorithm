from collections import deque
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # My first thought is to iterate over all the paths.
        # For example, given the input [2,3,1,1,4],
        # from index 0, can go to index 1 and 2,
        # from index 1, can go to index 2, 3, 4.
        # I think it becomes an adjacency list.
        # graph = [[1, 2], [2, 3, 4], [3], [4], []]
        # source = 0, destination = 4
        if len(nums) == 1: return True

        graph = []
        for i, n in enumerate(nums):
            # i: 0, n: 2
            # i: 1, n: 3
            # i: 2, n: 1
            # i: 3, n: 1
            # i: 4, n: 4
            graph.append([x + i + 1 for x in range(n) if x + i + 1 < len(nums)])

        # Source: 0
        destination = len(nums) - 1
        queue = deque()
        queue.append(0)
        visited = set()
        visited.add(0)

        while queue:
            vertex = queue.popleft()
            for v in graph[vertex]:
                if v == destination:
                    return True
                if v in visited:
                    continue
                visited.add(v)
                queue.append(v)
        return False
