package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode_15_3Sum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        // I would like to use two nested loops.
        // The outer loop fixes the first number.
        // The outer loop only needs to iterate up to nums.length - 2

        List<List<Integer>> result = new ArrayList<>();
        // To avoid duplicates, I need to skip over duplicate values whenever I move any of the three indices.
        for (int i = 0; i < nums.length - 2; i++) {
            // For each iteration of the outer loop, we use two pointers to find the remaining two numbers.
            // We only need to search for the remaining two numbers to the right of the first number.

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < 0) {
                    left++;
                } else if (0 < sum) {
                    right--;
                } else {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    while (left < right && nums[left - 1] == nums[left]) {
                        left++;
                    }
                    right--;
                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                }
            }

            while (i + 1 < nums.length - 2 && nums[i] == nums[i + 1]) {
                i++;
            }
        }

        // I always make syntax mistakes in statements like this.
        return result;
    }
}
