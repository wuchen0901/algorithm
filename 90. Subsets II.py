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

    def subsetsWithDup_v2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(curr: List[int], start: int):
            res.append(curr.copy())

            for i in range(start, len(nums)):
                if start < i and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)

        return res