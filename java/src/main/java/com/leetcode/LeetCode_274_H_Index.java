package com.leetcode;

import java.util.Arrays;

public class LeetCode_274_H_Index {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);

        for (int h = citations.length; 1 <= h; h--) {
            if (h <= citations[citations.length - h]) {
                return h;
            }
        }

        return 0;
    }
}
