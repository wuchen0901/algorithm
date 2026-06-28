package com.leetcode;

import java.util.Arrays;

public class LeetCode_121_Best_Time_to_Buy_and_Sell_Stock {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[] hold = new int[n + 1];
        int[] sold = new int[n + 1];

        Arrays.fill(hold, Integer.MIN_VALUE);

        // [7,    1,   5,   3,6,4]
        //  -inf -7  , -1  -5 -3 -6 -4
        //  -inf -inf, -6,  4 4  4  4
        for (int i = 1; i < n + 1; i++) {
            int price = prices[i - 1];

            hold[i] = Math.max(hold[i - 1], -price);
            // i: 1
            // hold[1]: -7

            sold[i] = Math.max(sold[i - 1], hold[i - 1] + price);

        }

        return sold[n] == Integer.MIN_VALUE ? 0 : sold[n];
    }
}
