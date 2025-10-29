package com.leetcode;

public class LeetCode_344_Reverse_String {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        // []
        // [1, 2, 3]
        // [1, 2, 3, 4]
        while (left < right) {
            char value = s[left];
            s[left] = s[right];
            s[right] = value;
            left++;
            right--;
        }
    }
}
