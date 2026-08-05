package com.leetcode;

public class LeetCode_704_Binary_Search {
    public int searchHalfOpenInterval(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (target < nums[mid]) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return left < nums.length && nums[left] == target ? left : -1;
    }

    // Time complexity: O(log n) — the search interval halves each iteration.
    // Auxiliary space: O(1) — only left, right, and mid are stored.
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (target < nums[mid]) {
                right = mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left < nums.length && nums[left] == target ? left : -1;
    }
}
