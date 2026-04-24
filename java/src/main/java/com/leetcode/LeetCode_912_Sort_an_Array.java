package com.leetcode;

public class LeetCode_912_Sort_an_Array {
    public int[] sortArray(int[] nums) {
        sort(nums, 0, nums.length - 1);
        return nums;
    }

    void sort(int[] nums, int left, int right) {
        if (right <= left) {
            return;
        }

        int mid = left + (right - left) / 2;
        sort(nums, left, mid);
        sort(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }

    void merge(int[] nums, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];

        int l = left;
        int m = mid;
        int r = right;
        int p = temp.length - 1;
        while (0 <= p) {
            if (left <= m && mid < r) {
                if (nums[m] < nums[r]) {
                    temp[p] = nums[r];
                    r--;
                } else {
                    temp[p] = nums[m];
                    m--;
                }
            } else if (left <= m) {
                temp[p] = nums[m];
                m--;
            } else if (mid < r) {
                temp[p] = nums[r];
                r--;
            }

            p--;
        }

        for (int i = 0; i < temp.length; i++) {
            nums[left + i] = temp[i];
        }
    }
}
