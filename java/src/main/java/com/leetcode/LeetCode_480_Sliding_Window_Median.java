package com.leetcode;

import java.util.*;

public class LeetCode_480_Sliding_Window_Median {

    // small: max-heap, 存较小的一半；large: min-heap, 存较大的一半
    private PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
    private PriorityQueue<Integer> large = new PriorityQueue<>();
    private Map<Integer, Integer> delayed = new HashMap<>();

    // 有效元素数量（不包括已标记 delayed 的）
    private int smallSize = 0;
    private int largeSize = 0;

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
        // 先按值决定放哪边，而不是按 size
        if (small.isEmpty() || num <= small.peek()) {
            small.offer(num);
            smallSize++;
        } else {
            large.offer(num);
            largeSize++;
        }

        rebalance();
    }

    // 从窗口里删除一个数（逻辑删除 + lazy deletion）
    private void remove(int num) {
        delayed.put(num, delayed.getOrDefault(num, 0) + 1);

        // 决定它属于哪个堆，修正 size
        if (!small.isEmpty() && num <= small.peek()) {
            smallSize--;
            if (num == small.peek()) {
                prune(small);
            }
        } else {
            largeSize--;
            if (!large.isEmpty() && num == large.peek()) {
                prune(large);
            }
        }

        rebalance();
    }

    // 保持不变量：smallSize == largeSize 或 smallSize == largeSize + 1
    private void rebalance() {
        if (smallSize > largeSize + 1) {
            // small 太多，挪一个到 large
            large.offer(small.poll());
            smallSize--;
            largeSize++;
            prune(small);
        } else if (smallSize < largeSize) {
            // large 太多，挪一个到 small
            small.offer(large.poll());
            largeSize--;
            smallSize++;
            prune(large);
        }
    }

    // 把堆顶那些已经 delayed 的元素真正弹出去
    private void prune(PriorityQueue<Integer> heap) {
        while (!heap.isEmpty()) {
            int num = heap.peek();
            Integer cnt = delayed.get(num);
            if (cnt == null || cnt == 0) {
                break;
            }
            if (cnt == 1) {
                delayed.remove(num);
            } else {
                delayed.put(num, cnt - 1);
            }
            heap.poll();
        }
    }

    private double getMedian(int k) {
        if ((k & 1) == 1) {
            // 窗口长度为奇数，small 顶就是中位数
            return (double) small.peek();
        } else {
            // 偶数，两个中间值平均；用 double 相加避免溢出问题
            return ((double) small.peek() + (double) large.peek()) / 2.0;
        }
    }

    // 可选：你的极端用例自测
    public static void main(String[] args) {
        LeetCode_480_Sliding_Window_Median solution = new LeetCode_480_Sliding_Window_Median();

        int[] nums = new int[]{-2147483648, -2147483648, 2147483647, -2147483648, -2147483648, -2147483648, 2147483647, 2147483647, 2147483647, 2147483647, -2147483648, 2147483647, -2147483648};
        int k = 3;

        double[] expected = new double[]{-2147483648.0, -2147483648.0, -2147483648.0, -2147483648.0, -2147483648.0, 2147483647.0, 2147483647.0, 2147483647.0, 2147483647.0, 2147483647.0, -2147483648.0};

        double[] actual = solution.medianSlidingWindow(nums, k);
        System.out.println("actual  = " + Arrays.toString(actual));
        System.out.println("expected= " + Arrays.toString(expected));

        if (!Arrays.equals(actual, expected)) {
            throw new RuntimeException("Test failed: expected=" + Arrays.toString(expected) + ", actual=" + Arrays.toString(actual));
        }

        System.out.println("✅ Test passed");
    }
}