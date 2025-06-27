from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        # === Method 1: For-loop based backtracking ===
        # Think of it as a tree where each level represents the decision of picking an element starting from index `start`.
        def backtrack_with_loop(path, start):
            result.append(path.copy())  # Each state of 'path' is a valid subset

            for i in range(start, len(nums)):
                path.append(nums[i])            # Choose nums[i]
                backtrack_with_loop(path, i + 1)  # Recurse with next index
                path.pop()                      # Undo the choice (backtrack)

        # Uncomment the next line to use method 1
        # backtrack_with_loop([], 0)

        # === Method 2: Choose / Don't Choose style (Decision Tree style) ===
        # At every index, we make two decisions: include nums[index] or not.
        def backtrack_choose_or_not(path, index):
            if index == len(nums):
                result.append(path.copy())
                return

            # Don't choose nums[index]
            backtrack_choose_or_not(path, index + 1)

            # Choose nums[index]
            path.append(nums[index])
            backtrack_choose_or_not(path, index + 1)
            path.pop()

        # Uncomment the next line to use method 2
        backtrack_choose_or_not([], 0)

        return result
