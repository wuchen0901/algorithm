package com.leetcode;

public class LeetCode_377_Combination_Sum_IV {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];

        dp[0] = 1;

        for (int i = 1; i < target + 1; i++) {
            for (int n : nums) {
                if (0 <= i - n) {
                    dp[i] += dp[i - n];
                }
            }
        }

        return dp[target];
    }
}
