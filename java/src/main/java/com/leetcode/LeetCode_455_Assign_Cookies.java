package com.leetcode;

import java.util.Arrays;

public class LeetCode_455_Assign_Cookies {
    public int findContentChildren(int[] greed, int[] cookies) {
        Arrays.sort(greed);
        Arrays.sort(cookies);
        int childIndex = 0;
        int contentCount = 0;
        for (int cookie : cookies) {
            if (childIndex < greed.length) {
                if (greed[childIndex] <= cookie) {
                    contentCount++;
                    childIndex++;
                }
            } else {
                return contentCount;
            }
        }

        return contentCount;
    }

    public int findContentChildrenV2(int[] g, int[] s) {
        Integer[] G = Arrays.stream(g).boxed().toArray(Integer[]::new);
        Integer[] S = Arrays.stream(s).boxed().toArray(Integer[]::new);
        Arrays.sort(G, (a, b) -> b - a);
        Arrays.sort(S, (a, b) -> b - a);

        int i = 0; // child
        int j = 0; // cookie
        int content = 0;

        while (i < G.length && j < S.length) {
            if (S[j] >= G[i]) { // give big cookie to the greediest remaining child
                content++;
                i++;
                j++;
            } else {
                i++; // try a less greedy child
            }
        }
        return content;
    }
}
