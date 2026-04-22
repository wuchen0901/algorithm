package com.leetcode;

public class LeetCode_238_Product_of_Array_Except_Self {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];

        left[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            left[i] = nums[i] * left[i - 1];
        }

        right[nums.length - 1] = nums[nums.length - 1];

        for (int i = nums.length - 2; 0 <= i; i--) {
            right[i] = nums[i] * right[i + 1];
        }

        int[] product = new int[nums.length];
        product[0] = right[1];
        product[nums.length - 1] = left[nums.length - 2];

        for (int i = 1; i < nums.length - 1; i++) {
            product[i] = left[i - 1] * right[i + 1];
        }

        return product;
    }
}
