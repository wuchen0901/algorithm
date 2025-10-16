package com.leetcode;

import com.leetcode.common.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_144_Binary_Tree_Preorder_Traversal {
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<>();
        dfs(root, result);
        return result;
    }

    private void dfs(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        result.add(node.val);
        dfs(node.left, result);
        dfs(node.right, result);
    }
}
