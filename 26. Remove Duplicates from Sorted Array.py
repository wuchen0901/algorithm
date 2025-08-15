from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = slow = 0
        while fast < len(nums):
            # Find the next different number
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1

            if fast < len(nums):
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
