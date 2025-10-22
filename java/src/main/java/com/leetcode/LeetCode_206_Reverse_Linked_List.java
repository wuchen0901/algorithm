package com.leetcode;

import com.leetcode.common.ListNode;

public class LeetCode_206_Reverse_Linked_List {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }

        if (head.next == null) {
            return head;
        }

        ListNode l = head;
        ListNode r = head.next;
        l.next = null;
        // 3 -> 6 -> 8
        // l    r    next
        while (r.next != null) {
            ListNode next = r.next;
            r.next = l;
            l = r;
            r = next;
        }

        r.next = l;

        return r;
    }
}
