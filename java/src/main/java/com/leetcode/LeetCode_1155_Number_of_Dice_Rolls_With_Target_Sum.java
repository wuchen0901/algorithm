package com.leetcode;

public class LeetCode_1155_Number_of_Dice_Rolls_With_Target_Sum {
    public int numRollsToTarget(int n, int k, int target) {
        int MOD = 1000000007;

        int[][] dp = new int[n + 1][target + 1];

        dp[0][0] = 1;

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < target + 1; j++) {
                for (int dice = 1; dice <= k; dice++) {
                    if (0 <= j - dice) {
                        dp[i][j] += dp[i - 1][j - dice];
                        dp[i][j] %= MOD;
                    }
                }
            }
        }

        return dp[n][target];
    }
}
