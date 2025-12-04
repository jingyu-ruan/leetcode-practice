# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        heap = []
        cnt = 0
        while cur:
            heapq.heappush(heap, (cur.val, cnt, cur))
            cur = cur.next
            cnt += 1
        dummy = ListNode(0)
        cur = dummy
        while heap:
            v, c, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
        
        cur.next = None
        return dummy.next