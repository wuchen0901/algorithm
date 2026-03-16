package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_992_Subarrays_with_K_Different_Integers {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }

    private int atMost(int[] nums, int k) {
        Map<Integer, Integer> window = new HashMap<>();
        int ans = 0;
        int l = 0;
        for (int r = 0; r < nums.length; r++) {
            window.put(nums[r], window.getOrDefault(nums[r], 0) + 1);
            while (k < window.size()) {
                window.compute(nums[l], (ch, freq) -> freq == 1 ? null : freq - 1);
                l++;
            }

            ans += r - (l - 1);
        }

        return ans;
    }
}
