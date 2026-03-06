package com.leetcode;

public class LeetCode_2585_Number_of_Ways_to_Earn_Points {
    public int waysToReachTarget(int target, int[][] types) {
        int mod = 1_000_000_007;
        long[][] dp = new long[types.length + 1][target + 1];

        for (int i = 0; i < types.length + 1; i++) {
            dp[i][0] = 1;
        }

        for (int i = 1; i < types.length + 1; i++) {
            int count = types[i - 1][0];
            int mark = types[i - 1][1];
            for (int j = 1; j < target + 1; j++) {
                dp[i][j] = dp[i - 1][j];
                for (int c = 1; c <= count; c++) {
                    if (0 <= j - c * mark) {
                        dp[i][j] += dp[i - 1][j - c * mark];
                    }
                }
                dp[i][j] %= mod;
            }
        }

        return (int) dp[types.length][target];
    }
}
