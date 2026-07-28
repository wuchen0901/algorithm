package com.leetcode;

public class LeetCode_208_Implement_Trie {

    TrieNode root = new TrieNode();

    public LeetCode_208_Implement_Trie() {

    }

    public void insert(String word) {
        TrieNode current = root;

        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (current.children[index] == null) {
                current.children[index] = new TrieNode();
            }

            current = current.children[index];
        }

        current.isWord = true;
    }

    public boolean search(String word) {
        TrieNode current = root;

        for (char c : word.toCharArray()) {
            int index = c - 'a';

            if (current.children[index] == null) {
                return false;
            } else {
                current = current.children[index];
            }
        }

        return current.isWord;
    }

    public boolean startsWith(String prefix) {
        TrieNode current = root;

        for (char c : prefix.toCharArray()) {
            int index = c - 'a';

            if (current.children[index] == null) {
                return false;
            } else {
                current = current.children[index];
            }
        }

        return true;
    }
}

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isWord = false;
}
