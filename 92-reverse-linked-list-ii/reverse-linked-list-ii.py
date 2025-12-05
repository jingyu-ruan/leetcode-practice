# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head

        num = 0
        dummy = ListNode(0, head)
        cur = dummy
        while cur:
            if num == left - 1:
                left_end = cur
            if num == left:
                rev_head = cur
            if num == right:
                rev_tail = cur
            
            cur = cur.next
            num += 1

        right_start = rev_tail.next
        rev_tail.next = None
        prev = None
        cur = rev_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        left_end.next = prev
        rev_head.next = right_start

        return dummy.next

