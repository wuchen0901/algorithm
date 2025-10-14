package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class LeetCode_3_Longest_Substring_Without_Repeating_Characters {
    // template like but incorrect
    public int lengthOfLongestSubstringV2(String s) {
        Set<Character> window = new HashSet<>();
        int l = 0;
        int longestLength = 0;
        for (int r = 0; r < s.length(); r++) {
            longestLength = Math.max(longestLength, r - l);

            // move left until it doesn't contain
            while (window.contains(s.charAt(r))) {
                // update window
                window.remove(s.charAt(l));
                l++;
            }
            window.add(s.charAt(r));

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
