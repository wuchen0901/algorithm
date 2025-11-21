package com.leetcode;

import java.util.Arrays;
import java.util.PriorityQueue;

public class LeetCode_703_Kth_Largest_Element_in_a_Stream {
    class KthLargest {
        private final PriorityQueue<Integer> minHeap;
        private final int k;

        public KthLargest(int k, int[] nums) {
            this.k = k;
            minHeap = new PriorityQueue<>(Arrays.stream(nums).boxed().toList());
            while (k < minHeap.size()) {
                minHeap.poll();
            }
        }

        public int add(int val) {
            minHeap.offer(val);

            if (k < minHeap.size()) {
                minHeap.poll();
            }

            return minHeap.peek();
        }
    }
}
