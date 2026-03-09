package com.leetcode;

public class LeetCode_643_Maximum_Average_Subarray_I {
    public double findMaxAverage(int[] nums, int k) {
        int runningSum = 0;
        int maxRunningSum = Integer.MIN_VALUE;

        for (int r = 0; r < nums.length; r++) {
            runningSum += nums[r];
            int l = r - k;
            if (-1 <= l) {
                maxRunningSum = Math.max(maxRunningSum, runningSum);
                if (0 <= l) {
                    runningSum -= nums[l];
                }
            }
        }

        return (double) maxRunningSum / k;
    }
}
