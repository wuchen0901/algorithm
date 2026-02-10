package com.leetcode;

public class LeetCode_322_Coin_Change {
    public int coinChange(int[] coins, int amount) {
        int inf = amount + 1;
        int[][] dp = new int[coins.length + 1][amount + 1];
        for (int j = 1; j < dp[0].length; j++) {
            dp[0][j] = inf;
        }

        for (int i = 1; i < dp.length; i++) {
            for (int j = 1; j < dp[i].length; j++) {
                int coin = coins[i - 1];
                if (j - coin >= 0) {
                    dp[i][j] = Math.min(dp[i][j - coin] + 1, dp[i - 1][j]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[coins.length][amount] >= inf ? -1 : dp[coins.length][amount];
    }

    public static void main(String[] args) {
        int[][] ints = new int[3][5];
        int index = 0;
        for (int i = 0; i < ints.length; i++) {
            for (int j = 0; j < ints[i].length; j++) {
                ints[i][j] = index;
                index++;
            }
        }
        System.out.println(ints);
    }
}
