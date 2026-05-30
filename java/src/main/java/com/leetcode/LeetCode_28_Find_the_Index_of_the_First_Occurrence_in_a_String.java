package com.leetcode;

import java.util.Arrays;

public class LeetCode_28_Find_the_Index_of_the_First_Occurrence_in_a_String {
    public int strStr(String haystack, String needle) {
        for (int i = 0; i < haystack.length() - needle.length() + 1; i++) {
            boolean match = true;
            for (int j = 0; j < needle.length(); j++) {
                if (haystack.charAt(i + j) != needle.charAt(j)) {
                    match = false;
                    break;
                }
            }

            if (match) {
                return i;
            }
        }

        return -1;
    }

    public int strStrKMP(String haystack, String needle) {
        int[] lps = buildLPS(needle);

        // i points to the current character in the haystack.
        int i = 0;

        // I initialize j to 0
        int j = 0;

        // I iterate while i is less than the length of the haystack
        while (i < haystack.length()) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;

                // If j equals the length of the needle.
                if (j == needle.length()) {
                    return i - j;
                }
            } else {
                if (0 < j) {
                    // I set j to LPS at index j - 1.
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }

        return -1;
    }

    private int[] buildLPS(String pattern) {
        // First, I define an integer array called lps.
        // Create the LPS array with the same length as the pattern.
        // Initialize the LPS array.
        int[] lps = new int[pattern.length()];
        // I create an integer variable i and initialize it to 1.
        int i = 1;
        // I create an integer variable len and initialize it to 0;
        int len = 0;
        // I iterate while i is less than the length of the pattern.
        while (i < pattern.length()) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                // I set lps[i] to len.
                lps[i] = len;
                i++;
            } else {
                if (0 < len) {
                    // I set len to lps at len minus 1
                    len = lps[len - 1];
                } else {
                    i++;
                }
            }
        }

        return lps;
    }

    public static void main(String[] args) {
        LeetCode_28_Find_the_Index_of_the_First_Occurrence_in_a_String solution =
                new LeetCode_28_Find_the_Index_of_the_First_Occurrence_in_a_String();

        String[] needles = {
                "a",
                "aa",
                "ababaca",
                "abcaby",
                "aabaaab",
                "abcdabca"
        };

        for (String needle : needles) {
            System.out.println(needle + " -> " + Arrays.toString(solution.buildLPS(needle)));
        }
    }
}
