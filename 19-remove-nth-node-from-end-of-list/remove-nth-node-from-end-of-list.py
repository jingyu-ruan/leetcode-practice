# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # cur = head
        length = 0
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur:
            length += 1
            cur = cur.next
        
        cur = dummy
        while cur:
            length -= 1
            if length - n == 0:
                nxt = cur.next.next
                cur.next = nxt
                break
            cur = cur.next
        
        return dummy.next
