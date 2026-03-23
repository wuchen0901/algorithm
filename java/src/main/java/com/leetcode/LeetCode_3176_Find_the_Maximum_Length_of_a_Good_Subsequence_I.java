package com.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class LeetCode_3176_Find_the_Maximum_Length_of_a_Good_Subsequence_I {
    public int maximumLength(int[] nums, int k) {
        Map<Integer, int[]> dp = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int[] row = new int[k + 1];
            Arrays.fill(row, 1);
            for (Map.Entry<Integer, int[]> entry : dp.entrySet()) {
                int[] value = entry.getValue();
                for (int j = 0; j < k + 1; j++) {
                    if (entry.getKey() == nums[i]) {
                        row[j] = Math.max(row[j], value[j] + 1);
                    } else {
                        if (0 <= j - 1) {
                            row[j] = Math.max(row[j], value[j - 1] + 1);
                        }
                    }
                }
            }

            dp.put(nums[i], row);
        }

        int max = 0;
        for (Map.Entry<Integer, int[]> entry : dp.entrySet()) {
            max = Math.max(max, entry.getValue()[k]);
        }

        return max;
    }

    public static void main(String[] args) {
        LeetCode_3176_Find_the_Maximum_Length_of_a_Good_Subsequence_I solution = new LeetCode_3176_Find_the_Maximum_Length_of_a_Good_Subsequence_I();
        int i = solution.maximumLength(new int[]{59, 60, 58, 59, 58, 58}, 2);
        System.out.println(i);
    }
}
