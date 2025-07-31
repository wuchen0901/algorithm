import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u in range(len(points)):
            for v in range(u + 1, len(points)):
                manhattan_distance = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                graph[u].append((v, manhattan_distance))
                graph[v].append((u, manhattan_distance))

        visited = set()
        heap = [(0, 0)]
        cost = 0

        while heap and len(visited) < len(points):
            distance, vertex = heapq.heappop(heap)

            if vertex in visited:
                continue

            visited.add(vertex)

            cost += distance

            for neighbor, weight in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(heap, (weight, neighbor))

        return cost
