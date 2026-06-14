package com.leetcode;

import com.leetcode.common.ListNode;

public class LeetCode_21_Merge_Two_Sorted_Lists {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null)
            return list2;
        if (list2 == null)
            return list1;

        ListNode head = new ListNode();
        ListNode p = head;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                p.next = list1;
                list1 = list1.next;
            } else {
                p.next = list2;
                list2 = list2.next;
            }
            p = p.next;
        }

        if (list1 == null) {
            p.next = list2;
        }

        if (list2 == null) {
            p.next = list1;
        }

        return head.next;
    }
}
