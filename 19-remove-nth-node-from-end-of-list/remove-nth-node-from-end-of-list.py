# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        p_slow, p_fast = dummy, dummy
        for i in range(n + 1):
            p_fast = p_fast.next

        while p_fast:
            p_fast = p_fast.next
            p_slow = p_slow.next

        p_slow.next = p_slow.next.next

        return dummy.next
