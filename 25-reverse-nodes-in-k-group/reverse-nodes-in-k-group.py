# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        last_end = dummy
        # start = head
        cur = dummy
        while True:
            cur = last_end
            cur_start = cur.next
            for _ in range(k):
                cur = cur.next
                if not cur:
                    return dummy.next
            cur_end = cur
            next_start = cur.next
            # start reverse
            cur_end.next = None
            last_end.next = None
            p = cur_start
            prev = None
            while p:
                nxt = p.next
                p.next = prev
                prev = p
                p = nxt
            cur_start.next = next_start
            last_end.next = cur_end

            last_end = cur_start
