from typing import List


# Given a list of unique integers, return all possible subsets (the power set).
# Example:
#   Input:  nums = [1, 2, 3]
#   Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
#
#   curr        start           i          curr         next range      next value
#   []              0           0          [1]          (1, 3)          [2, 3]
#   [1]             1           1          [1, 2]       (2, 3)          [3]
#   []              0           1          [2]          (2, 3)          [3]
#   []              0           2          [3]          (3, 3)          []

def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(curr: List[int], start: int):
        res.append(curr.copy())

        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()

    backtrack([], 0)
    return res


print(subsets([1, 2, 3]))


# Given a list of integers that may contain duplicates, return all unique subsets (the power set).
# Example:
#   Input:  nums = [1, 2, 3, 2]
#   Output: [[], [3], [3, 3], [3, 3, 6], [3, 6], [6]]
def subsets_v2(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    def backtrack(curr: List[int], start: int):
        res.append(curr.copy())

        while start < len(nums):
            curr.append(nums[start])
            while start < len(nums) and nums[start] == curr[- 1]:
                start += 1
            if start < len(nums):
                backtrack(curr, start)
            curr.pop()

    backtrack([], 0)
    return res


print(subsets_v2([1, 2, 3, 2]))


# Given a list of integers that may contain duplicates, return all unique subsets (the power set).
# Example:
#   Input:  nums = [1, 2, 3, 2]
#   Output: [[], [3], [3, 3], [3, 3, 6], [3, 6], [6]]
def subsets_v3(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    def backtrack(curr: List[int], start: int):
        res.append(curr.copy())

        while start < len(nums):
            curr.append(nums[start])
            while start < len(nums) and nums[start] == curr[- 1]:
                start += 1
            backtrack(curr, start)
            curr.pop()

    backtrack([], 0)
    return res


print(subsets_v3([1, 2, 3, 2]))


# Given a list of integers that may contain duplicates, return all unique subsets (the power set).
# Example:
#   Input:  nums = [1, 2, 3, 2]
#   Output:
def subsets_v4(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    # nums: [ 1, 2, 2, 3]
    # When curr is [1, 2], start: 2, range(2, 4): [2, 3]
    # When curr is [1, 2, 2], start: 3, range(3, 4): [3]
    def backtrack(curr: List[int], start: int):
        res.append(curr.copy())

        for i in range(start, len(nums)):
            if 0 <= i < len(nums) and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()

    backtrack([], 0)
    return res


print('subsets_v4', subsets_v4([1, 2, 3, 2]))


# Given a list of integers that may contain duplicates, return all unique subsets (the power set).
# Example:
#   Input:  nums = [1, 2, 3, 2]
#   Output:
def subsets_v5(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    def backtrack(curr: List[int], start: int):
        res.append(curr.copy())

        for i in range(start, len(nums)):
            if i == start:
                pass
            elif 0 < i < len(nums) and nums[i] == nums[i - 1]:  # skip duplicates in the same layer
                continue
            curr.append(nums[i])
            print("curr: ", curr, ",\t\t i + 1: ", i + 1, "\t range: ", nums[i + 1:])
            backtrack(curr, i + 1)
            curr.pop()

    backtrack([], 0)
    return res


print('subsets_v5', subsets_v5([1, 2, 3, 2]))
