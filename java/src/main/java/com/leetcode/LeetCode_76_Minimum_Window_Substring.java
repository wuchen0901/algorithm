package com.leetcode;

public class LeetCode_76_Minimum_Window_Substring {

    public String minWindow(String s, String t) {
        int[] need = new int[128];

        for (int i = 0; i < t.length(); i++) {
            need[t.charAt(i)]++;
        }

        int[] freq = new int[128];
        int l = 0;
        int minLength = Integer.MAX_VALUE;
        int start = 0;

        for (int r = 0; r < s.length(); r++) {
            freq[s.charAt(r)]++;

            while (covers(freq, need)) {
                if (r - l + 1 < minLength) {
                    minLength = r - l + 1;
                    start = l;
                }

                freq[s.charAt(l)]--;
                l++;
            }
        }

        return minLength == Integer.MAX_VALUE ? "" : s.substring(start, start + minLength);
    }

    private boolean covers(int[] freq, int[] need) {
        for (int i = 0; i < 128; i++) {
            if (freq[i] < need[i]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        LeetCode_76_Minimum_Window_Substring solution = new LeetCode_76_Minimum_Window_Substring();
        System.out.println(solution.minWindow("ADOBECODEBANC", "ABC"));
        System.out.println(solution.minWindow("cabwefgewcwaefgcf", "cae"));
    }
}
