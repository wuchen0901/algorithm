from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.
        Assumes exactly one solution exists.
        """
        index_map: Dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], i]
            index_map[num] = i

        raise ValueError("No two sum solution exists")
