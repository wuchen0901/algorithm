package com.leetcode;

import java.util.HashSet;
import java.util.Set;

public class LeetCode_645_Set_Mismatch {
    public int[] findErrorNums(int[] nums) {
        Set<Integer> remaining = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            remaining.add(i + 1);
        }
        int duplicate = 0;
        for (int num : nums) {
            if (remaining.contains(num)) {
                remaining.remove(num);
            } else {
                duplicate = num;
            }
        }

        return new int[]{duplicate, remaining.iterator().next()};
    }
}
