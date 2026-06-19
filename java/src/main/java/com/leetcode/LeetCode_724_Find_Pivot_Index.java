package com.leetcode;

public class LeetCode_724_Find_Pivot_Index {
    public int pivotIndex(int[] nums) {
        int[] prefixSum = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        //            [1, 7, 3,  6,  5,  6]
        // i: 3
        // prefixSum: [0, 1, 8, 11, 17, 22, 28]
        for (int i = 0; i < nums.length; i++) {
            if (prefixSum[i] == prefixSum[nums.length] - prefixSum[i + 1]) {
                return i;
            }
        }

        return -1;
    }
}
