package com.leetcode;

import java.util.*;

public class LeetCode_347_Top_K_Frequent_Elements {
    /**
     * Time Complexity: O(n + m), which is O(n) in the worst case.
     * Space Complexity: O(n + m + k), which simplifies to O(n) in the worst case.
     */
    public int[] topKFrequentBucketSort(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] buckets = new ArrayList[nums.length + 1];

        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();

            if (buckets[count] == null) {
                buckets[count] = new ArrayList<>();
            }

            buckets[count].add(num);
        }

        int[] result = new int[k];
        int index = 0;
        for (int count = buckets.length - 1; count >= 0; count--) {
            if (buckets[count] == null) {
                continue;
            }

            for (int num : buckets[count]) {
                result[index] = num;
                index++;

                if (index == k) {
                    return result;
                }
            }

        }

        return result;
    }

    /**
     * Time Complexity: O(n + m log m + k log m), where m is the number of unique elements. In the worst case (m = n), this becomes O(n log n).
     * Space Complexity: O(m), or O(n) in the worst case.
     */
    public int[] topKFrequentMinHeap(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        Queue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<>((a, b) -> a.getValue() - b.getValue());

        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            heap.offer(entry);

            if (k < heap.size()) {
                heap.poll();
            }
        }

        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = heap.poll().getKey();
        }

        return result;
    }
}
