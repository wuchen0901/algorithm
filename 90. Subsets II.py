from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtrack(path, index):
            if index == len(nums):
                unique_subsets.add(tuple(path))
                return

            # Skip current element
            backtrack(path, index + 1)

            # Include current element
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()

        unique_subsets = set()
        backtrack([], 0)
        return [list(path) for path in unique_subsets]
