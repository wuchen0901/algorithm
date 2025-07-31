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


# Kruskal's algorithm implementation
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        self.parent[fx] = fy
        return True


class SolutionKruskal:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort()
        uf = UnionFind(n)
        cost = 0
        count = 0

        for dist, u, v in edges:
            if uf.union(u, v):
                cost += dist
                count += 1
                if count == n - 1:
                    break

        return cost
