from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Input: nums = [0,0,1,1,1,2,2,3,3,4]
        # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        slow = fast = 0
        while True:
            while fast < len(nums) and nums[slow] == nums[fast]:
                fast += 1
            slow += 1

            if fast < len(nums):
                nums[slow] = nums[fast]
            else:
                break

        return slow
