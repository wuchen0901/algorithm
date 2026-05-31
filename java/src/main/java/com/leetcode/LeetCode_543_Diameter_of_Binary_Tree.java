package com.leetcode;

import com.leetcode.common.TreeNode;

public class LeetCode_543_Diameter_of_Binary_Tree {
    public int diameterOfBinaryTree(TreeNode root) {
        // I create a variable called diameter first.
        // I define diameter as an array.
        // I define diameter as a one-element array.
        int[] diameter = new int[1];
        height(root, diameter);
        return diameter[0];
    }

    int height(TreeNode root, int[] diameter) {
        if (root == null) {
            return 0;
        }

        int l = height(root.left, diameter);
        int r = height(root.right, diameter);

        diameter[0] = Math.max(diameter[0], l + r);

        return Math.max(l, r) + 1;
    }
}
