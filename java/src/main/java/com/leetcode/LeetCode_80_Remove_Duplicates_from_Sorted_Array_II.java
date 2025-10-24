package com.leetcode;

public class LeetCode_80_Remove_Duplicates_from_Sorted_Array_II {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        if (n < 2) {
            return n;
        }

        // 1 1 2 2 3 3
        int fast = 2;
        int slow = 2;
        while (fast < n) {
            if (nums[slow - 2] != nums[fast]) {
                nums[slow] = nums[fast];
                slow++;
            }
            fast++;
        }

        return slow;
    }

    public static void main(String[] args) {
        LeetCode_80_Remove_Duplicates_from_Sorted_Array_II solution = new LeetCode_80_Remove_Duplicates_from_Sorted_Array_II();
        int i = solution.removeDuplicates(new int[]{1, 1, 1, 2, 2, 3});
        System.out.println("i = " + i);
    }
}
