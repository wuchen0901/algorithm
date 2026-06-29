package com.leetcode;

public class LeetCode_123 {
    public int maxProfit(int[] prices) {
        int n = prices.length;

        int K = 2;

        int[][] hold = new int[n + 1][K + 1];
        int[][] sold = new int[n + 1][K + 1];

        // hold
        // -∞   -∞  -∞
        //

        // sold
        // 0    0   0
        //

        for (int i = 0; i < K + 1; i++) {
            hold[0][i] = Integer.MIN_VALUE;
        }

        for (int i = 1; i < n + 1; i++) {
            int price = prices[i - 1];
            for (int j = 1; j < K + 1; j++) {
                hold[i][j] = Math.max(hold[i - 1][j], sold[i - 1][j - 1] - price);
                sold[i][j] = Math.max(sold[i - 1][j], hold[i - 1][j] + price);
            }
        }

        return sold[n][K];
    }
}
