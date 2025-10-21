package com.leetcode;

import com.leetcode.common.ListNode;

public class LeetCode_2_Add_Two_Numbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }

        if (l2 == null) {
            return l1;
        }

        ListNode result = l1;

        int carry = 0;

        while (l1.next != null && l2.next != null) {
            l1.val += l2.val + carry;
            carry = 0;
            if (10 <= l1.val) {
                l1.val -= 10;
                carry = 1;
            }

            l1 = l1.next;
            l2 = l2.next;
        }

        // 3 -> 5 -> 8 -> null
        // 2 -> 4 -> null
        l1.val += l2.val + carry;
        carry = 0;
        if (10 <= l1.val) {
            l1.val -= 10;
            carry = 1;
        }

        if (l1.next == null) {
            l1.next = l2.next;
        }

        while (carry == 1) {
            if (l1.next == null) {
                l1.next = new ListNode(1);
                carry = 0;
            } else {
                l1.next.val += carry;
                carry = 0;
                if (10 <= l1.next.val) {
                    l1.next.val -= 10;
                    carry = 1;
                }
                l1 = l1.next;
            }
        }
        return result;
    }
}
