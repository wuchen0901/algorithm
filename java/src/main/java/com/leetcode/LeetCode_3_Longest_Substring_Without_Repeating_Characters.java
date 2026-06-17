package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LeetCode_3_Longest_Substring_Without_Repeating_Characters {
    public int lengthOfLongestSubstring(String s) {
        int[] windowFreq = new int[128];
        int longestLength = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);
            windowFreq[rightChar]++;

            while (1 < windowFreq[rightChar]) {
                char leftChar = s.charAt(left);
                windowFreq[leftChar]--;
                left++;
            }

            longestLength = Math.max(longestLength, right + 1 - left);
        }

        return longestLength;
    }
}
