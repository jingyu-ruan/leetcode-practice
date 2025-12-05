# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head

        dummy = ListNode(0, head)
        cur = dummy
        last_end = dummy
        while True:
            # last_end = cur
            cur = last_end
            for i in range(k):
                cur = cur.next
                if not cur:
                    return dummy.next
            
            cur_end = cur
            nxt_start = cur.next
            cur_start = last_end.next
            last_end.next = None
            cur_end.next = None

            prev = None
            cur = cur_start
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            last_end.next = cur_end
            cur_start.next = nxt_start
            last_end = cur_start
            
        return dummy.next