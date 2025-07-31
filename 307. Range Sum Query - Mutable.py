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


# Segment Tree implementation
class NumArraySegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n * 4)
        self.nums = nums[:]
        self._build(0, 0, self.n - 1)

    def _build(self, node: int, l: int, r: int):
        if l == r:
            self.tree[node] = self.nums[l]
            return
        mid = (l + r) // 2
        self._build(2 * node + 1, l, mid)
        self._build(2 * node + 2, mid + 1, r)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index: int, val: int):
        self._update(0, 0, self.n - 1, index, val)

    def _update(self, node: int, l: int, r: int, index: int, val: int):
        if l == r:
            self.tree[node] = val
            return
        mid = (l + r) // 2
        if index <= mid:
            self._update(2 * node + 1, l, mid, index, val)
        else:
            self._update(2 * node + 2, mid + 1, r, index, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def sumRange(self, left: int, right: int) -> int:
        return self._sumRange(0, 0, self.n - 1, left, right)

    def _sumRange(self, node: int, l: int, r: int, left: int, right: int) -> int:
        if right < l or r < left:
            return 0
        if left <= l and r <= right:
            return self.tree[node]
        mid = (l + r) // 2
        return self._sumRange(2 * node + 1, l, mid, left, right) + self._sumRange(2 * node + 2, mid + 1, r, left, right)