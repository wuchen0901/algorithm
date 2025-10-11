package cn.com.ilean;

import org.junit.jupiter.api.Test;

class Solution480SlidingWindowMedianTest {
    Solution_480_Sliding_Window_Median solution = new Solution_480_Sliding_Window_Median();

    @Test
    void medianSlidingWindow() {
        solution.medianSlidingWindow(new int[]{1, 3, -1, -3, 5, 3, 6, 7}, 3);
    }
}