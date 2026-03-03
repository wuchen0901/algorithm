package com.leetcode;

public class LeetCode_377_Combination_Sum_IV {
    public int combinationSum4(int[] nums, int target) {
        int[][] dp = new int[nums.length + 1][target + 1];

        for (int i = 0; i < nums.length + 1; i++) {
            dp[i][0] = 1;
        }

        for (int i = 1; i < nums.length + 1; i++) {
            for (int j = 1; j < target + 1; j++) {
                for (int n : nums) {
                    if (0 <= j - n) {
                        dp[i][j] += dp[i][j - n];
                    }
                }
            }
        }

        return dp[nums.length][target];
    }
}
