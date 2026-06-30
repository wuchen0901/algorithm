package com.leetcode;

public class LeetCode_188_Best_Time_to_Buy_and_Sell_Stock_IV {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        int[][] hold = new int[n + 1][k + 1];
        int[][] sold = new int[n + 1][k + 1];

        for (int i = 0; i < k + 1; i++) {
            hold[0][i] = Integer.MIN_VALUE;
        }

        for (int i = 1; i < n + 1; i++) {
            int price = prices[i - 1];
            for (int j = 1; j < k + 1; j++) {
                hold[i][j] = Math.max(hold[i - 1][j], sold[i - 1][j - 1] - price);
                sold[i][j] = Math.max(sold[i - 1][j], hold[i - 1][j] + price);
            }
        }

        return sold[n][k];
    }
}
