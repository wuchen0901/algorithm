from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights = [0] + heights + [0]
        max_area = 0
        for right in range(1, len(heights)):
            while stack and heights[stack[-1]] > heights[right]:
                top = stack.pop()
                max_area = max(max_area, (right - stack[-1] - 1) * heights[top])
            stack.append(right)

        return max_area


print(Solution().largestRectangleArea([2, 1, 2]))
