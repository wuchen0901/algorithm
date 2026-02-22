package com.leetcode;

public class LeetCode_416_Partition_Equal_Subset_Sum {
    public boolean canPartition(int[] nums) {
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }

        if (sum %2 == 1) {
            return false;
        }

        int target = sum / 2;

        int[][] dp = new int[nums.length + 1][target + 1];

        dp[0][0] = 1;

        //              0   1   2   3   4   5   6
        //  []          1 // TODO: 为什么这里是 1 ？
        //  [2]         1       1
        //  [2, 3]      1       1   1       1
        //  [2, 3, 1]   1   1   1   2   1   1   1
        for (int i = 1; i < nums.length + 1; i++) {
            int num = nums[i - 1];
            for (int j = 0; j < target + 1; j++) {
                if (0 <= j - num) {
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }

            }
        }

        return dp[nums.length][target] != 0;
    }
}
