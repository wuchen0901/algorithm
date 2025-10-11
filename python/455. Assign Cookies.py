from typing import List


class Solution:
    def findContentChildren(self, greedy_factors: List[int], cookies: List[int]) -> int:
        greedy_factors.sort()
        cookies.sort()
        i = 0
        result = 0
        for factor in greedy_factors:
            # refactor: [1 2 3],
            # cookies: [1, 1]
            while i < len(cookies) and cookies[i] < factor:
                i += 1
            if i < len(cookies): # cookies[i] >= factor
                result += 1
                i += 1
            else:
                break

        return result
