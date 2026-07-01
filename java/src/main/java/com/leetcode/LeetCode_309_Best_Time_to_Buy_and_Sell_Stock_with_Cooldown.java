package com.leetcode;

public class LeetCode_309_Best_Time_to_Buy_and_Sell_Stock_with_Cooldown {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[] hold = new int[n + 1];
        int[] sold = new int[n + 1];

        hold[0] = Integer.MIN_VALUE / 2;

        for (int i = 1; i < n + 1; i++) {
            int price = prices[i - 1];

            if (0 <= i - 2) {
                hold[i] = Math.max(hold[i - 1], sold[i - 2] - price);
            } else {
                hold[i] = Math.max(hold[i - 1], -price);
            }

            sold[i] = Math.max(sold[i - 1], hold[i - 1] + price);
        }

        return sold[n];
    }
}
