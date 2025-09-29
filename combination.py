from typing import List


# Given a list of unique integers, return all possible subsets (the power set).
# Example:
#   Input:  nums = [3, 6, 7]
#   Output: [[], [3], [3, 6], [3, 6, 7], [3, 7], [6], [6, 7], [7]]
def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(curr: List[int], index: int):
        res.append(curr.copy())

        for i in range(index, len(nums)):
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()

    backtrack([], 0)
    return res

print(subsets([3, 6, 7]))
