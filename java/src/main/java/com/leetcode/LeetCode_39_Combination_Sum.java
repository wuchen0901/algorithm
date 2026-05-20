package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_39_Combination_Sum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();

        backtrack(candidates, new ArrayList<>(), 0, 0, target, result);

        return result;
    }

    void backtrack(int[] candidates, List<Integer> path, int currentSum, int start, int target,
                   List<List<Integer>> result) {
        if (target <= currentSum) {
            if (target == currentSum) {
                result.add(new ArrayList<>(path));
            }
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            path.add(candidates[i]);
            backtrack(candidates, path, currentSum + candidates[i], i, target, result);
            path.remove(path.size() - 1);
        }
    }
}
