package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class LeetCode_20_Valid_Parentheses {
    // Time: O(n)
    // Auxiliary space: O(n)
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> brackets = new HashMap<>();
        brackets.put('(', ')');
        brackets.put('[', ']');
        brackets.put('{', '}');

        for (char c : s.toCharArray()) {
            if (brackets.containsKey(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                } else {
                    if (c != brackets.get(stack.pop())) {
                        return false;
                    }
                }
            }
        }

        return stack.isEmpty();
    }
}
