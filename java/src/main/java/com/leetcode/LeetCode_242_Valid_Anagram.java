package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_242_Valid_Anagram {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> counter = new HashMap<>();
        for (char c : s.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            if (counter.containsKey(c)) {
                counter.compute(c, (k, v) -> v == 1 ? null : v - 1);
            } else {
                return false;
            }

        }

        return counter.isEmpty();
    }
}
