package com.leetcode;

import com.leetcode.common.TreeNode;

public class LeetCode_687_Longest_Univalue_Path {
    // I use maxLength to keep track of the longest path found so far.
    int maxLength = 0;

    public int longestUnivaluePath(TreeNode root) {
        dfs(root);
        return maxLength;
    }

    // The first idea that comes to mind is to use DFS to traverse the tree.
    // In the next step, I will change the return value to the length of the path.
    int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftLength = dfs(root.left);
        int rightLength = dfs(root.right);

        if (root.left != null && root.left.val == root.val && root.right != null && root.right.val == root.val) {
            maxLength = Math.max(maxLength, leftLength + 1 + rightLength + 1);
            return Math.max(leftLength, rightLength) + 1;
        } else if (root.left != null && root.left.val == root.val) {
            maxLength = Math.max(maxLength, leftLength + 1);
            return leftLength + 1;
        } else if (root.right != null && root.right.val == root.val) {
            maxLength = Math.max(maxLength, rightLength + 1);
            return rightLength + 1;
        } else {
            return 0;
        }

        // Now I'll dry-run my solution.
    }
}
