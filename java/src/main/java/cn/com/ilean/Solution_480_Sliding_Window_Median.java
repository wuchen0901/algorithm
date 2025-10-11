package cn.com.ilean;

import java.util.TreeMap;

public class Solution_480_Sliding_Window_Median {
    public double[] medianSlidingWindow(int[] nums, int k) {
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        for (int i = 0; i < k; i++) {
            treeMap.put(nums[i], i);
        }

        double[] result = new double[nums.length - k + 1];
        for (int i = 0; i < nums.length - k + 1; i++) {
            Integer[] array = treeMap.keySet().toArray(new Integer[0]);
            double middle = 0;
            if (array.length % 2 == 0) {
                middle = (array[array.length / 2] + array[array.length / 2 + 1]) / 2.0;
            } else {
                middle = (array[array.length / 2]);
            }
            result[i] = middle;
        }
        return result;
    }
}

