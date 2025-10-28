package com.leetcode;

public class LeetCode_704_Binary_Search {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        // [8,12], target: 12
        // left = 0, right = 1
        while (left <= right) {
            int mid = (left + right) / 2; // 0

            if (target < nums[mid]) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else { // nums[mid] == target
                return mid;
            }
        }

        return -1;
    }
}
