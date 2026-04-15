package com.leetcode;

public class LeetCode_189_Rotate_Array {
    public void rotate(int[] nums, int k) {
        k %= nums.length;

        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    void reverse(int[] nums, int left, int right) {
        while (left < right) {
            int i = nums[right];
            nums[right] = nums[left];
            nums[left] = i;

            left++;
            right--;
        }
    }
}
