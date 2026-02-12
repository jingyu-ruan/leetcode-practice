# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        last_end = dummy
        while True:
            for _ in range(2):
                cur = cur.next
                if not cur:
                    return dummy.next
            next_start = cur.next
            cur_end = cur
            cur.next = None
            cur_start = last_end.next
            last_end.next = None

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
            cur = last_end
