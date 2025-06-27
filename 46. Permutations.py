from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack([], nums, result)
        return result

    def backtrack(self, path, remaining, result):
        if not remaining:
            result.append(path.copy())
            return

        # This backtracking approach generates all possible permutations.
        # It works because the order of elements in 'path' matters — e.g., [1, 2, 3] and [3, 2, 1] are different permutations.
        # When the order of elements doesn’t matter, such as in combinations or subsets,
        # we should avoid generating duplicate results like [1, 2] and [2, 1].
        # Instead of trying all remaining elements, we typically sort the input
        # and use an index-based loop that only considers forward elements.
        #
        # Example:
        # for i in range(start, len(nums)):
        #   path.append(nums[i])
        #   backtrack(i + 1, path)
        #   path.pop()
        for i in remaining:
            next_remaining = remaining.copy()
            next_remaining.remove(i)
            path.append(i)
            self.backtrack(path, next_remaining, result)
            path.pop()
