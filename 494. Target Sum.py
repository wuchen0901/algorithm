from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(maxsize=None)
        def dfs(pre_sum, i):
            if i == len(nums):
                if pre_sum == target:
                    return 1
                return 0

            return dfs(pre_sum + nums[i], i + 1) + dfs(pre_sum - nums[i], i + 1)

        return dfs(0, 0)

    def findTargetSumWays_bottom_up(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0

        subset_sum = (total + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset_sum]
