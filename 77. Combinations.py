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
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def dfs(idx: int) -> None:
            # Record combination when path length reaches k
            if len(path) == k:
                result.append(path.copy())
                return
            # Prune when remaining elements are insufficient
            if len(path) + (n - idx + 1) < k:
                return

            # Record idx and recurse (choose)
            path.append(idx)
            dfs(idx + 1)
            path.pop()

            # Skip idx and recurse
            dfs(idx + 1)

        dfs(1)
        return result