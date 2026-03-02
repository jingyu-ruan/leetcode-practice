# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        D  1  2  3  4  5
        le cs ce ns 
        '''
        dummy = ListNode(0, head)
        last_end = dummy
        cur_start = last_end.next
        while True:
            p = last_end
            for _ in range(k):
                p = p.next
                if not p:
                    return dummy.next
            cur_end = p
            next_start = p.next

            last_end.next = None
            cur_end.next = None
            prev = None
            cur = cur_start
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            cur_start.next = next_start
            last_end.next = cur_end

            last_end = cur_start
            cur_start = last_end.next

