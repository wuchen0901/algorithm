package com.leetcode;

public class LeetCode_162_Find_Peak_Element {
    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (mid + 1 < nums.length && nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
