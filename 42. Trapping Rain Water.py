from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for right in range(len(height)):
            while stack and height[right] > height[stack[-1]]:
                bottom = stack.pop()
                if stack:
                    left = stack[-1]
                    width = right - left - 1
                    bounded_height = min(height[left], height[right]) - height[bottom]
                    water += width * bounded_height

            stack.append(right)

        return water
