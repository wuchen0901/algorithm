from typing import List


class Solution:
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dynamic programming problem
        # dp = {}
        # for num in nums:
        #     for v in dp.items():
        #        if v < num:
        #            dp[v]
        # If I write it this way, things will go wrong when the input contains duplicate elements
        # so the inputs can’t be used as hash keys
        # At last, I
        # Input: nums = [10,9,2,5,3,7,101,18]
        # I need to maintain an relationship
        # read 10
        # [10] ,[1]
        # read 9
        # [10,9], [1,1]
        # 2
        # [10,9,2],  [1,1,1]
        # 5
        # [10,9,2,5],  [1,1,1,2]
        # 3
        # [10,9,2,5,3],  [1,1,1,2,2]
        # 7
        # [10,9,2,5,3,7],  [1,1,1,2,2,3]
        # 101
        # [10,9,2,5,3,7,101],  [1,1,1,2,2,3,4]
        # 18
        # [10,9,2,5,3,7,101,18],  [1,1,1,2,2,3,4,4]
        # 4
        # Input: nums = [10,9,2,5,3,7,101,18]
        counts = []
        for i, num in enumerate(nums):
            max_count = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_count = max(max_count, counts[j] + 1)
            counts.append(max_count)
        return max(counts)
