from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self._update_fenwick_tree(i + 1, num)

    def _update_fenwick_tree(self, i: int, delta: int):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def update(self, index: int, val: int):
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update_fenwick_tree(index + 1, delta)

    def query(self, i: int) -> int:
        r = 0
        while i > 0:
            r += self.tree[i]
            i -= i & -i
        return r

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)