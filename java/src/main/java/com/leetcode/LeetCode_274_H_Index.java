package com.leetcode;

import java.util.Arrays;

public class LeetCode_274_H_Index {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);

        int h = citations.length;
        while (0 <= h) {
            boolean qualified = true;
            for (int i = citations.length - 1; citations.length - h <= i; i--) {
                if (i + 1 <= citations[i]) {

                } else {
                    qualified = false;
                    break;
                }
            }

            if (qualified) {
                return h;
            }

            h--;
        }

        return 0;
    }
}
