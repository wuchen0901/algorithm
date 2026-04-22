package com.leetcode;

public class LeetCode_45_Jump_Game_II {
    public int jump(int[] nums) {
        if (nums.length == 1) {
            return 0;
        }
        int currPos = 0;
        int reachablePos = currPos + nums[0];

        // 1
        // 1 3
        // 1 3 1
        // [2,3,1,1,4]
        int step = 0;

        while (true) {
            step++;
            int nextStepCanReach = 0;
            while (currPos < reachablePos) {
                currPos++;
                if (nums.length - 1 <= currPos) {
                    return step;
                }

                nextStepCanReach = Math.max(nextStepCanReach, currPos + nums[currPos]);
            }

            reachablePos = nextStepCanReach;
        }
    }
}
