from typing import List


class SolutionForLoopPrune:
    """
    Generate all combinations of k numbers from 1 to n using for-loop backtracking with pruning.
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(start: int, path: List[int]) -> None:
            if len(path) == k:
                result.append(path.copy())
                return
            # Prune: ensure enough remaining numbers to reach k
            max_start = n - (k - len(path)) + 1
            for i in range(start, max_start + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result


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
