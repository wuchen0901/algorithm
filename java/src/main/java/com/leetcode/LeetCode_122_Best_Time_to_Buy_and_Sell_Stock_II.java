package com.leetcode;

public class LeetCode_122_Best_Time_to_Buy_and_Sell_Stock_II {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[] hold = new int[n + 1];
        int[] sold = new int[n + 1];
        hold[0] = Integer.MIN_VALUE;
        //      7       5       4           8
        // hold -INF    -7     -5           -5, 0 - 4
        // sold 0       0       0, -7 + 5   0, -5 + 8
        for (int i = 1; i < n + 1; i++) {
            int price = prices[i - 1];
            hold[i] = Math.max(hold[i - 1], sold[i - 1] - price);
            sold[i] = Math.max(sold[i - 1], hold[i - 1] + price);
        }

        return sold[n];
    }
}
