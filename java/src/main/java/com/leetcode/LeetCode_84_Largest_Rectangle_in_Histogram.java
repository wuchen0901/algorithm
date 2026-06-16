package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class LeetCode_84_Largest_Rectangle_in_Histogram {
    public int largestRectangleArea(int[] heights) {
        // I think I should pad heights with a 0 at both ends.
        int[] paddedHeights = new int[heights.length + 2];

        for (int i = 0; i < heights.length; i++) {
            paddedHeights[i + 1] = heights[i];
        }

        Deque<Integer> stack = new ArrayDeque<>();

        int maxArea = 0;

        for (int i = 0; i < paddedHeights.length; i++) {
            while (!stack.isEmpty() && paddedHeights[stack.peek()] > paddedHeights[i]) {
                int index = stack.pop();

                maxArea = Math.max(maxArea, (i - stack.peek() - 1) * paddedHeights[index]);
            }

            //             *
            //         *   *
            //   * *   * * *
            //   * * * * * * *
            // stack
            // 0     3   5 6

            stack.push(i);
        }

        return maxArea;
    }
}
