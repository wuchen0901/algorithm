from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, n in enumerate(nums):
            if target - n in complement:
                return [complement[target - n], i]
            complement[n] = i
        return None
