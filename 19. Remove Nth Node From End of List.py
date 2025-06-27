# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Step 1: fast 先走 n+1 步（确保 slow 停在要删除节点的前一个）
        for _ in range(n + 1):
            fast = fast.next

        # Step 2: fast 和 slow 一起走，直到 fast 走到末尾
        while fast:
            fast = fast.next
            slow = slow.next

        # Step 3: 删除 slow.next
        slow.next = slow.next.next

        return dummy.next
