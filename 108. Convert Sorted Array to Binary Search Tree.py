# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if length == 0:
            return None

        middle = length // 2
        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[0:middle])
        root.right = self.sortedArrayToBST(nums[middle + 1:length])
        return root


if __name__ == '__main__':
    bst = Solution().sortedArrayToBST([4])
    bst = Solution().sortedArrayToBST([3, 6, 9])
    bst = Solution().sortedArrayToBST([2, 5])
    bst = Solution().sortedArrayToBST([2, 5, 6, 8, 9])

