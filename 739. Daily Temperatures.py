from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[int] = []  # Stores indices of temperatures
        r = [0] * len(temperatures)  # Result array with default 0s

        for right, temperature in enumerate(temperatures):
            # Check if current temperature is higher than the one at the top of the stack
            while stack and temperatures[stack[-1]] < temperature:
                left = stack.pop()
                r[left] = right - left  # Days until a warmer temperature
            stack.append(right)  # Add current index to the stack

        return r
