from collections import defaultdict
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

    def findTargetSumWays_subset_sum(self, nums: List[int], target: int) -> int:
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

    def findTargetSumWays_state_compression(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1  # Base case: one way to reach sum 0 with 0 elements

        for num in nums:
            new_dp = defaultdict(int)
            for r, count in dp.items():
                new_dp[r + num] += count
                new_dp[r - num] += count
            dp = new_dp

        return dp[target]
