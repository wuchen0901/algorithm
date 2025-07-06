from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 5,4,     6,2,7
        # 0 1      2 3 4
        #   index  i
        stack = []

        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result