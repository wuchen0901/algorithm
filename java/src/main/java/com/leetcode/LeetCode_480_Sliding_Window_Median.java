package com.leetcode;

import java.util.*;

public class LeetCode_480_Sliding_Window_Median {

    // small: max-heap, 存较小的一半；large: min-heap, 存较大的一半
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    private PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    private Map<Integer, Integer> delayed = new HashMap<>();

    // 有效元素数量（不包括已标记 delayed 的）
    private int minHeapSize = 0;
    private int maxHeapSize = 0;

    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] res = new double[nums.length - k + 1];
        int left = 0;
        int right = 0;
        while (right < nums.length) {
            add(nums[right]);
            right++;
            // 窗口长度达到 k
            if (right - left == k) {
                res[left] = getMedian(k);
                remove(nums[left]);
                left++;
            }
        }

        return res;
    }

    // 往窗口里加入一个数
    private void add(int num) {
        minHeap.offer(num);
        maxHeap.offer(minHeap.poll());
        maxHeapSize++;
        if (minHeapSize < maxHeapSize) {
            minHeap.offer(maxHeap.poll());
            maxHeapSize--;
            minHeapSize++;
        }
    }

    // 从窗口里删除一个数（逻辑删除 + lazy deletion）
    private void remove(int num) {
        delayed.put(num, delayed.getOrDefault(num, 0) + 1);
        if (!minHeap.isEmpty() && minHeap.peek() <= num) {
            minHeapSize--;
        } else if (!maxHeap.isEmpty() && num <= maxHeap.peek()) {
            maxHeapSize--;
        }
        if (minHeapSize < maxHeapSize) {
            minHeap.offer(maxHeap.poll());
            maxHeapSize--;
            minHeapSize++;
        }
        if (maxHeapSize + 1 < minHeapSize) {
            maxHeap.offer(minHeap.poll());
            minHeapSize--;
            maxHeapSize++;
        }
    }

    // 把堆顶那些已经 delayed 的元素真正弹出去
    private void prune(PriorityQueue<Integer> heap) {
        while (!heap.isEmpty()) {
            int num = heap.peek();
            if (!delayed.containsKey(num)) {
                break;
            }
            delayed.compute(num, (k, v) -> v == 1 ? null : v - 1);
            heap.poll();
        }
    }

    private double getMedian(int k) {
        prune(minHeap);
        prune(maxHeap);
        if ((k & 1) == 1) {
            return (double) minHeap.peek();
        } else {
            // 偶数，两个中间值平均；用 double 相加避免溢出问题
            return ((double) minHeap.peek() + (double) maxHeap.peek()) / 2.0;
        }
    }

    // 可选：你的极端用例自测
    public static void main(String[] args) {
        LeetCode_480_Sliding_Window_Median solution = new LeetCode_480_Sliding_Window_Median();

        int[] nums = new int[]{1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;

        double[] expected = new double[]{1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000};

        double[] actual = solution.medianSlidingWindow(nums, k);
        System.out.println("actual  = " + Arrays.toString(actual));
        System.out.println("expected= " + Arrays.toString(expected));

        if (!Arrays.equals(actual, expected)) {
            throw new RuntimeException("Test failed: expected=" + Arrays.toString(expected) + ", actual=" + Arrays.toString(actual));
        }

        System.out.println("✅ Test passed");
    }
}