from collections import defaultdict
from typing import List


class Solution:
    def canPartitionV3(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2

        counts = defaultdict(int)
        counts[0] = 1
        for n in nums:
            new_counts = defaultdict(int, counts)
            for k, v in counts.items():
                new_counts[k + n] += v
            counts = new_counts
        return counts[half] > 0

    def canPartitionV2(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half_sum = total // 2

        dp = [False] * (half_sum + 1)
        dp[0] = True
        for n in nums:
            for i in range(half_sum, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]
        return dp[half_sum]

    def canPartitionV1(self, nums: List[int]) -> bool:
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


print(Solution().canPartitionV3([1, 5, 11, 5]))
