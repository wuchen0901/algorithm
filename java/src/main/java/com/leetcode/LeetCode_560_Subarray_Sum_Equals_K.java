package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_560_Subarray_Sum_Equals_K {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefix = new HashMap<>();
        prefix.put(0, 1);
        int sum = 0;
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];

            ans += prefix.getOrDefault(sum - k, 0);

            prefix.put(sum, prefix.getOrDefault(sum, 0) + 1);
        }

        return ans;
    }
}
