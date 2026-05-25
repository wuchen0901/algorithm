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
        if (needle.isEmpty()) {
            return 0;
        }

        int[] lps = buildLPS(needle);

        int i = 0;
        int j = 0;

        while (i < haystack.length()) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;

                if (j == needle.length()) {
                    return i - j;
                }
            } else if (j > 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }

        return -1;
    }

    private int[] buildLPS(String needle) {
        int[] lps = new int[needle.length()];

        int len = 0;
        int i = 1;

        while (i < needle.length()) {
            if (needle.charAt(i) == needle.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else if (len > 0) {
                len = lps[len - 1];
            } else {
                i++;
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
