package com.leetcode;

import com.leetcode.common.ListNode;

/**
 * Time: O(n)
 * Space: O(1)
 */
public class LeetCode_876_Middle_of_the_Linked_List {
    public ListNode middleNode(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        return slow;
    }
}
