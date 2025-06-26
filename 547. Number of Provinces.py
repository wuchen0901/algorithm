from typing import List


class Solution:
    def findCircleNum(self, is_connected: List[List[int]]) -> int:
        # DFS: Starting from a node, recursively explore all its connected neighbors before backtracking.
        # Actually, both adjacency list and adjacency matrix implicitly assume each node has an ID — usually an integer index 0 to n-1.
        # len(isConnected) equals the number of nodes in the graph.

        # Example: isConnected = [
        #     [1, 1, 0],
        #     [1, 1, 0],
        #     [0, 0, 1]
        # ]
        count = 0
        visited = set()
        # Iterate over all unvisited node. i: 0, 1, 2
        for i in range(len(is_connected)):
            if i in visited:
                continue
            visited.add(i)

            # DFS through from this unvisited node and mark all as visited.
            self.dfs(i, is_connected, visited)

            count += 1

        return count

    def dfs(self, curr, is_connected: List[List[int]], visited):
        # If the current node has no more unvisited neighbors.
        # For example, isConnected[0] is [1, 1, 0]
        # For example, isConnected[1] is [1, 1, 0]
        # For example, isConnected[2] is [0, 0, 1]
        for i, v in enumerate(is_connected[curr]):
            # If node curr is not connected to the node i, which means i is not curr's neighbor, then continue.
            if v == 0:
                continue
            # If the neighbor 'i' is visited, then continue.
            if i in visited:
                continue
            # If the 'i' is curr's neighbor and hasn't been visited.
            visited.add(i)
            self.dfs(i, is_connected, visited)
