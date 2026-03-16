package com.leetcode;

public class LeetCode_11_Container_With_Most_Water {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length - 1;

        int maxVolume = 0;

        while (l < r) {

            int volume = Math.min(height[l], height[r]) * (r - l);

            if (maxVolume < volume) {
                maxVolume = volume;
            }

            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }

        return maxVolume;
    }
}
