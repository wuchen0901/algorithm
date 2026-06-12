package com.leetcode;

import java.util.Arrays;

public class LeetCode_300_Longest_Increasing_Subsequence {
    public int lengthOfLISLinearSearch(int[] nums) {
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


    public int lengthOfLIS(int[] nums) {
        int[] lis = new int[nums.length];
        for (int i = 0; i < lis.length; i++) {
            lis[i] = 10000 + 1;
        }
        // [10,9,2,4,5,3,7,101,18]
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
            int i = binarySearch(lis, num);
            lis[i] = num;
            maxLength = Math.max(maxLength, i + 1);
        }

        return maxLength;
    }

    private int binarySearch(int[] tails, int target) {
        int left = 0;
        int right = tails.length;
        // left is inclusive, right is exclusive
        // half-open interval

        // 1 3 5 target: 2;
        // left: 0, right = 3;
        // mid: 1
        //

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (target < tails[mid]) {
                right = mid;
            } else if (tails[mid] < target) {
                left = mid + 1;
            } else { // equal
                right = mid;
            }
        }

        return left;
    }
}
