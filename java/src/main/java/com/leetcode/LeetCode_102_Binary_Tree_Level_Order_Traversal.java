package com.leetcode;

import com.leetcode.common.TreeNode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class LeetCode_102_Binary_Tree_Level_Order_Traversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.offer(root);

        List<List<Integer>> result = new ArrayList<>();
        while (!deque.isEmpty()) {
            int size = deque.size();
            ArrayList<Integer> integers = new ArrayList<>(size);
            for (int i = 0; i < size; i++) {
                TreeNode node = deque.poll();
                integers.add(node.val);
                if (node.left != null) deque.offer(node.left);
                if (node.right != null) deque.offer(node.right);
            }
            result.add(integers);
        }
        return result;
    }
}

//return new ArrayList<>(new ArrayList<>(0))
//integers.add 下标