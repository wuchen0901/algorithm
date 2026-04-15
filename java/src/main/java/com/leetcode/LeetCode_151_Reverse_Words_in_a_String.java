package com.leetcode;

public class LeetCode_151_Reverse_Words_in_a_String {
    public String reverseWords(String s) {
        char[] chars = s.toCharArray();
        int length = cleanSpaces(chars);
        reverse(chars, 0, length - 1);

        int left = 0;
        int right = 0;
        while (right < length) {
            while (right < length && chars[right] != ' ') {
                right++;
            }

            reverse(chars, left, right - 1);
            right++;
            left = right;
        }

        return new String(chars, 0, length);
    }

    private int cleanSpaces(char[] chars) {
        int fast = 0;
        int slow = 0;

        while (fast < chars.length) {
            while (fast < chars.length && chars[fast] == ' ') {
                fast++;
            }

            while (fast < chars.length && chars[fast] != ' ') {
                chars[slow] = chars[fast];
                fast++;
                slow++;
            }

            while (fast < chars.length && chars[fast] == ' ') {
                fast++;
            }

            if (fast < chars.length) {
                chars[slow] = ' ';
                slow++;
            }
        }

        return slow;
    }

    private void reverse(char[] chars, int left, int right) {
        // close interval
        while (left < right) {
            char c = chars[right];
            chars[right] = chars[left];
            chars[left] = c;
            left++;
            right--;
        }
    }
}
