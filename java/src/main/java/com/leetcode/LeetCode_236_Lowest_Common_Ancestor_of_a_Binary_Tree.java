package com.leetcode;

import com.leetcode.common.TreeNode;

public class LeetCode_236_Lowest_Common_Ancestor_of_a_Binary_Tree {
    TreeNode lca;

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        //   1
        // 2
        // p: 1 q: 2

        //   1
        // 2   3
        // p: 2 q: 3
        find(root, p, q);
        return lca;
    }

    boolean find(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return false;
        }

        // I made a mistake here, When I find these nodes, I should not stop traversing.
        // if (root == p || root == q) {
        //     return true;
        // }

        boolean foundInLeft = find(root.left, p, q);
        boolean foundInRight = find(root.right, p, q);

        if (foundInLeft && foundInRight) {
            lca = root;
        } else if ((root == p || root == q) && (foundInLeft || foundInRight)) {
            lca = root;
        }

        return foundInLeft || foundInRight || root == p || root == q;
    }
}
