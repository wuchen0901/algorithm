from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        i = 0
        for n in nums:
            i |= i << n
            i |= 1 << n
            if i & (1 << target):
                return True
        return False


print(Solution().canPartition([4, 1, 6, 3]))
