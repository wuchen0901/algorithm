package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_46_Permutations {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        backtrack(nums, new boolean[nums.length], new ArrayList<>(), result);

        return result;
    }

    void backtrack(int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> result) {
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i] == false) {
                used[i] = true;
                path.add(nums[i]);
                backtrack(nums, used, path, result);
                path.remove(path.size() - 1);
                used[i] = false;
            }
        }
    }
}
