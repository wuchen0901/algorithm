from collections import deque
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        # [1,0,4]
        for i, num in enumerate(nums):
            # 0, 1
            # 1, 0
            # 2, 4
            if farest < i:
                return False
            farest = max(farest, i + num)
            # 1
            # 1
            if farest >= len(nums) - 1:
                return True
        return True
