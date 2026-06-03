package com.leetcode;

import com.leetcode.common.TreeNode;

public class LeetCode_124_Binary_Tree_Maximum_Path_Sum {
    // I maintain a global variable to keep track of the maximum path sum.
    // The maximum number of nodes is thirty thousand, and the minimum value of each node is negative one thousand, so I initialize maxSum to thirty thousand times negative one thousand.
    int maxSum = 30000 * -1000;

    public int maxPathSum(TreeNode root) {
        maxGain(root);
        return maxSum;
    }

    // The first idea that came to mind was to use DFS to traverse the tree.
    // Based on this DFS, I'll add a parameter to keep track of the maximum path sum.
    // I change the return value of the DFS function to the maximum path sum of each subtree.
    // So I decided to change the name of the DFS function to maxGain.
    int maxGain(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftGain = maxGain(root.left);
        int rightGain = maxGain(root.right);
        maxSum = Math.max(maxSum, leftGain + root.val + rightGain);

        return Math.max(0, Math.max(leftGain, rightGain) + root.val);
    }
}
