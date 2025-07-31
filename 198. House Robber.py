from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp1, dp2 = nums[0], max(nums[0], nums[1])
        for num in nums[2:]:
            dp1, dp2 = dp2, max(dp2, dp1 + num)
        return dp2
