package com.leetcode;

class LeetCode_209_Minimum_Size_Subarray_Sum {
    public int minSubArrayLenV2(int target, int[] nums) {
        long sum = 0;
        int l = 0, r = 0;
        int minimalLength = Integer.MAX_VALUE;
        while (r < nums.length) {
            sum += nums[r];
            r++;
            // Enter the loop when
            // [2,3,1,2,4,3]
            //          ^
            // I am following the half-open interval convention,
            // which means the left endpoint is inclusive and the right endpoint is exclusive.
            while (target <= sum) {
                minimalLength = Math.min(minimalLength, r - l);
                sum -= nums[l];
                l++;
            }
            // After exiting the while loop, sum < target
            // [2,3,1,2,4,3]
            //    ^     ^
        }

        return minimalLength == Integer.MAX_VALUE ? 0 : minimalLength;
    }

    public int minSubArrayLenV1(int target, int[] nums) {
        int sum = 0;
        int l = 0;
        int r = 0;
        int minimalLength = Integer.MAX_VALUE;
        while (r < nums.length) {
            while (r < nums.length && sum < target) {
                sum += nums[r];
                r++;
            }
            // Enter the loop when
            // [2,3,1,2,4,3]
            //          ^
            // I am following the half-open interval convention,
            // which means the left endpoint is inclusive and the right endpoint is exclusive.
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