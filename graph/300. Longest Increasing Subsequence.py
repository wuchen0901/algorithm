from bisect import bisect_left
from typing import List


class Solution:
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [float('inf')] * len(nums)
        # tails = [0,0,0,0,0,0,0,0]
        length = 0
        for num in nums:
            index = bisect_left(tails, num)
            # 0
            # 0
            # 0
            # 1
            # 1
            # 2
            # 3
            # 3
            tails[index] = num
            # [10,0,0,0, 0,0,0,0]
            # [ 9,0,0,0, 0,0,0,0]
            # [ 2,0,0,0, 0,0,0,0]
            # [ 2,5,0,0, 0,0,0,0]
            # [ 2,3,0,0, 0,0,0,0]
            # [ 2,3,7,0, 0,0,0,0]
            # [ 2,3,7,101, 0,0,0,0]
            # [ 2,3,7,18, 0,0,0,0]
            length = max(length, index)
            # 0
            # 0
            # 0
            # 1
            # 1
            # 2
            # 3
            # 3

        return length + 1


if __name__ == '__main__':
    index = bisect_left([1, 2, 2, 3], 1.5, )
    print(index)
