package com.leetcode;

public class LeetCode_567_Permutation_in_String {
    public boolean checkInclusion(String s1, String s2) {
        int[] freq = new int[26];

        for (int i = 0; i < s1.length(); i++) {
            freq[s1.charAt(i) - 'a']++;
        }

        for (int r = 0; r < s2.length(); r++) {
            freq[s2.charAt(r) - 'a']--;
            int l = r - s1.length();
            if (-1 <= l) {
                if (0 <= l) {
                    freq[s2.charAt(l) - 'a']++;
                }

                boolean match = true;
                for (int i = 0; i < freq.length; i++) {
                    if (freq[i] != 0) {
                        match = false;
                    }
                }

                if (match) {
                    return true;
                }
            }
        }

        return false;
    }
}
