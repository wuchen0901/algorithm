package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class LeetCode_496_Next_Greater_Element_I {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Deque<Integer> stack = new ArrayDeque<>();
        // I need to build a map for num2 so that I can find an index from a value
        Map<Integer, Integer> map = new HashMap<>();

        int[] nextGreaterElements = new int[nums2.length];

        for (int i = 0; i < nextGreaterElements.length; i++) {
            nextGreaterElements[i] = -1;
        }

        for (int i = 0; i < nums2.length; i++) {
            map.put(nums2[i], i);

            while (!stack.isEmpty() && nums2[stack.peek()] < nums2[i]) {
                int index = stack.pop();
                nextGreaterElements[index] = nums2[i];
            }

            stack.push(i);
        }

        int[] result = new int[nums1.length];

        for (int i = 0; i < nums1.length; i++) {
            result[i] = nextGreaterElements[map.get(nums1[i])];
        }

        return result;
    }
}
