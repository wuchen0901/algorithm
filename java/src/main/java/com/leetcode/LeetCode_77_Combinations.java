package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_77_Combinations {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();

        backtrack(n, k, new ArrayList<>(), 1, result);

        return result;
    }

    void backtrack(int n, int k, List<Integer> path, int start, List<List<Integer>> result) {
        if (path.size() == k) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = start; i <= n; i++) {
            path.add(i);
            backtrack(n, k, path, i + 1, result);
            path.remove(path.size() - 1);
        }
    }
}
