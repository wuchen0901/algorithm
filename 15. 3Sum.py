from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Input: nums = [-1,0,1,2,-1,-4]
        # Output: [[-1,-1,2],[-1,0,1]]
        nums.sort()
        # Input: nums = [-4,-1,-1,0,1,2]
        unique_set = set()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left != right:
                total = nums[left] + nums[right]
                if total < -nums[i]:
                    left += 1
                elif -nums[i] < total:
                    right -= 1
                else:
                    unique_set.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
        return [list(r) for r in unique_set]
