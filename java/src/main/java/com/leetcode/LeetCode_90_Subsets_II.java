package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode_90_Subsets_II {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        backtrack(nums, new ArrayList<>(), 0, result);

        return result;
    }

    void backtrack(int[] nums, List<Integer> path, int start, List<List<Integer>> result) {
        result.add(new ArrayList<>(path));

        while (start < nums.length) {
            path.add(nums[start]);
            backtrack(nums, path, start + 1, result);
            path.remove(path.size() - 1);

            while (start + 1 < nums.length &&
                    nums[start] == nums[start + 1]) {
                start++;
            }

            start++;
        }
    }
}
