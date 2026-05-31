package com.leetcode;

import com.leetcode.common.TreeNode;

public class LeetCode_110_Balanced_Binary_Tree {
    public boolean isBalanced(TreeNode root) {
        return dfs(root) != -1;
    }

    int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int l = dfs(root.left);
        int r = dfs(root.right);
        if (l == -1 || r == -1) {
            return -1;
        }
        if (Math.abs(l - r) <= 1) {
            return Math.max(l, r) + 1;
        } else {
            return -1;
        }
    }
}
