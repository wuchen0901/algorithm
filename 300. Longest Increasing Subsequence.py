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


if __name__ == '__main__':
    index = bisect_left([1, 2, 2, 3], 1.5, )
    print(index)
