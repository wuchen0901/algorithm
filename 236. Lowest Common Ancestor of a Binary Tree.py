from collections import deque, defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([root])
        parents = {root: None}
        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
                parents[node.left] = node
            if node.right:
                queue.append(node.right)
                parents[node.right] = node

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]

        return q
