package com.leetcode;

import com.leetcode.common.TreeNode;

public class LeetCode_108 {
    public TreeNode sortedArrayToBST(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }

    TreeNode build(int[] nums, int l, int r) {
        if (r < l) {
            return null;
        }

        int middle = l + (r - l) / 2;

        TreeNode node = new TreeNode(nums[middle]);

        node.left = build(nums, l, middle - 1);
        node.right = build(nums, middle + 1, r);

        return node;
    }
}
