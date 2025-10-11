def can_reach(nums, target):
    def dfs(path, i):
        if len(nums) == i:
            return sum(path) == target

        path.append(nums[i])
        if dfs(path, i + 1):
            return True
        path.pop()

        path.append(-nums[i])
        if dfs(path, i + 1):
            return True
        path.pop()

        return False

    return dfs([], 0)
