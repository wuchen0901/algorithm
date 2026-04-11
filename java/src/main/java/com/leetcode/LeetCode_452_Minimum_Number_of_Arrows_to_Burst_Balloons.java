package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;

public class LeetCode_452_Minimum_Number_of_Arrows_to_Burst_Balloons {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, Comparator.comparingInt(p -> p[1]));
        int end = points[0][1];
        int overlappedCount = 0;
        for (int i = 1; i < points.length; i++) {
            int start = points[i][0];
            if (start <= end) {
                overlappedCount++;
            } else {
                end = points[i][1];
            }
        }

        return points.length - overlappedCount;
    }
}
