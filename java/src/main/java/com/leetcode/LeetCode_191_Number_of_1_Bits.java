package com.leetcode;

public class LeetCode_191_Number_of_1_Bits {
    public int hammingWeight(int n) {
        int count = 0;

        while (n != 0) {
            n &= n - 1;
            count++;
        }

        return count;
    }
}
