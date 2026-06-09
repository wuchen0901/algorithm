package com.leetcode;

import java.util.HashSet;
import java.util.Set;

public class LeetCode_128_Longest_Consecutive_Sequence {
    public int longestConsecutive(int[] nums) {

        Set<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        int longestLen = 0;

        for (Integer start : set) {
            if (!set.contains(start - 1)) {
                int end = start;
                while (set.contains(end)) {
                    end++;
                }

                longestLen = Math.max(longestLen, end - start);
            }
        }

        return longestLen;
    }
}
