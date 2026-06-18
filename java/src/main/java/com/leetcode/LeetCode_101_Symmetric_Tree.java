package com.leetcode;

import com.leetcode.common.TreeNode;

public class LeetCode_101_Symmetric_Tree {
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root.left, root.right);
    }

    boolean isMirror(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        } else if (left != null && right != null && left.val == right.val) {
            return isMirror(left.left, right.right) && isMirror(left.right, right.left);
        } else {
            return false;
        }
    }
}
