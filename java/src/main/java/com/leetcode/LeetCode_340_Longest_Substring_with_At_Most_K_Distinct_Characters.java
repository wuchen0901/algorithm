package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_340_Longest_Substring_with_At_Most_K_Distinct_Characters {

    int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> window = new HashMap<>();
        int longestLength = 0;
        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            window.put(s.charAt(r), window.getOrDefault(s.charAt(r), 0) + 1);
            // shink
            while (k < window.size()) {
                window.compute(s.charAt(l), (character, frequency) -> (frequency == null || frequency == 1) ? null : frequency - 1);
                l++;
            }

            if (longestLength < r + 1 - l) {
                longestLength = r + 1 - l;
            }
        }

        return longestLength;
    }
}
