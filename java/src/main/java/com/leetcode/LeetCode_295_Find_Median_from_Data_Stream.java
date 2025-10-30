package com.leetcode;

import java.util.Comparator;
import java.util.PriorityQueue;

public class LeetCode_295_Find_Median_from_Data_Stream {
    class MedianFinder {
        private PriorityQueue<Integer> minHeap;
        private PriorityQueue<Integer> maxHeap;

        public MedianFinder() {
            this.minHeap = new PriorityQueue<>();
            this.maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        }

        // 6
        // [6] []
        // 1, 2, 3
        // 1, 3    2

        //
        // maxHeap, minHeap
        // [-3, -1] [-2]
        public void addNum(int num) {
            this.minHeap.offer(num);
            this.maxHeap.offer(this.minHeap.poll());
            if (this.maxHeap.size() - this.minHeap.size() > 1) {
                this.minHeap.offer(this.maxHeap.poll());
            }
        }

        public double findMedian() {
            if (this.maxHeap.size() == this.minHeap.size()) {
                return (this.maxHeap.peek() + this.minHeap.peek()) / 2.0;
            } else { // max heap size == min heap size + 1
                return this.maxHeap.peek();
            }
        }
    }
}
