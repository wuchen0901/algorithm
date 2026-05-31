package com.leetcode;

import com.leetcode.common.TreeNode;

public class LeetCode_112_Path_Sum {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }

        return dfs(root, 0, targetSum);
    }

    boolean dfs(TreeNode root, int currentSum, int targetSum) {
        if (root == null) {
            return false;
        }

        currentSum += root.val;

        if (root.left == null && root.right == null) {
            return currentSum == targetSum;
        }

        return dfs(root.left, currentSum, targetSum) || dfs(root.right, currentSum, targetSum);
    }
}
