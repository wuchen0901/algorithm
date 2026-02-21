package com.leetcode;

public class LeetCode_518_Coin_Change_II {
    //      0   1   2   3   4   5   6
    // 1    0   1   2   3   4   5   6   `1 + 1 + 1 + 1 + 1 + 1`
    // 6    0   1   2   3   4   5   1   `6`
    // 2    0   1   1   2   2   3   3   `1 + 1 + 1 + 1 + 2`
    //                                  `2 + 2 + 2`

    // HashMap
    // key  ->  value
    // 0    ->  0
    // 2    ->  1
    // 4    ->  2
    // 6    ->  3

    // + 4
    // 0    ->  0
    // 2    ->  1
    // 4    ->  1
    // 6    ->  2

    // + 3
    // 0    ->  0
    // 2    ->  1
    // 3    ->  1
    // 4    ->  1
    // 5    ->  2
    // 6    ->  2


    //      0   2   3   4   5   6
    //  2   0   1       2       3
    //  4   0           1       2
    //  3   0   1   1   1   2   2
    //

    // Array, key sorted, 0 based, continuously HashMap
    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length + 1][amount + 1];

        // initial
        for (int i = 0; i < coins.length + 1; i++) {
            dp[i][0] = 1;
        }
        // dp[i][0] = 1

        // coin [2, 1, 5]
        //                  0   1   2   3   4   5
        //  0   []          _   0   0   0   0   0
        //  1   [2]         1   0   1   0   1   0
        //  2   [2, 1]      1   1   2   2   3   3
        //  3   [2, 1, 5]   1   1   2   2   3   4

        for (int i = 1; i < coins.length + 1; i++) {
            for (int j = 1; j < amount + 1; j++) {
                int coin = coins[i - 1];
                if (j - coin >= 0) {
                    dp[i][j] = dp[i][j - coin] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[coins.length][amount];
    }

    // 0/1 Knapsack version: each coin can be used at most once
    public int change01(int amount, int[] coins) {
        int[][] dp = new int[coins.length + 1][amount + 1];

        // base case
        for (int i = 0; i <= coins.length; i++) {
            dp[i][0] = 1;
        }

        for (int i = 1; i <= coins.length; i++) {
            int coin = coins[i - 1];
            for (int j = 1; j <= amount; j++) {
                // not use current coin
                dp[i][j] = dp[i - 1][j];

                // use current coin (only once)
                if (j - coin >= 0) {
                    dp[i][j] += dp[i - 1][j - coin];
                }
            }
        }

        return dp[coins.length][amount];
    }
}
