from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half_sum = total // 2
        bits = 1
        for n in nums:
            if half_sum < n:
                continue
            bits |= bits << n
            bits &= (1 << (half_sum + 1)) - 1
            if bits & (1 << half_sum):
                return True
        return False


print(Solution().canPartition([4, 1, 6, 3]))
