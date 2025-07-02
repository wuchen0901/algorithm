from typing import List


class SolutionWithLoop:
    """
    Generate all subsets of a list using for-loop backtracking.
    """
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

        backtrack_with_loop([], 0)

        return result


class SolutionChooseSkip:
    """
    Generate all subsets of a list using choose / don't choose backtracking.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(path: List[int], index: int) -> None:
            if index == len(nums):
                result.append(path.copy())
                return

            # Don't choose nums[index]
            backtrack(path, index + 1)

            # Choose nums[index]
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()

        backtrack([], 0)
        return result

# 测试代码
if __name__ == "__main__":
    sol = SolutionChooseSkip()
    output = sol.subsets([1, 2, 3])
    for subset in output:
        print(subset)