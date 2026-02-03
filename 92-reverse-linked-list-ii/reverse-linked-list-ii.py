# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        num = -1
        prev = None
        while cur:
            num += 1
            if num == left - 1:
                last_end = cur
            if left <= num <= right:
                nxt = cur.next
                cur.next = prev
                prev = cur
                if num == left:
                    end = cur

                if num == right:
                    start = cur
                    end.next = nxt
                    last_end.next = start
                    return dummy.next
                cur = nxt
            else:
                cur = cur.next
        
            
# D 1 2 3 4 5
# 0 1 2 3 4 5