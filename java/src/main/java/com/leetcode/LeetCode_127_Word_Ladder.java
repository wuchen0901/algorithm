package com.leetcode;

import java.util.*;

public class LeetCode_127_Word_Ladder {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        Queue<String> queue = new ArrayDeque<>();
        queue.offer(beginWord);

        int step = 1;

        while (!queue.isEmpty()) {

            int size = queue.size();

            for (int s = 0; s < size; s++) {
                String word = queue.poll();

                for (String adjancency : getAdjacency(wordSet, word)) {
                    if (adjancency.equals(endWord)) {
                        return step + 1;
                    } else {
                        queue.offer(adjancency);
                    }
                }
            }

            step++;
        }

        return 0;
    }

    private List<String> getAdjacency(Set<String> wordSet, String target) {
        List<String> adjacency = new ArrayList<>();

        for (int i = 0; i < target.length(); i++) {
            for (char c = 'a'; c <= 'z'; c++) {
                String w = target.substring(0, i) + c + target.substring(i + 1);

                if (wordSet.contains(w)) {
                    adjacency.add(w);
                    wordSet.remove(w);
                }
            }
        }

        return adjacency;
    }
}
