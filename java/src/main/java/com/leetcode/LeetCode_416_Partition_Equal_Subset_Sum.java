package com.leetcode;

public class LeetCode_416_Partition_Equal_Subset_Sum {
    public boolean canPartition(int[] nums) {
        int sum = 0;

        for (int k : nums) {
            sum += k;
        }

        if (sum % 2 == 1) { // odd
            return false;
        }

        int target = sum / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        // 1, 5, 11, 5
        // 0 1 2 3 4 5 6 7 8 9 10 11
        // t t       t t        t  t
        for (int num : nums) {
            for (int j = dp.length - 1; 0 <= j - num; j--) {
                dp[j] |= dp[j - num];
            }
        }

        return dp[target];
    }
}
