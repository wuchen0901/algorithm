package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode_56_Merge_Intervals {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return new int[0][2];
        }

        // 1) sort by start
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> merged = new ArrayList<>();
        int curStart = intervals[0][0];
        int curEnd = intervals[0][1];

        // 2) scan and merge
        for (int i = 1; i < intervals.length; i++) {
            int s = intervals[i][0], e = intervals[i][1];
            if (s <= curEnd) {           // overlap
                curEnd = Math.max(curEnd, e);
            } else {                     // no overlap
                merged.add(new int[]{curStart, curEnd});
                curStart = s;
                curEnd = e;
            }
        }

        // 3) add the last window
        merged.add(new int[]{curStart, curEnd});
        return merged.toArray(new int[merged.size()][]);
    }
}
