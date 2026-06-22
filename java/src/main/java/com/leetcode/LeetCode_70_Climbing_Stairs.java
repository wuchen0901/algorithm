package com.leetcode;

public class LeetCode_70_Climbing_Stairs {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        // n: 1, 1
        // n: 2, 2
        // n: 3, 1 + 2
        // n: 4, 2 + 3
        // climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2);
        int twoStepsBefore = 1; // climbStairs(n - 2)
        int oneStepBefore = 2; // climbStairs(n - 1)

        int curr = 0;
        for (int i = 3; i <= n; i++) {
            curr = oneStepBefore + twoStepsBefore;
            twoStepsBefore = oneStepBefore;
            oneStepBefore = curr;
        }

        return curr;
    }
}
