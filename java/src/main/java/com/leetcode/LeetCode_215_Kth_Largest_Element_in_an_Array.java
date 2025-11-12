package com.leetcode;

import java.util.PriorityQueue;

public class LeetCode_215_Kth_Largest_Element_in_an_Array {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int i = 0; i < nums.length; i++) {
            minHeap.offer(nums[i]);
            if (k < minHeap.size()) {
                minHeap.poll();
            }
        }
        return minHeap.peek();
    }
}
