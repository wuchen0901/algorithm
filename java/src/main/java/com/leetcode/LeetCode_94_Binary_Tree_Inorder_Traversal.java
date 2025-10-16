package com.leetcode;

import com.leetcode.common.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_94_Binary_Tree_Inorder_Traversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        dfs(root, result);
        return result;
    }

    private void dfs(TreeNode node, List<Integer> result) {
        if (node == null) return;
        dfs(node.left, result);   // 1️⃣ visit left
        result.add(node.val);     // 2️⃣ visit root
        dfs(node.right, result);  // 3️⃣ visit right
    }
}