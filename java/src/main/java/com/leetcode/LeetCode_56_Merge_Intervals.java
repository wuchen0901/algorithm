package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class LeetCode_56_Merge_Intervals {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(i -> i[0]));
        List<int[]> mergedIntervals = new ArrayList<>();

        int start = intervals[0][0];
        int end = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];
            if (end < currStart) {
                mergedIntervals.add(new int[]{start, end});
                start = currStart;
                end = currEnd;
            } else {
                end = Math.max(end, currEnd);
            }
        }

        mergedIntervals.add(new int[]{start, end});

        return mergedIntervals.toArray(new int[0][]);
    }
}
