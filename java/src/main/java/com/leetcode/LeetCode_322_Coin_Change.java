package com.leetcode;

public class LeetCode_322_Coin_Change {
    public int coinChange(int[] coins, int amount) {
        int[][] dp = new int[coins.length + 1][amount + 1];

        int inf = amount + 1;

        for (int j = 0; j < amount + 1; j++) {
            dp[0][j] = inf;
        }
        //              0   1   2   3   4   5   6
        // 0 []
        // 1 [2]        0  +∞   1  +∞   2  +∞   2
        // 2 [2, 1]
        // 3 [2, 1, 5]
        for (int i = 1; i < coins.length + 1; i++) {
            int coin = coins[i - 1];
            for (int j = 1; j < amount + 1; j++) {
                if (0 <= j - coin) {
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - coin] + 1);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[coins.length][amount] < inf ? dp[coins.length][amount] : -1;
    }
}
