from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, index):
            if index == len(nums):
                result.append(path.copy())
                return

            # Do not include nums[index] in the current subset
            backtrack(path, index + 1)

            # Include nums[index] in the current subset
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()

        backtrack([], 0)
        return result
