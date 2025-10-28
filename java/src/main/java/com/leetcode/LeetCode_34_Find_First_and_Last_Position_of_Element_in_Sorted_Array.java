package com.leetcode;

public class LeetCode_34_Find_First_and_Last_Position_of_Element_in_Sorted_Array {
    public int[] searchRange(int[] nums, int target) {
        return new int[]{findFirstOccurrence(nums, target), findLastOccurrence(nums, target)};
    }

    private int findFirstOccurrence(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        // [1,2,2,2], target: 2
        // left:  0, 2
        // right: 3
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target < nums[mid]) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else { // equal
                right = mid - 1;
            }
        }

        if (left < nums.length) {
            if (nums[left] == target) {
                return left;
            } else {
                return -1;
            }
        } else {
            return -1;
        }
    }

    private int findLastOccurrence(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        // [2,2,2], target: 1
        // left:  0, 2
        // right: 3
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target < nums[mid]) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else { // equal
                left = mid + 1;
            }
        }

        if (0 <= right) {
            if (nums[right] == target) {
                return right;
            } else {
                return -1;
            }
        } else {
            return -1;
        }
    }
}
