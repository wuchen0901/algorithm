package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class LeetCode_215_Kth_Largest_Element_in_an_Array {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Comparator.reverseOrder());
        priorityQueue.addAll(Arrays.stream(nums).boxed().toList());
        int result = 0;
        for (int i = 0; i < k; i++) {
            result = priorityQueue.poll();
        }

        return result;
    }
}
