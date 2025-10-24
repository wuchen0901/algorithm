package com.leetcode;

public class LeetCode_26_Remove_Duplicates_from_Sorted_Array {
    public int removeDuplicates(int[] nums) {
        // []
        // [4]
        // [4,   6]
        //  slow fast
        // [4,   4]
        int n = nums.length;
        if (n < 1) {
            return n;
        }

        int slow = 1;
        int fast = 1;

        while (fast < n) {
            if (nums[fast - 1] != nums[fast]) {
                nums[slow] = nums[fast];
                slow++;
            }
            fast++;
        }

        return slow;
    }
}
