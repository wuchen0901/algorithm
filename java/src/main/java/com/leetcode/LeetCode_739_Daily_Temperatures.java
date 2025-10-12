package com.leetcode;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class LeetCode_739_Daily_Temperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> integers = new ArrayDeque<>();
        int[] res = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            while (!integers.isEmpty() && temperatures[integers.peek()] < temperatures[i]) {
                Integer day = integers.pop();
                res[day] = i - day;
            }

            integers.push(i);
        }

        return res;
    }

    public static void main(String[] args) {
        LeetCode_739_Daily_Temperatures solution = new LeetCode_739_Daily_Temperatures();
        System.out.println(Arrays.toString(solution.dailyTemperatures(new int[]{73, 74, 75, 71, 69, 72, 76, 73})));
        // [1,1,4,2,1,1,0,0]
    }
}
