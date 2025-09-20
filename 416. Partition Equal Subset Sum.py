from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        total = sum(nums)
        if total % 2:
            return False
        half_sum = total // 2
        bits = 1
        for n in nums:
            if n > half_sum:
                break  # 已排序，后面都更大
            bits |= bits << n
            bits &= (1 << (half_sum + 1)) - 1
            if bits & (1 << half_sum):
                return True
        return False


print(Solution().canPartition([4, 1, 6, 3]))
