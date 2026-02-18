package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_494_Target_Sum {

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