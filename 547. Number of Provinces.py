from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = list(range(n))

        # 🧠 Path Compression
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        # 🔄 Union
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y: # Is it necessary?
                parents[root_x] = root_y

        # ⚙️ Traverse only the upper triangle of the matrix
        for i in range(n):
            for j in range(i):
                if i < j and isConnected[i][j]:
                    union(i, j)

        # ✅ Count the number of unique roots (provinces)
        return sum(1 for i in range(n) if parents[i] == i)