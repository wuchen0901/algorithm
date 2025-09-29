class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            res.append(path[:])  # 每一步都存当前组合

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
