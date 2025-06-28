from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [1, 2, 3, 4, 4, 6]
        # [1, 1, 1, 1]
        # [-10, -5, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]
        result = []
        i = 0
        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:  # Find the next different value
                        left += 1
                elif 0 < total:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:  # Find the next different value
                        left += 1

                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            i += 1
            while i < len(nums) - 2 and nums[i - 1] == nums[i]:
                i += 1
        return result
