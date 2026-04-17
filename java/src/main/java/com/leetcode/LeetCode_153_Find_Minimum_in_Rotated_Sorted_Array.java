package com.leetcode;

public class LeetCode_153_Find_Minimum_in_Rotated_Sorted_Array {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // 1 2 3 4 5
            // 5 1 2 3 4
            // 4 5 1 2 3
            if (nums[mid] < nums[right]) {
                right = mid;
            } else

                // 9
                // 1 2 3 4 5
                // 3 4 5 1 2
                // 2 3 4 5 1
                if (nums[left] <= nums[mid]) {
                    // 1 2 3 4 5
                    if (nums[left] < nums[right]) {
                        return left;
                        // 3 4 5 1 2
                    } else if (nums[left] > nums[right]) {
                        left = mid + 1;
                    }
                }
        }

        return nums[left];
    }
}
