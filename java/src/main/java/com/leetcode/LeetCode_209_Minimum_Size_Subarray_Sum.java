package com.leetcode;

class LeetCode_209_Minimum_Size_Subarray_Sum {
    public int minSubArrayLen(int target, int[] nums) {
        int runningSum = 0;
        int minLength = Integer.MAX_VALUE;
        int l = 0;
        for (int r = 0; r < nums.length; r++) {
            runningSum += nums[r];

            while (target <= runningSum) {
                minLength = Math.min(minLength, r - l + 1);

                runningSum -= nums[l];
                l++;
            }
        }

        return minLength == Integer.MAX_VALUE ? 0 : minLength;
    }
}