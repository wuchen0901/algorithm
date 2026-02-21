package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_494_Target_Sum {

    public int findTargetSumWays2(int[] nums, int target) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        if (sum < Math.abs(target)){
            return 0;
        }

        final int offset = sum;
        final int width = 2 * sum + 1;

        int[][] dp = new int[nums.length + 1][width];
        dp[0][offset] = 1; // using 0 numbers, only sum=0 is reachable

        for (int i = 1; i <= nums.length; i++) {
            int num = nums[i - 1];
            for (int j = 0; j < width; j++) {
                // j = 0, 1, 2, 3

                // nums = [2, 2]
                // sum = 4,
                // 0   1  2  3  4 5 6 7 8
                // -4 -3 -2 -1  0 1 2 3 4
                //
                //              1
                //        1         1
                // 1            2       1
                if (j + num < width) {
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