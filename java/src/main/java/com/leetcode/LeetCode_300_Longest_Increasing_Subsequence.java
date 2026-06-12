package com.leetcode;

import java.util.Arrays;

public class LeetCode_300_Longest_Increasing_Subsequence {
    public int lengthOfLIS(int[] nums) {
        int[] lis = new int[nums.length];
        Arrays.fill(lis, 10000 + 1);
        // [10, 9, 2, 4, 5, 3, 7, 101, 18]
        // 10
        // 9
        // 2
        // 2 4
        // 2 4 5
        // 2 3 5
        // 2 3 7
        // 2 3 7 101
        // 2 3 7 18

        int maxLength = 0;
        for (int num : nums) {
            int i = 0;
            while (lis[i] < num) {
                i++;
            }
            lis[i] = num;
            maxLength = Math.max(maxLength, i + 1);
        }

        return maxLength;
    }
}
