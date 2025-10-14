package com.leetcode;

class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int sum = 0;
        int l = 0;
        int r = 0;
        int minimalLength = Integer.MAX_VALUE;
        while (r < nums.length) {
            while (r < nums.length && sum < target) {
                sum += nums[r];
                r++;
            }
            // [2,3,1,2,4,3]
            //          ^
            while (target <= sum) {
                if (r - l < minimalLength) {
                    minimalLength = r - l;
                }
                sum -= nums[l];
                l += 1;
            }
            // [2,3,1,2,4,3]
            //    ^     ^
            // sum < target
        }

        return minimalLength == Integer.MAX_VALUE ? 0 : minimalLength;
    }
}