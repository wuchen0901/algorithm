package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode_76_Minimum_Window_Substring {

    public String minWindow(String s, String t) {
        HashMap<Character, Integer> target = new HashMap<>();
        for (char c : t.toCharArray()) {
            target.put(c, target.getOrDefault(c, 0) + 1);
        }

        HashMap<Character, Integer> window = new HashMap<>();
        int left = 0;

        int length = Integer.MAX_VALUE;
        String result = "";
        for (int right = 0; right < s.length(); ) {
            // move right until all characters in t are included
            while (right < s.length() && !containsAllElements(target, window)) {
                // update window
                window.put(s.charAt(right), window.getOrDefault(s.charAt(right), 0) + 1);

                right++;
            }
            // A        B
            // true     true
            // false    true
            // true     false
            // false    false
            System.out.println("right = " + right);
            // move left until not all are included
            while (containsAllElements(target, window)) {
                if (right - left < length) {
                    result = s.substring(left, right);
                    length = result.length();
                }
                window.computeIfPresent(s.charAt(left), (c, count) -> count == 1 ? null : count - 1);
                left++;
            }
        }

        return result;
    }

    boolean containsAllElements(HashMap<Character, Integer> target, HashMap<Character, Integer> window) {
        boolean included = true;
        for (Map.Entry<Character, Integer> entry : target.entrySet()) {
            if (window.getOrDefault(entry.getKey(), 0) < entry.getValue()) {
                included = false;
            }
        }
        return included;
    }

    public static void main(String[] args) {
        LeetCode_76_Minimum_Window_Substring solution = new LeetCode_76_Minimum_Window_Substring();
//        System.out.println(solution.minWindow("ADOBECODEBANC", "ABC"));
        System.out.println(solution.minWindow("cabwefgewcwaefgcf", "cae"));
    }
}
