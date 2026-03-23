package com.leetcode;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class LeetCode_739_Daily_Temperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> stack = new ArrayDeque<>();
        // ArrayDeque 常用方法与操作位置说明：
        // push()  -> 头（左）
        // pop()   -> 头（左）
        // peek()  -> 头（左）
        // offer() -> 尾（右）
        // poll()  -> 头（左）
        // peek()（队列语义）-> 头（左）

        int[] result = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int index = stack.pop();
                result[index] = i - index;
            }

            stack.push(i);
        }

        return result;
    }

    public static void main(String[] args) {
        LeetCode_739_Daily_Temperatures solution = new LeetCode_739_Daily_Temperatures();
        System.out.println(Arrays.toString(solution.dailyTemperatures(new int[]{73, 74, 75, 71, 69, 72, 76, 73})));
        // [1,1,4,2,1,1,0,0]
    }
}
