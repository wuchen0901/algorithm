package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_228_Summary_Ranges {
    public List<String> summaryRanges(int[] nums) {
        List<String> ranges = new ArrayList<>();

        if (nums.length == 0) {
            return ranges;
        }

        int start = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] + 1 < nums[i]) {
                ranges.add(buildString(start, nums[i - 1]));
                start = nums[i];
            }
        }

        ranges.add(buildString(start, nums[nums.length - 1]));

        return ranges;
    }

    String buildString(int startValue, int endValue) {
        if (startValue == endValue) {
            return String.valueOf(startValue);
        } else {
            return startValue + "->" + endValue;
        }
    }
}
