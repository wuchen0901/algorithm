package com.leetcode;

public class LeetCode_76_Minimum_Window_Substring {

    public String minWindow(String s, String target) {
        // What size array should I use for freq here?
        // Why should I use an array of size 128?
        // Why should the array size be 128?
        int[] windowFreq = new int[128];
        int[] targetFreq = new int[128];
        int unmatchedCount = 0;
        for (int i = 0; i < target.length(); i++) {
            char c = target.charAt(i);
            if (targetFreq[c] == 0) {
                unmatchedCount++;
            }
            targetFreq[c]++;
        }

        String result = "";
        int resultLength = 100000;

        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);

            if (0 < targetFreq[rightChar]) {
                windowFreq[rightChar]++;
                if (windowFreq[rightChar] == targetFreq[rightChar]) {
                    unmatchedCount--;
                }
            }

            while (unmatchedCount == 0) {
                if (right - left + 1 < resultLength) {
                    result = s.substring(left, right + 1);
                    resultLength = right - left + 1;
                }

                char leftChar = s.charAt(left);

                if (0 < targetFreq[leftChar]) {
                    windowFreq[leftChar]--;
                    if (windowFreq[leftChar] == targetFreq[leftChar] - 1) {
                        unmatchedCount++;
                    }
                }

                left++;
            }
        }

        return result;
    }
}
