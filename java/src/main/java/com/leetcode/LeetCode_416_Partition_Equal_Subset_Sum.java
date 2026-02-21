package com.leetcode;

public class LeetCode_416_Partition_Equal_Subset_Sum {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        if (sum % 2 == 1) { // odd
            return false;
        }

        int[][] dp = new int[nums.length + 1][sum / 2 + 1];

        for (int i = 0; i < nums.length; i++) {
            dp[i][0] = 1;
        }

        // todo  背包问题不是用dfs解决的吗？
        //
        // 1 5 5  -  11
        //     0 1 2 3 4 5 6 7 8 9 10
        //     1
        // 0 3       1
        // 1 2     1     1
        // 2 4         1   1     1
        for (int i = 1; i <= nums.length; i++) {
            int num = nums[i - 1];
            for (int j = 1; j <= sum / 2; j++) {
                if (0 <= j - num) {
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[nums.length][sum / 2] != 0;
    }
}
