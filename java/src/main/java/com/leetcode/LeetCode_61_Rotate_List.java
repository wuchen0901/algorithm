package com.leetcode;

import com.leetcode.common.ListNode;

public class LeetCode_61_Rotate_List {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) {
            return null;
        }

        ListNode tail = head;
        int length = 1;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }

        // build a loop
        tail.next = head;

        k %= length;

        for (int i = 0; i < length - k; i++) {
            tail = tail.next;
        }

        ListNode result = tail.next;
        tail.next = null;
        return result;
    }
}
