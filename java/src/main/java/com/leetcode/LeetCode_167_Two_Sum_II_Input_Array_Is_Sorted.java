package com.leetcode;

public class LeetCode_167_Two_Sum_II_Input_Array_Is_Sorted {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;

        while (l < r) {
            if (numbers[l] + numbers[r] < target) {
                l++;
            } else if (target < numbers[l] + numbers[r]) {
                r--;
            } else {
                return new int[] { l + 1, r + 1 };
            }
        }

        return new int[2];
    }
}
