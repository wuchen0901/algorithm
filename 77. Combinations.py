from typing import List


class SolutionForLoopPrune:
    """
    Generate all combinations of k numbers from 1 to n using for-loop backtracking with pruning.
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        nums.sort()

        combinations = []

        def backtrack(path, start):
            if len(path) == k:
                combinations.append(path.copy())
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)

        return combinations


class SolutionChooseSkip:
    """
    Generate all combinations of k numbers from 1 to n using choose/skip backtracking with pruning.
    """

    def combine(self, candidates: List[int], k: int) -> List[List[int]]:
        result = []

        def backtrack(path: List[int], i):
            # Prune
            if len(path) == k:
                result.append(path.copy())
                return

            if i == len(candidates):
                return

            backtrack(path, i + 1)

            path.append(candidates[i])
            backtrack(path, i + 1)
            path.pop()

        backtrack([], 0)

        return result


if __name__ == "__main__":
    sol = SolutionChooseSkip()
    output = sol.combine([1, 2, 3], 2)
    for combination in output:
        print(combination)
