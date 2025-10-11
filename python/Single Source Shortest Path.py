import heapq
from typing import List, Tuple


# 📘 Problem: Single Source Shortest Path (Dijkstra Template)
# Given a directed graph with non-negative edge weights, compute the shortest distances
# from a starting node to all other nodes.
#
# Parameters:
# - n: Total number of nodes in the graph, labeled from 0 to n-1.
# - edges: A list of tuples (u, v, w) where u -> v is a directed edge with weight w.
# - start: The starting node to compute shortest paths from.
#
# Returns:
# - A list `dist` of size n, where dist[i] is the shortest distance from `start` to node i.
#   If a node is unreachable, its distance should be -1.
def dijkstra_shortest_path(n: int, edges: List[Tuple[int, int, int]], start: int) -> List[int]:
    """
    Dijkstra's algorithm for single-source shortest paths.
    Args:
        n: number of nodes (0 to n-1)
        edges: list of (u, v, w) directed edges with weight w
        start: starting node
    Returns:
        List of shortest distances from start to each node; -1 if unreachable.
    """
    graph = {u: [] for u in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))

    distances = [float('inf')] * n
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        distance, v = heapq.heappop(heap)
        if distance > distances[v]:
            continue
        for neighbor, w in graph[v]:
            new_dist = distance + w
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return [d if d != float('inf') else -1 for d in distances]


# Test case for Dijkstra implementation
if __name__ == "__main__":
    # Test case: triggers relaxation failure path
    # 0 --1--> 1
    # 0 --2--> 2   (shorter direct path)
    # 1 --3--> 2   (longer via 1, triggers ❌ branch)
    # 1 --6--> 3
    # 2 --3--> 3
    n = 4
    edges = [
        (0, 1, 1),
        (0, 2, 2),  # direct and shorter path to 2
        (1, 2, 3),  # longer via 1, should hit ❌ print
        (1, 3, 6),
        (2, 3, 3)
    ]
    start = 0
    result = dijkstra_shortest_path(n, edges, start)
    print("Shortest distances from node 0:", result)
    # Expected: [0, 1, 2, 5]
