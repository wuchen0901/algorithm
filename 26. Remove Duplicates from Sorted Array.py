from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 0
        while fast < len(nums):
            nums[slow] = nums[fast]
            while fast < len(nums) and nums[slow] == nums[fast]:
                fast += 1
            slow += 1

        return slow
