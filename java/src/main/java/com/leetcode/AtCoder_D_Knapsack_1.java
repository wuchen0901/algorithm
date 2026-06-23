package com.leetcode;

public class AtCoder_D_Knapsack_1 {
    int maxValue(int[] weights, int[] values, int capacity) {
        int n = weights.length;
        int[][] dp = new int[n + 1][capacity + 1];

        // weights: 1 2 4
        // values : 2 5 9
        //
        // dp
        // 0 1  2  3  4  5  6  7  8
        // 0 0  0  0  0  0  0  0  0
        // 0 2  2  2  2  2  2  2  2
        // 0 2  5  7  7  7  7  7  7
        // 0 2  5  7、9  9
        for (int i = 1; i <= n; i++) {
            int w = weights[i - 1];
            int v = values[i - 1];
            for (int j = 1; j <= capacity; j++) {
                dp[i][j] = dp[i - 1][j];
                if (w <= j) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - w] + v);
                }
            }
        }

        return dp[n][capacity];
    }
}
