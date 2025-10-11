from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutations = []

        def backtrack(path, remaining):
            if not remaining:
                permutations.append(path.copy())
                return

            i = 0

            while i < len(remaining):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i + 1:])
                path.pop()

                i = bisect_right(remaining, remaining[i])

        backtrack([], nums)

        return permutations

    def permuteUnique_used_array(self, nums: List[int]) -> List[List[int]]:
        """
        Method 2: Use 'used' array + sorting + pruning to avoid duplicates
        """
        nums.sort()
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue  # Prune: avoid choosing the same element in the same depth
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res

    def permuteUnique_counter(self, nums: List[int]) -> List[List[int]]:
        """
        Method 3: Use Counter to track element usage frequency
        """
        from collections import Counter
        counter = Counter(nums)
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    counter[num] += 1

        backtrack([])
        return res


if __name__ == '__main__':
    print(bisect_right([], 1))
    print(bisect_right([1], 1))
    print(bisect_right([1], 2))
    print(bisect_right([1], 0))
    print('---')
    print(bisect_left([], 1))
    print(bisect_left([1], 1))
    print(bisect_left([1], 2))
    print(bisect_left([1], 0))
    print('---')
    a = [9, 8, 3, 3]
    a.remove(3)
    print(a)
    b = [8, 7, 0, 9]
    print(b[4:])
