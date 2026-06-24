package com.leetcode;

public class LeetCode_198_House_Robber {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] rob = new int[n + 1];
        int[] skip = new int[n + 1];
        // 1     2  3          1
        // 1 2 + 0  1 + 0 + 3  2 + 0 + 1
        // 0 1 + 0  2 + 0      1 + 0 + 3
        for (int i = 1; i <= n; i++) {
            int num = nums[i - 1];
            rob[i] = skip[i - 1] + num;
            skip[i] = Math.max(rob[i - 1], skip[i - 1]);
        }

        return Math.max(rob[n], skip[n]);
    }
}
