package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_992_Subarrays_with_K_Different_Integers {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }

    int atMost(int[] nums, int k) {
        int[] freq = new int[20000 + 1];
        int distinctCount = 0;
        int left = 0;
        int count = 0;
        for (int right = 0; right < nums.length; right++) {
            int rightNum = nums[right];
            if (freq[rightNum] == 0) {
                distinctCount++;
            }

            freq[rightNum]++;

            while (k < distinctCount) {
                int leftNum = nums[left];
                freq[leftNum]--;
                if (freq[leftNum] == 0) {
                    distinctCount--;
                }
                left++;
            }

            count += right - left + 1;
        }
        return count;
    }
}
