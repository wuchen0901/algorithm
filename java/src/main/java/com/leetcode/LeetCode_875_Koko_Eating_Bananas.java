package com.leetcode;

public class LeetCode_875_Koko_Eating_Bananas {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = 1_000_000_000;

        int k = -1;
        while (l <= r) {
            int speed = (l + r) / 2;
            if (h < timeTakes(piles, speed)) {
                l = speed + 1;
            } else if (timeTakes(piles, speed) < h) {
                k = speed;
                r = speed - 1;
            }
        }

        return k;
    }

    private long timeTakes(int[] piles, int k) {
        long time = 0;
        for (int pile : piles) {
            time += pile / k;
            if (pile % k != 0) time++;
        }
        return time;
    }
}
