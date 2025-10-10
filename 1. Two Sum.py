from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, num in enumerate(nums):
            if target - num in complement:
                return [complement[target - num], i]  # earlier index, then current
            else:
                complement[num] = i
