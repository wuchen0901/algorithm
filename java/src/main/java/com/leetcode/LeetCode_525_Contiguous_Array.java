package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_525_Contiguous_Array {
    public int findMaxLength(int[] nums) {
        int maxLength = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, 0);
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i] * 2 - 1;
            if (map.containsKey(sum)) {
                maxLength = Math.max(maxLength, i - map.get(sum) + 1);
            } else {
                map.put(sum, i + 1);
            }
        }

        return maxLength;
    }
}
