# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = head
        dummy.next = head
        node_len = 0    
        while cur:
            node_len += 1
            cur = cur.next

        p = dummy
        lft = node_len
        while p:
            lft -= 1
            if lft - n == -1:
                p.next = p.next.next
                break
            p = p.next
                

        return dummy.next 