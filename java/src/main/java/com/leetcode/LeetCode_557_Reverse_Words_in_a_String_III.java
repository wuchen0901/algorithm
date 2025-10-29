package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode_557_Reverse_Words_in_a_String_III {
    public String reverseWords(String s) {
        String[] tokens = s.split("\\s+");
        List<String> words = new ArrayList<>(tokens.length);
        for (String token : tokens) {
            words.add(new StringBuilder(token).reverse().toString());
        }

        return String.join(" ", words);
    }
}
