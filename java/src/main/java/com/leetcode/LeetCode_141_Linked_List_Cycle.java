package com.leetcode;

import com.leetcode.common.ListNode;

public class LeetCode_141_Linked_List_Cycle {
    public boolean hasCycle(ListNode head) {
        // 0 node
        // 1 node has cycle
        // 1 node no cycle
        // 2 node has cycle
        if (head == null) {
            return false;
        }

        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;

            if (fast == slow) {
                return true;
            }
        }

        return false;
    }
}
