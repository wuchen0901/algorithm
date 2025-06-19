# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # previous
        # TODO: head == None
        # TODO: head is the only node
        previous = head
        p = previous.next

        while p is not None:
            n = p.next
            p.next = previous
            previous = p
            p = n

        return p

