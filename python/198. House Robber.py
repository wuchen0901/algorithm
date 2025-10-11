from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        take = [0] * n
        take[0] = nums[0]

        skip = [0] * n

        for i in range(1, len(nums)):
            take[i] = max(take[i - 1], skip[i - 1] + nums[i])
            skip[i] = max(skip[i - 1], take[i - 1])
        return max(take[n - 1], skip[n - 1])
        #       3, 4, 2, 1, 9, 5
        # take  3  4
        # skip  0  3
