package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_438_Find_All_Anagrams_in_a_String {
    public List<Integer> findAnagrams(String s, String p) {
        int[] freq = new int[26];

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < p.length(); i++) {
            freq[p.charAt(i) - 'a']++;
        }

        for (int r = 0; r < s.length(); r++) {
            freq[s.charAt(r) - 'a']--;
            int l = r - p.length();
            if (-1 <= l) {
                if (0 <= l) {
                    freq[s.charAt(l) - 'a']++;
                }

                boolean isAnagram = true;

                for (int i = 0; i < freq.length; i++) {
                    if (freq[i] != 0) {
                        isAnagram = false;
                        break;
                    }
                }

                if (isAnagram) {
                    result.add(l + 1);
                }
            }
        }

        return result;
    }
}
