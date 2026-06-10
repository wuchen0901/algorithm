package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_57_Insert_Interval {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();

        for (int[] current : intervals) {
            if (current[1] < newInterval[0]) {
                // current 在 newInterval 左边
                result.add(current);
            } else if (newInterval[1] < current[0]) {
                // current 在 newInterval 右边
                result.add(newInterval);

                newInterval = current;
            } else {
                // overlap
                newInterval[0] = Math.min(newInterval[0], current[0]);
                newInterval[1] = Math.max(newInterval[1], current[1]);
            }
        }
        result.add(newInterval);
        return result.toArray(new int[result.size()][]);
    }
}
