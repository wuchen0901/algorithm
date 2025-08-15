from typing import List


class Solution:
    # Input: points = [[10,16],[2,8],[1,6],[7,12]]
    # Output: 2
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda balloon: balloon[1])
        # [1, 6]
        # [2, 8]
        # [7, 12]
        # [10, 16]

        #        16
        #
        #        13
        #     12
        #
        #   8
        #     7
        # 6
        #
        #   2
        # 1
        #

        arrows = 0
        i = 0
        while i < len(points):
            start, end = points[i]
            arrows += 1
            i += 1
            while i < len(points) and points[i][0] <= end:
                i += 1

        return arrows
