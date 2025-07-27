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
                rest = remaining[:i] + remaining[i + 1:]
                backtrack(path, rest)
                path.pop()

                i = bisect_right(remaining, remaining[i])

        backtrack([], nums)

        return permutations


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
