from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]

        # 🔁 1. Recursive Traversal (Side-Effect Recursion)
        # 🔄 2. Recursive Return (Return-Value-Based Recursion)
        # x: 0 -> 4
        # x: 1 -> 5
        # Process:
        # x: 0
        # while parents[x] != x:
        # parents[x]: 2
        # x: 2
        # parents[2]: 4
        # x: 4
        # parents[4]: 4
        def find(x):
            # x: 2
            while parents[x] != x:
                x = parents[x]
            return x

        def union(x, y):
            x_root = find(x)
            y_root = find(y)
            parents[x_root] = y_root

        for row in range(len(isConnected)):
            for i in range(len(isConnected[row])):
                if i < row and isConnected[row][i] == 1:
                    union(row, i)

        count = 0
        for i, parent in enumerate(parents):
            if i == parent:
                count += 1
        return count
