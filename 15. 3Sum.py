from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        unique_set = set()

        def backtrack(path, start):
            if len(path) == 3:
                if sum(path) == 0:
                    unique_set.add(tuple(path))
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return [list(result) for result in unique_set]
