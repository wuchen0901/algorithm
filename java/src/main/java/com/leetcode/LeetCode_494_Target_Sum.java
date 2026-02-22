package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_494_Target_Sum {
    // todo 最标准（面试里最常见、最“模板化”）的解法：把 Target Sum 转成子集和计数问题（0/1 背包计数），再用 1D DP。
    public int findTargetSumWays2(int[] nums, int target) {
        // index        0   1   2   3   4   5   6
        //              -3  -2  -1  0   1   2   3   4   5   6   7
        //          []              1
        //         [1]          1       1
        //      [1, 1]      1       2       1
        //   [1, 1, 1]  1       3       3       1

        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }

        if (sum < Math.abs(target)) {
            return 0;
        }

        int offset = sum;

        int[][] dp = new int[nums.length + 1][sum * 2 + 1];

        dp[0][0 + offset] = 1;

        for (int i = 1; i < nums.length + 1; i++) {
            int num = nums[i - 1];
            for (int j = 0; j < sum * 2 + 1; j++) {
                if (j + num < sum * 2 + 1) {
                    dp[i][j] += dp[i - 1][j + num];
                }
                if (0 <= j - num) {
                    dp[i][j] += dp[i - 1][j - num];
                }
            }
        }

        return dp[nums.length][target + offset];
    }
    public int findTargetSumWays(int[] nums, int target) {
        // Quick infeasible check (optional but can save time/memory)
        int sum = 0;
        for (int x : nums) sum += Math.abs(x);
        if (Math.abs(target) > sum) return 0;

        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 1);

        for (int num : nums) {
            // Pre-size to reduce rehashing; worst-case distinct states ~ 2 * dp.size()
            Map<Integer, Integer> next = new HashMap<>(dp.size() * 2);

            for (Map.Entry<Integer, Integer> e : dp.entrySet()) {
                int s = e.getKey();
                int ways = e.getValue();

                int plus = s + num;
                int minus = s - num;

                next.put(plus, next.getOrDefault(plus, 0) + ways);
                next.put(minus, next.getOrDefault(minus, 0) + ways);
            }

            dp = next;
        }

        return dp.getOrDefault(target, 0);
    }
}