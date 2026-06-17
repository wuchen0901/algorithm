package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_78_Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        ArrayList<List<Integer>> res = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), 0, res);
        return res;
    }

    private void backtrack(int[] nums, List<Integer> path, int start, List<List<Integer>> res) {
        res.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(nums, path, i + 1, res);
            path.remove(path.size() - 1);
        }
    }

    public List<List<Integer>> subsetsIncludeExclude(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrackIncludeExclude(nums, new ArrayList<>(), 0, result);
        return result;
    }

    private void backtrackIncludeExclude(int[] nums, List<Integer> path, int index, List<List<Integer>> result) {
        if (index == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }

        path.add(nums[index]);
        backtrackIncludeExclude(nums, path, index + 1, result);
        path.remove(path.size() - 1);

        backtrackIncludeExclude(nums, path, index + 1, result);
    }
}
