package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode_15_3Sum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> results = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (1 <= i && nums[i - 1] == nums[i]) {
                continue;
            }
            int l = i + 1;
            int r = nums.length - 1;

            while (l < r) {
                if (nums[i] + nums[l] + nums[r] < 0) {
                    l++;
                } else if (0 < nums[i] + nums[l] + nums[r]) {
                    r--;
                } else {
                    results.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    do {
                        l++;
                    } while (l < r && nums[l - 1] == nums[l]);
                    do {
                        r--;
                    } while (l < r && nums[r] == nums[r + 1]);
                }
            }
        }

        return results;
    }
}
