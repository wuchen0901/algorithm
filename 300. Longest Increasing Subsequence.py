from bisect import bisect_left
from typing import List


class Solution:
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], so the length is 4.
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Returns the length of the longest strictly increasing subsequence in the input list.
        Uses binary search (via bisect_left) to achieve O(n log n) time complexity.
        """
        from bisect import bisect_left

        tails = []
        for num in nums:
            index = bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num
        return len(tails)

    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        """
        Quadratic-time DP solution (O(n^2)).
        dp[i] = length of the longest strictly increasing subsequence that ends at index i.
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution()
    print('O(n log n) tails + binary search:', s.lengthOfLIS(nums))
    print('O(n^2) DP:', s.lengthOfLIS_dp(nums))
