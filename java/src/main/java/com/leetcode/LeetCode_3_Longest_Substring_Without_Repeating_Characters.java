package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LeetCode_3_Longest_Substring_Without_Repeating_Characters {
    // expand first
    public int lengthOfLongestSubstringV3(String s) {
        Map<Character, Integer> window = new HashMap<>();
        int l = 0;
        int longestLength = 0;

        for (int r = 0; r < s.length(); ) {
            char c = s.charAt(r);
            window.put(c, window.getOrDefault(c, 0) + 1);
            r++;
            // "abcabcbb"
            //  ^  ^
            // move left until it doesn't contain duplicates
            while (1 < window.getOrDefault(c, 0)) {
                // update window
                window.computeIfPresent(s.charAt(l), (_, count) -> count == 1 ? null : count - 1);
                l++;
            }
            // "abcabcbb"
            //   ^ ^
            longestLength = Math.max(longestLength, r - l);
        }

        return longestLength;
    }

    // Shrink first
    public int lengthOfLongestSubstringV2(String s) {
        Set<Character> window = new HashSet<>();
        int l = 0;
        int longestLength = 0;
        for (int r = 0; r < s.length(); r++) {
            // move left until it doesn't contain
            while (window.contains(s.charAt(r))) {
                // update window
                window.remove(s.charAt(l));
                l++;
            }
            window.add(s.charAt(r));
            longestLength = Math.max(longestLength, r - l + 1);
        }

        return longestLength;
    }

    // Instinct but incorrect
    public int lengthOfLongestSubstringV1(String s) {
        Set<Character> window = new HashSet<>();
        int l = 0;
        int longestLength = 0;
        for (int r = 0; r < s.length(); r++) {
            if (window.contains(s.charAt(r))) {
                // move left until it doesn't contain
                while (window.contains(s.charAt(r))) {
                    // update window
                    window.remove(s.charAt(l));
                    l++;
                }
            } else {
                window.add(s.charAt(r));
                longestLength = Math.max(longestLength, r - l);
            }
        }

        return longestLength;
    }

}
