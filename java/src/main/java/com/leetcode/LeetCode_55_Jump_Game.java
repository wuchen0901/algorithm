package com.leetcode;

public class LeetCode_55_Jump_Game {
    public boolean canJump(int[] nums) {
        int i = 0;
        int farthest = i + nums[i];
        if (nums.length == 1) {
            return true;
        }
        while (i < farthest) {
            i++;
            if (nums.length - 1 <= i) {
                return true;
            } else {
                farthest = Math.max(farthest, i + nums[i]);
            }
        }

        return false;
    }
}
