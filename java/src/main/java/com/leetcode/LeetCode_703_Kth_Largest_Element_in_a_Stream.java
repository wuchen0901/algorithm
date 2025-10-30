package com.leetcode;

import java.util.PriorityQueue;

public class LeetCode_703_Kth_Largest_Element_in_a_Stream {
    class KthLargest {
        private final PriorityQueue<Integer> queue = new PriorityQueue<>();
        private int k = 0;

        public KthLargest(int k, int[] nums) {
            this.k = k;
            for (int num : nums) {
                this.add(num);
            }
        }

        public int add(int val) {
            queue.offer(val);

            while (k < queue.size()) {
                queue.poll();
            }

            return queue.peek();
        }
    }
}
