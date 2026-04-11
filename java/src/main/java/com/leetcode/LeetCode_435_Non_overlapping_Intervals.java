package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;

public class LeetCode_435_Non_overlapping_Intervals {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(i -> i[1]));
        int end = intervals[0][1];
        int overlapCount = 0;
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < end) {
                overlapCount++;
            } else {
                end = intervals[i][1];
            }
        }

        return overlapCount;
    }
}
