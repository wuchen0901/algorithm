package com.leetcode;

public class LeetCode_459_Repeated_Substring_Pattern {
    public boolean repeatedSubstringPattern(String s) {
        // I create two integer variables len and i
        // I initialize two integer variables, len and i.
        // I initialize len to 0 and i to 1.
        // len represents the length of the current matching prefix-suffix.
        int len = 0;
        int i = 1;

        // I initialize an LPS array with the same length as s.
        int[] lps = new int[s.length()];

        // I iterate while i is less than the length of s
        while (i < lps.length) {
            if (s.charAt(len) == s.charAt(i)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (0 < len) {
                    // Set len to the LPS value at index len - 1.
                    len = lps[len - 1];
                } else {
                    i++;
                }
            }
        }

        // last represents the length of the repeated substring
        int last = lps[s.length() - 1];

        // I initialize a variable unitLen, which represents the length of the repeating unit.
        int unitLen = s.length() - last;

        if (unitLen == s.length()) {
            return false;
        }
        // a b c b
        // a b c c
        // a b a c
        return s.length() % unitLen == 0;
    }
}
