package com.leetcode;

public class LeetCode_340_Longest_Substring_with_At_Most_K_Distinct_Characters {

    int lengthOfLongestSubstringKDistinct(String s, int k) {
        int longestLength = 0;
        int[] freq = new int[128];
        int distinctCount = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);
            if (freq[rightChar] == 0) {
                distinctCount++;
            }
            freq[rightChar]++;
            while (k < distinctCount) {
                char leftChar = s.charAt(left);
                freq[leftChar]--;
                if (freq[leftChar] == 0) {
                    distinctCount--;
                }

                left++;
            }

            longestLength = Math.max(longestLength, right + 1 - left);
        }

        return longestLength;
    }
}
