package com.leetcode;

import java.util.*;

public class LeetCode_239_Sliding_Window_Maximum {
    // Balanced Binary Search Tree (BST)–based sliding window solution
    // Implemented with a TreeSet (Red-Black Tree).
    // Time complexity: O(n log k)
    // ⚠️ Only correct if all numbers in the input window are distinct,
    // because TreeSet does not handle duplicates (it merges identical values).
    public int[] maxSlidingWindowV1(int[] nums, int k) {
        TreeSet<Integer> integers = new TreeSet<>();

        for (int i = 0; i < k; i++) {
            integers.add(nums[i]);
        }

        int[] result = new int[nums.length - k + 1];
        result[0] = integers.last();
        // 1 3 4 5 6
        // l = 5
        // k = 3
        for (int i = 0; i < nums.length - k; i++) {
            integers.add(nums[i + k]);
            integers.remove(nums[i]);
            result[i + 1] = integers.last();
        }

        return result;
    }

    /**
     * Balanced Binary Search Tree (BST)–based sliding window solution.
     * Implemented with a TreeMap (Red-Black Tree) as a multiset (stores frequencies of elements).
     * Maintains element counts in the current window to support duplicates.
     * Time complexity: O(n log k)
     * Correct for all inputs, including those with duplicate numbers.
     */
    public int[] maxSlidingWindowV2(int[] nums, int k) {
        TreeMap<Integer, Integer> integers = new TreeMap<>();

        for (int i = 0; i < k; i++) {
            integers.put(nums[i], integers.getOrDefault(nums[i], 0) + 1);
        }

        int[] result = new int[nums.length - k + 1];
        result[0] = integers.lastKey();
        for (int i = 0; i < nums.length - k; i++) {
            integers.put(nums[i + k], integers.getOrDefault(nums[i + k], 0) + 1);
            if (integers.containsKey(nums[i])) {
                Integer count = integers.get(nums[i]);
                count--;
                if (count == 0) {
                    integers.remove(nums[i]);
                } else {
                    integers.put(nums[i], count);
                }
            }
            result[i + 1] = integers.lastKey();
        }

        return result;
    }

    // TreeMap-multiset solution
    public int[] maxSlidingWindowV3(int[] nums, int k) {
        TreeMap<Integer, Integer> integers = new TreeMap<>();

        for (int i = 0; i < k; i++) {
            integers.merge(nums[i], 1, Integer::sum);
        }

        int[] result = new int[nums.length - k + 1];
        result[0] = integers.lastKey();
        for (int i = 0; i < nums.length - k; i++) {
            integers.merge(nums[i + k], 1, Integer::sum);
            integers.computeIfPresent(nums[i], (key, count) -> count == 1 ? null : count - 1);
            result[i + 1] = integers.lastKey();
        }

        return result;
    }

    public int[] maxSlidingWindowV4(int[] nums, int k) {
        TreeMap<Integer, Integer> integers = new TreeMap<>();

        for (int i = 0; i < k; i++) {
            integers.merge(nums[i], 1, Integer::sum);
        }

        int[] result = new int[nums.length - k + 1];
        result[0] = integers.lastKey();
        for (int i = 0; i < nums.length - k; i++) {
            integers.merge(nums[i + k], 1, Integer::sum);
            integers.computeIfPresent(nums[i], (key, count) -> count == 1 ? null : count - 1);
            result[i + 1] = integers.lastKey();
        }

        return result;
    }

    // Deque
    public void maxSlidingWindowV5(int[] nums, int k) {
        Deque<Integer> integers = new ArrayDeque<>();
        int[] ints = {3, 7, 9, 4, 5, 1};
        for (int i = 0; i < ints.length; i++) {
            while (!integers.isEmpty() && ints[integers.peekLast()] < ints[i]) {
                integers.pollLast();
            }
            integers.addLast(i);
        }
        System.out.println("integers = " + integers);
    }

    // Deque
    public int[] maxSlidingWindowV6(int[] nums, int k) {
        Deque<Integer> integers = new ArrayDeque<>();
        int[] result = new int[nums.length - k + 1];
        for (int i = 0; i < k; i++) {
            while (!integers.isEmpty() && nums[integers.peekLast()] <= nums[i]) {
                integers.pollLast();
            }
            integers.addLast(i);
        }

        if (!integers.isEmpty()) result[0] = integers.peekFirst();

        for (int i = k; i < nums.length; i++) {
            while (!integers.isEmpty() && nums[integers.peekLast()] <= nums[i]) {
                integers.pollLast();
            }
            integers.addLast(i);

            if (!integers.isEmpty() && integers.peekFirst() == i - k) {
                integers.removeFirst();
            }

            if (!integers.isEmpty()) result[i - k + 1] = integers.peekFirst();
        }

        for (int i = 0; i < result.length; i++) {
            result[i] = nums[result[i]];
        }
        return result;
    }

    // Deque
    public int[] maxSlidingWindowV7(int[] nums, int k) {
        Deque<Integer> integers = new ArrayDeque<>();
        int[] result = new int[nums.length - k + 1];

        for (int i = 0; i < nums.length; i++) {
            while (!integers.isEmpty() && nums[integers.peekLast()] <= nums[i]) {
                integers.pollLast();
            }

            integers.addLast(i);

            if (k <= i && !integers.isEmpty() && integers.peekFirst() == i - k) {
                integers.removeFirst();
            }

            if (k - 1 <= i && !integers.isEmpty()) result[i - k + 1] = nums[integers.peekFirst()];
        }

        return result;
    }

    public int[] maxSlidingWindowV8(int[] nums, int k) {
        Deque<Integer> dq = new ArrayDeque<>(); // store indices; nums[dq] is decreasing
        int[] res = new int[nums.length - k + 1];

        for (int i = 0; i < nums.length; i++) {
            // pop smaller or equal from back (newer equals dominate)
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();

            dq.addLast(i);

            // evict out-of-window from front
            if (dq.peekFirst() <= i - k) dq.pollFirst();

            // record once the window is formed
            if (k - 1 <= i)
                res[i - k + 1] = nums[dq.peekFirst()];
        }
        return res;
    }

    public static void main(String[] args) {
        LeetCode_239_Sliding_Window_Maximum solution = new LeetCode_239_Sliding_Window_Maximum();
        System.out.println(Arrays.toString(
                solution.maxSlidingWindowV8(new int[]{9, 3, -1, -3, 5, 3, 6, 7}, 3)
        ));
    }
}
