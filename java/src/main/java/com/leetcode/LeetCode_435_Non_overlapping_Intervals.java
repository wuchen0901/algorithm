package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;

public class LeetCode_435_Non_overlapping_Intervals {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));
        int count = 0;
        // [4, 6],
        // [4, 6], [7, 9]
        // [4, 7], [5, 7]
        // [4, 6], [3, 9]
        int prevEnd = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            if (start < prevEnd) { // Overlapping
                count++;
                if (end < prevEnd) {
                    // Update prevStart, prevEnd
                    prevEnd = end;
                }
            }
        }
        return count;
    }

    public int eraseOverlapIntervalsV1(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(interval -> -interval[1]));

        int prevStart = intervals[0][0];
        int count = 0;
        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            if (prevStart < end) { // Overlapping
                count++;
                if (prevStart < start) {
                    prevStart = start;
                }
            } else { // Non-overlapping
                prevStart = start;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        LeetCode_435_Non_overlapping_Intervals solution = new LeetCode_435_Non_overlapping_Intervals();
        System.out.println(solution.eraseOverlapIntervalsV1(new int[][]{{1, 100}, {11, 22}, {1, 11}, {2, 12}}));
        System.out.println(solution.eraseOverlapIntervalsV1(new int[][]{{1, 2}, {2, 3}, {3, 4}, {1, 3}}));
    }
}
