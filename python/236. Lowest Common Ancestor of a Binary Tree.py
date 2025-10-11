from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parents = {root: None}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)

        pointer_p, pointer_q = p, q
        while pointer_p != pointer_q:
            pointer_p = parents[pointer_p] if pointer_p else q
            pointer_q = parents[pointer_q] if pointer_q else p

        return pointer_p
