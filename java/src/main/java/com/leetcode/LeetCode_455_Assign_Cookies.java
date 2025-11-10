package com.leetcode;

import java.util.Arrays;

public class LeetCode_455_Assign_Cookies {
    public int findContentChildren(int[] greed, int[] cookies) {
        Arrays.sort(greed);
        Arrays.sort(cookies);
        int childIndex = 0;
        int contentCount = 0;
        for (int cookie : cookies) {
            if (childIndex < greed.length) {
                if (greed[childIndex] <= cookie) {
                    contentCount++;
                    childIndex++;
                }
            } else {
                return contentCount;
            }
        }

        return contentCount;
    }
}
