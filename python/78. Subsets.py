from typing import List


class SolutionWithLoop:
    """
    For-loop based backtracking
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path: List[int], start):
            result.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return result


class SolutionChooseSkip:
    """
    Binary decision tree
    Choose / Don't Choose recursion
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path: List[int], i: int):
            if i == len(nums):
                result.append(path.copy())
                return

            path.append(nums[i])
            backtrack(path, i + 1)
            path.pop()
            backtrack(path, i + 1)

        backtrack([], 0)
        return result


# 测试代码
if __name__ == "__main__":
    sol = SolutionChooseSkip()
    output = sol.subsets([1, 2, 3])
    for subset in output:
        print(subset)
