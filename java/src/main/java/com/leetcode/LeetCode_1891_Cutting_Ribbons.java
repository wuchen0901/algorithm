package com.leetcode;

public class LeetCode_1891_Cutting_Ribbons {
    int maxLength(int[] ribbons, int k) {
        int l = 1;
        int r = 0;

        for (int ribbon : ribbons) {
            r = Math.max(r, ribbon + 1);
        }

        while (l < r) {
            int length = l + (r - l) / 2;
            if (canCut(ribbons, length) < k) {
                r = length;
            } else {
                l = length + 1;
            }
        }

        return l - 1;
    }

    private int canCut(int[] ribbons, int length) {
        int pieceCount = 0;
        for (int ribbon : ribbons) {
            pieceCount += ribbon / length;
        }
        return pieceCount;
    }

    public static void main(String[] args) {
        LeetCode_1891_Cutting_Ribbons solution = new LeetCode_1891_Cutting_Ribbons();

        // Counterexample 1: should return 9, but current code returns 8
        int[] ribbons1 = {9};
        int k1 = 1;
        System.out.println("Test1 Expected: 9, Actual: " + solution.maxLength(ribbons1, k1));

        // Counterexample 2: should return 0, but current code returns 1
        int[] ribbons2 = {1, 2};
        int k2 = 10;
        System.out.println("Test2 Expected: 0, Actual: " + solution.maxLength(ribbons2, k2));
    }
}
