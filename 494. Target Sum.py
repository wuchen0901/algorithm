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
