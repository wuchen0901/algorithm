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

        int leftContribution = dfs(root.left);
        int rightContribution = dfs(root.right);

        if (root.left != null && root.left.val == root.val) {
            leftContribution += 1;
        } else {
            leftContribution = 0;
        }

        if (root.right != null && root.right.val == root.val) {
            rightContribution += 1;
        } else {
            rightContribution = 0;
        }

        maxLength = Math.max(maxLength, leftContribution + rightContribution);

        return Math.max(leftContribution, rightContribution);
        // Now I'll dry-run my solution.
    }
}
