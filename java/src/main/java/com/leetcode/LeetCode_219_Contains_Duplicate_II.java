package com.leetcode;

import java.util.HashSet;

public class LeetCode_219_Contains_Duplicate_II {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashSet<Integer> window = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (window.contains(nums[i])) {
                return true;
            }
            window.add(nums[i]);
            if (0 <= i - k) {
                window.remove(nums[i - k]);
            }

            if (k - 1 <= i) {
//                System.out.println("integers = " + integers);
            }
        }

        return false;
    }

    public static void main(String[] args) {
        LeetCode_219_Contains_Duplicate_II solution = new LeetCode_219_Contains_Duplicate_II();
        solution.containsNearbyDuplicate(new int[]{6, 2, 9, 5, 3, 1, 9}, 3);
    }
}
